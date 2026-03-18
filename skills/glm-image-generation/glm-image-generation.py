#!/usr/bin/env python3
"""
GLM Text-to-Image Generation Script

Generates images from text prompts using GLM's cogview models.

Usage:
    uv run python glm-image-generation "一只可爱的小猫咪，坐在窗台上"
    uv run python glm-image-generation -m cogview-4 "专业人像照"
    uv run python glm-image-generation -s 1920x1080 "风景画"
"""

import os
import sys
import json
import time
from pathlib import Path
from datetime import datetime
from typing import Optional, Dict, Any

import click
from dotenv import load_dotenv
import requests
from PIL import Image
from PIL.PngImagePlugin import PngInfo

# Load environment variables
load_dotenv()

# Model endpoint mapping
MODEL_ENDPOINTS = {
    "cogview-3-flash": "cogview-3-flash",
    "cogview-4": "cogview-4",
    "cogview-4-250304": "cogview-4-250304",
    "glm-image": "glm-image",
}

# Default model
DEFAULT_MODEL = "cogview-3-flash"

# Premium models that incur costs
PREMIUM_MODELS = ["cogview-4", "cogview-4-250304", "glm-image"]

# API configuration
API_URL = "https://open.bigmodel.cn/api/paas/v4/images/generations"

# Size mapping - cogview-3-flash, cogview-4, cogview-4-250304
SIZE_OPTIONS = {
    "1024x1024": "1024x1024",
    "768x1344": "768x1344",
    "1152x864": "1152x864",
    "864x1152": "864x1152",
    "1344x768": "1344x768",
    "1440x720": "1440x720",
    "720x1440": "720x1440",
}

# glm-image specific sizes
GLM_IMAGE_SIZES = {
    "1280x1280": "1280x1280",
    "1568x1056": "1568x1056",
    "1056x1568": "1056x1568",
    "1472x1088": "1472x1088",
    "1088x1472": "1088x1472",
    "1728x960": "1728x960",
    "960x1728": "960x1728",
}


def check_api_key() -> Optional[str]:
    """
    Check if ZHIPU_API_KEY is configured.

    Returns:
        API key if configured, None otherwise
    """
    api_key = os.getenv("ZHIPU_API_KEY")
    if not api_key:
        click.echo("✗ Error: ZHIPU_API_KEY environment variable not set", err=True)
        click.echo("\nSet your API key:", err=True)
        click.echo("  export ZHIPU_API_KEY='your-api-key-here'", err=True)
        click.echo("\nGet your key at: https://open.bigmodel.cn/", err=True)
        return None
    return api_key


def show_cost_warning(model: str) -> None:
    """
    Show warning if using premium model.

    Args:
        model: Model name to check
    """
    if model in PREMIUM_MODELS:
        click.echo(
            f"\n⚠️  Warning: Using premium model '{model}'. This may incur charges."
        )
        click.echo(f"   Current default: {DEFAULT_MODEL} (low cost)")
        click.echo(f"   Continue? (y/n): ", nl=False)

        try:
            response = input()
            if response.lower() != "y":
                click.echo("Generation cancelled.")
                sys.exit(0)
        except (EOFError, KeyboardInterrupt):
            click.echo("\nGeneration cancelled.")
            sys.exit(0)


def prepare_output_dir() -> Path:
    """
    Prepare output directory for generated images.

    Returns:
        Path to output directory
    """
    # Get the workspace root (project root)
    script_dir = Path(__file__).parent.resolve()
    # Go up to project root: .agents/skills/glm-image-generation -> ../../..
    project_root = script_dir.parent.parent.parent
    output_dir = project_root / ".glm_aigc"
    output_dir.mkdir(parents=True, exist_ok=True)
    return output_dir


def generate_image(
    prompt: str,
    model: str,
    size: str,
    quality: str,
    watermark: bool,
    api_key: str,
    user_id: Optional[str] = None,
    timeout: int = 120,
) -> Dict[str, Any]:
    """
    Generate image using GLM API.

    Args:
        prompt: Text prompt for image generation
        model: Model to use
        size: Image size
        quality: Quality level
        watermark: Whether to include watermark
        api_key: API key
        timeout: Request timeout in seconds

    Returns:
        Response data including image URL
    """
    headers = {"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"}

    payload = {
        "model": model,
        "prompt": prompt,
        "size": size,
        "watermark_enabled": watermark,
        "quality": quality,
    }

    # Add user_id if provided (for compliance)
    if user_id:
        payload["user_id"] = user_id

    click.echo(f"\n{'=' * 60}")
    click.echo(f"Generating image with {model}")
    click.echo(f"{'=' * 60}")
    click.echo(f"Prompt: {prompt}")
    click.echo(f"Size: {size}")
    click.echo(f"Quality: {quality}")
    click.echo(f"Watermark: {'enabled' if watermark else 'disabled'}")
    click.echo(f"{'=' * 60}\n")

    start_time = time.time()
    click.echo("⏳ Generating image...")

    try:
        response = requests.post(
            API_URL, json=payload, headers=headers, timeout=timeout
        )

        generation_time = time.time() - start_time

        response.raise_for_status()
        result = response.json()

        click.echo(f"✓ Generated in {generation_time:.2f}s")

        return result

    except requests.exceptions.Timeout:
        click.echo(f"✗ Generation timeout after {timeout}s", err=True)
        return {}
    except requests.exceptions.RequestException as e:
        click.echo(f"✗ API request failed: {e}", err=True)
        return {}
    except json.JSONDecodeError as e:
        click.echo(f"✗ Failed to parse response: {e}", err=True)
        return {}


def extract_image_url(result: Dict[str, Any]) -> Optional[str]:
    """
    Extract image URL from API response.

    Args:
        result: API response data

    Returns:
        Image URL or None
    """
    try:
        # GLM API response format
        if "data" in result and len(result["data"]) > 0:
            return result["data"][0].get("url")

        # Alternative format
        if "images" in result and len(result["images"]) > 0:
            return result["images"][0].get("url")

        # Single image format
        if "image" in result:
            return result["image"].get("url")

    except (KeyError, IndexError, TypeError):
        pass

    return None


def save_image_with_metadata(
    image_url: str, output_path: Path, prompt: str, model: str, metadata: Dict[str, Any]
) -> None:
    """
    Download and save image with embedded metadata.

    Args:
        image_url: URL of generated image
        output_path: Where to save the image
        prompt: Generation prompt
        model: Model used
        metadata: Additional metadata to embed
    """
    try:
        # Download image
        response = requests.get(image_url, timeout=30)
        response.raise_for_status()

        # Save as PNG
        output_path.write_bytes(response.content)

        click.echo(f"✓ Image saved: {output_path}")

    except Exception as e:
        click.echo(f"✗ Failed to save image: {e}", err=True)
        raise


@click.command()
@click.argument("prompt", required=True)
@click.option(
    "-m",
    "--model",
    type=click.Choice(list(MODEL_ENDPOINTS.keys()), case_sensitive=False),
    default=DEFAULT_MODEL,
    help=f"Model to use (default: {DEFAULT_MODEL})",
)
@click.option(
    "-s",
    "--size",
    type=str,
    default="1024x1024",
    help="Image size (default: 1024x1024). For glm-image: 1280x1280, 1568x1056, etc. For others: 1024x1024, 768x1344, etc.",
)
@click.option(
    "-q",
    "--quality",
    type=click.Choice(["standard", "hd"], case_sensitive=False),
    default="hd",
    help="Quality level (default: hd). Use 'hd' for glm-image, 'standard' for fast generation.",
)
@click.option(
    "-o",
    "--output",
    type=str,
    help="Output filename (default: generated_TIMESTAMP.png)",
)
@click.option(
    "--watermark",
    is_flag=True,
    default=False,
    help="Enable watermark (default: disabled)",
)
@click.option(
    "--user-id",
    type=str,
    help="End user ID for compliance (6-128 characters)",
)
def main(
    prompt: str,
    model: str,
    size: str,
    quality: str,
    output: Optional[str],
    watermark: bool,
    user_id: Optional[str],
) -> None:
    """
    Generate images from text prompts using GLM models.

    PROMPT: Text description of the image to generate

    Examples:

        uv run python glm-image-generation "一只可爱的小猫咪"

        uv run python glm-image-generation -m cogview-4 "专业人像照"

        uv run python glm-image-generation -s 1920x1080 "风景画"
    """
    # Check API key
    api_key = check_api_key()
    if not api_key:
        sys.exit(1)

    # Show cost warning for premium models
    if model != DEFAULT_MODEL:
        show_cost_warning(model)

    # Prepare output directory
    output_dir = prepare_output_dir()

    # Generate image
    result = generate_image(
        prompt=prompt,
        model=model,
        size=size,
        quality=quality,
        watermark=watermark,
        api_key=api_key,
        user_id=user_id,
    )

    if not result:
        sys.exit(1)

    # Extract image URL
    image_url = extract_image_url(result)
    if not image_url:
        click.echo("✗ Failed to extract image URL from response", err=True)
        click.echo(f"Response: {json.dumps(result, indent=2)}", err=True)
        sys.exit(1)

    # Prepare output path
    if output is None:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        output = f"generated_{model.replace('-', '_')}_{timestamp}.png"
        output_path = output_dir / output
    else:
        output_path = Path(output)
        if not output_path.is_absolute():
            output_path = output_dir / output_path

    output_path.parent.mkdir(parents=True, exist_ok=True)

    # Save image
    metadata = {
        "model": model,
        "size": size,
        "quality": quality,
        "watermark": watermark,
    }

    try:
        save_image_with_metadata(
            image_url=image_url,
            output_path=output_path,
            prompt=prompt,
            model=model,
            metadata=metadata,
        )

        click.echo(f"\nImage URL: {image_url}")
        click.echo(f"{'=' * 60}\n")
        click.echo(f"✓ Generation completed successfully!")

    except Exception as e:
        sys.exit(1)


if __name__ == "__main__":
    main()

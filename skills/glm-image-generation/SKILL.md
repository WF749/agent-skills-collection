---
name: glm-image-generation
description: Generate images using GLM's text-to-image models (cogview-4, cogview-3-flash). Use this skill whenever user wants to create images from text descriptions, mentions GLM, cogview, or image generation.
---

# GLM Text-to-Image Generation Skill

Generate high-quality images from text prompts using GLM's state-of-the-art text-to-image models.

## When to Use This Skill

Trigger when user:
- Requests image generation from text descriptions
- Wants to create images with AI
- Mentions GLM, cogview, or Zhipu AI models
- Asks for text-to-image or AI drawing
- Needs to generate pictures from prompts

## Quick Start

### Basic Usage
```bash
uv run python glm-image-generation "一只可爱的小猫咪，坐在窗台上"
```

### With Custom Size
```bash
uv run python glm-image-generation "风景画" -s 1920x1080
```

### Using Premium Model (will show cost warning)
```bash
uv run python glm-image-generation "专业人像照" -m glm-image
```

## Supported Models

| Model | Description | Cost |
|-------|-------------|------|
| `cogview-3-flash` | **Default** - Fast generation, good quality | Free/Low cost |
| `cogview-4` | High quality, more detailed | Paid |
| `cogview-4-250304` | Latest version, best quality | Paid |
| `glm-image` | Newest model (2025) | Paid |

**Note**: When using paid models (`cogview-4`, `cogview-4-250304`, `glm-image`), the script will warn about potential costs. Default `cogview-3-flash` is recommended for testing.

## Command-Line Interface

```bash
uv run python glm-image-generation [OPTIONS] PROMPT

Arguments:
  PROMPT                    Text description of the image to generate

Options:
  -m, --model TEXT          Model to use (default: cogview-3-flash)
  -s, --size TEXT           Image size (default: 1024x1024)
                           For cogview models: 1024x1024, 768x1344, 1152x864, etc.
                           For glm-image: 1280x1280, 1568x1056, 1056x1568, etc.
  -q, --quality TEXT       Quality: standard or hd (default: hd)
                           hd: Higher quality, ~20s (glm-image only)
                           standard: Fast generation, 5-10s
  -o, --output TEXT        Output filename
  --watermark              Enable watermark (default: disabled)
  --user-id TEXT          End user ID for compliance (6-128 chars)
  --help                   Show this message and exit
```

## Authentication Setup

Before first use, set your GLM API key:

```bash
export ZHIPU_API_KEY="your-api-key-here"
```

Get your API key from: https://open.bigmodel.cn/

## Size Options

### For cogview-3-flash, cogview-4, cogview-4-250304:
| Size | Aspect Ratio | Best For |
|------|--------------|----------|
| 1024x1024 | 1:1 | General use (default) |
| 768x1344 | 9:16 | Portrait, mobile |
| 1152x864 | 4:3 | Landscape |
| 864x1152 | 3:4 | Portrait |
| 1344x768 | 16:9 | Landscape, banners |
| 1440x720 | 2:1 | Ultra-wide |
| 720x1440 | 9:18 | Tall portrait |

### For glm-image:
| Size | Aspect Ratio | Best For |
|------|--------------|----------|
| 1280x1280 | 1:1 | High-res square (default) |
| 1568x1056 | 3:2 | Landscape |
| 1056x1568 | 2:3 | Portrait |
| 1472x1088 | 4:3 | Standard landscape |
| 1088x1472 | 3:4 | Standard portrait |
| 1728x960 | 16:9 | Wide landscape |
| 960x1728 | 9:16 | Tall portrait |

## Quality Options

- `standard`: Fast generation (5-10 seconds), suitable for most scenarios
- `hd`: Higher quality, more details, ~20 seconds (glm-image model only)

## Output

Images are saved to: `.glm_aigc/` (in project root)

Generated images include:
- Timestamp in filename
- Prompt as metadata (if supported)
- Console displays generation time

## Examples

### Simple Image Generation
```bash
uv run python glm-image-generation "一只可爱的橘猫在阳光下打盹"
```

### High Quality with Custom Size
```bash
uv run python glm-image-generation \
  "未来科技城市夜景" \
  -s 1344x768 \
  -q standard \
  -m cogview-4
```

### Save to Custom Location
```bash
uv run python glm-image-generation "动漫风格少女" -o my_image.png
```

## Troubleshooting

| Problem | Solution |
|---------|----------|
| `ZHIPU_API_KEY not set` | Export ZHIPU_API_KEY environment variable |
| `API request failed` | Check API key validity and account balance |
| `Generation timeout` | Try standard quality or smaller size |
| `Rate limit error` | Wait a moment and retry |

## Cost Warning

When using non-default models, the script will display:
```
⚠️ Warning: Using premium model [model-name]. This may incur charges.
   Current default: cogview-3-flash (low cost)
```

## File Structure

```
glm-image-generation/
├── SKILL.md                        # This file
├── pyproject.toml                  # Dependencies (uv)
├── glm-image-generation.py         # Main executable script
└── evals/
    └── evals.json                  # Test cases
```

## Dependencies

Managed via `uv`:
- `requests`: HTTP client for API calls
- `python-dotenv`: Environment variable management
- `click`: CLI interface
- `pillow`: Image handling

## Best Practices

1. **Start with default model**: Use `cogview-3-flash` for testing
2. **Prompt engineering**: Be specific and descriptive for better results
3. **Size selection**: Use appropriate size for your use case
4. **Check costs**: Monitor usage on GLM dashboard for paid models

## Resources

- GLM API Documentation: https://open.bigmodel.cn/dev/api
- API Keys Management: https://open.bigmodel.cn/
- Pricing: Check your dashboard for latest pricing

## Limitations

- Requires active ZHIPU_API_KEY
- Subject to GLM rate limits and quotas
- Internet connection required
- Some models have usage costs
- Watermark is disabled by default (use --watermark to enable)

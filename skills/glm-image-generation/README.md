# GLM Image Generation Skill

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)

**English** | [简体中文](README.zh-CN.md)

Generate high-quality images from text prompts using GLM's state-of-the-art text-to-image models including cogview-3-flash, cogview-4, and glm-image.

## ✨ Features

- 🎨 **Multiple Models**: Support for cogview-3-flash (default), cogview-4, cogview-4-250304, and glm-image
- 📏 **Flexible Sizes**: Multiple aspect ratios for different use cases
- ⚡ **Quality Options**: Standard (fast) or HD (high-quality) modes
- 🔇 **No Watermark**: Watermark disabled by default
- 📁 **Auto Save**: Images automatically saved to `.glm_aigc/` directory
- ⚠️ **Cost Awareness**: Automatic warnings when using premium models
- 🔒 **Compliance**: User ID support for regulatory compliance

## 🚀 Quick Start

### Prerequisites

1. **Python 3.10+** required
2. **uv** package manager
3. **ZHIPU_API_KEY** environment variable

### Installation

```bash
# Install via npx skills (recommended)
npx skills add biiigwang/agent-skills-collection --skill glm-image-generation

# Or clone and install manually
cd skills/glm-image-generation
uv sync
```

### Set API Key

```bash
export ZHIPU_API_KEY="your-api-key-here"
```

Get your API key from: https://open.bigmodel.cn/

### Basic Usage

```bash
# Simple image generation
uv run python glm-image-generation "一只可爱的小猫咪，坐在窗台上"

# With custom model
uv run python glm-image-generation "专业人像照" -m glm-image

# With custom size
uv run python glm-image-generation "风景画" -s 1344x768

# High quality mode
uv run python glm-image-generation "精细插画" -q hd
```

## 📖 Command Reference

```bash
uv run python glm-image-generation [OPTIONS] PROMPT

Arguments:
  PROMPT                    Text description of the image to generate

Options:
  -m, --model TEXT          Model to use (default: cogview-3-flash)
                            Options: cogview-3-flash, cogview-4, 
                                    cogview-4-250304, glm-image
  -s, --size TEXT           Image size (default: 1024x1024)
                            For cogview: 1024x1024, 768x1344, 1152x864, etc.
                            For glm-image: 1280x1280, 1568x1056, etc.
  -q, --quality TEXT        Quality: standard or hd (default: hd)
                            hd: Higher quality, ~20s (glm-image only)
                            standard: Fast generation, 5-10s
  -o, --output TEXT         Output filename
  --watermark               Enable watermark (default: disabled)
  --user-id TEXT           End user ID for compliance (6-128 chars)
  --help                    Show this message and exit
```

## 🎯 Supported Models

| Model | Description | Cost | Generation Time | Best For |
|-------|-------------|------|-----------------|----------|
| `cogview-3-flash` | **Default** - Fast generation | Low | 5-10s | Quick iterations, testing |
| `cogview-4` | High quality | Paid | 10-15s | Professional outputs |
| `cogview-4-250304` | Latest version | Paid | 10-15s | Best quality |
| `glm-image` | Newest model (2025) | Paid | ~20s | HD quality, detailed images |

## 📐 Size Options

### For cogview-3-flash, cogview-4, cogview-4-250304:

| Size | Aspect Ratio | Best For |
|------|--------------|----------|
| `1024x1024` | 1:1 | General use (default) |
| `768x1344` | 9:16 | Portrait, mobile |
| `1152x864` | 4:3 | Landscape |
| `864x1152` | 3:4 | Portrait |
| `1344x768` | 16:9 | Landscape, banners |
| `1440x720` | 2:1 | Ultra-wide |
| `720x1440` | 9:18 | Tall portrait |

### For glm-image:

| Size | Aspect Ratio | Best For |
|------|--------------|----------|
| `1280x1280` | 1:1 | High-res square (default) |
| `1568x1056` | 3:2 | Landscape |
| `1056x1568` | 2:3 | Portrait |
| `1472x1088` | 4:3 | Standard landscape |
| `1088x1472` | 3:4 | Standard portrait |
| `1728x960` | 16:9 | Wide landscape |
| `960x1728` | 9:16 | Tall portrait |

## 💡 Examples

### Simple Image Generation
```bash
uv run python glm-image-generation "一只可爱的橘猫在阳光下打盹"
```

### Professional Portrait
```bash
uv run python glm-image-generation \
  "Professional business headshot, studio lighting" \
  -m glm-image \
  -q hd \
  -s 1280x1280
```

### Landscape with Custom Size
```bash
uv run python glm-image-generation \
  "未来科技城市夜景，高楼大厦，霓虹灯，赛博朋克风格" \
  -s 1344x768 \
  -m cogview-4
```

### Chinese Traditional Style
```bash
uv run python glm-image-generation \
  "中国风山水画，青山绿水，亭台楼阁，水墨画风格" \
  -s 1152x864
```

### With User ID for Compliance
```bash
uv run python glm-image-generation \
  "测试图片" \
  --user-id "user123456"
```

## 📁 Output

Generated images are saved to:
```
<project-root>/.glm_aigc/generated_<model>_<timestamp>.png
```

Example:
```
my-project/.glm_aigc/generated_cogview_3_flash_20260318_230000.png
```

## ⚠️ Troubleshooting

### API Key Not Set
```
✗ Error: ZHIPU_API_KEY environment variable not set

# Solution:
export ZHIPU_API_KEY="your-api-key-here"
```

### Invalid Size for Model
```
✗ API request failed: 400 Bad Request

# Solution: Use appropriate size for your model
# cogview models: 1024x1024, 768x1344, etc.
# glm-image: 1280x1280, 1568x1056, etc.
```

### Premium Model Warning
```
⚠️ Warning: Using premium model 'glm-image'. This may incur charges.
   Current default: cogview-3-flash (low cost)
   Continue? (y/n):
```

### Generation Timeout
```
✗ Generation timeout after 120s

# Solution: 
# 1. Try standard quality instead of hd
# 2. Use smaller image size
# 3. Check network connection
```

### Rate Limit Error
```
✗ API request failed: 429 Too Many Requests

# Solution: Wait a moment and retry
```

## 🛠️ Development

### Local Testing

1. Navigate to skill directory:
```bash
cd skills/glm-image-generation
```

2. Install dependencies:
```bash
uv sync
```

3. Test with your API key:
```bash
export ZHIPU_API_KEY="your-api-key"
uv run python glm-image-generation "test prompt"
```

### Running Tests

Test cases are defined in `evals/evals.json`. Run them to verify functionality.

## 📦 Dependencies

- **Python**: 3.10+
- **uv**: Python package manager
- **click**: CLI interface
- **python-dotenv**: Environment management
- **requests**: HTTP client
- **pillow**: Image handling

## 🔗 Resources

- [GLM API Documentation](https://open.bigmodel.cn/dev/api)
- [Get API Key](https://open.bigmodel.cn/)
- [Skills.sh Documentation](https://skills.sh/docs/cli)

## 📝 License

MIT License - see main repository [LICENSE](../../LICENSE) file for details.

## 🤝 Contributing

Contributions are welcome! Please see the main repository for contribution guidelines.

## 📮 Support

- **Issues**: [Create an issue](https://github.com/biiigwang/agent-skills-collection/issues)
- **Author**: [@biiigwang](https://github.com/biiigwang)

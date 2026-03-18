# GLM Image Generation Skill

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)

**English** | [简体中文](README.zh-CN.md)

使用 GLM 的先进文本生成图像模型（包括 cogview-3-flash、cogview-4 和 glm-image）从文本提示生成高质量图像。

## ✨ 特性

- 🎨 **多种模型**：支持 cogview-3-flash（默认）、cogview-4、cogview-4-250304 和 glm-image
- 📏 **灵活尺寸**：多种宽高比适用于不同场景
- ⚡ **质量选项**：Standard（快速）或 HD（高质量）模式
- 🔇 **无水印**：默认禁用水印
- 📁 **自动保存**：图像自动保存到 `.glm_aigc/` 目录
- ⚠️ **费用感知**：使用付费模型时自动提示
- 🔒 **合规支持**：用户 ID 支持，满足监管要求

## 🚀 快速开始

### 前置条件

1. **Python 3.10+**
2. **uv** 包管理器
3. **ZHIPU_API_KEY** 环境变量

### 安装

```bash
# 通过 npx skills 安装（推荐）
npx skills add biiigwang/agent-skills-collection --skill glm-image-generation

# 或手动克隆安装
cd skills/glm-image-generation
uv sync
```

### 设置 API Key

```bash
export ZHIPU_API_KEY="your-api-key-here"
```

获取 API Key：https://open.bigmodel.cn/

### 基础使用

```bash
# 简单图像生成
uv run python glm-image-generation "一只可爱的小猫咪，坐在窗台上"

# 使用自定义模型
uv run python glm-image-generation "专业人像照" -m glm-image

# 使用自定义尺寸
uv run python glm-image-generation "风景画" -s 1344x768

# 高质量模式
uv run python glm-image-generation "精细插画" -q hd
```

## 📖 命令参考

```bash
uv run python glm-image-generation [OPTIONS] PROMPT

Arguments:
  PROMPT                    图像的文本描述

Options:
  -m, --model TEXT          使用的模型（默认：cogview-3-flash）
                            可选：cogview-3-flash, cogview-4, 
                                 cogview-4-250304, glm-image
  -s, --size TEXT           图像尺寸（默认：1024x1024）
                            cogview 系列：1024x1024, 768x1344, 1152x864 等
                            glm-image：1280x1280, 1568x1056 等
  -q, --quality TEXT        质量：standard 或 hd（默认：hd）
                            hd：更高质量，约 20 秒（仅 glm-image）
                            standard：快速生成，5-10 秒
  -o, --output TEXT         输出文件名
  --watermark               启用水印（默认：禁用）
  --user-id TEXT           终端用户 ID，用于合规（6-128 字符）
  --help                    显示帮助信息
```

## 🎯 支持模型

| 模型 | 描述 | 费用 | 生成时间 | 适用场景 |
|-------|-------------|------|----------|----------|
| `cogview-3-flash` | **默认** - 快速生成 | 低 | 5-10 秒 | 快速迭代、测试 |
| `cogview-4` | 高质量 | 付费 | 10-15 秒 | 专业输出 |
| `cogview-4-250304` | 最新版本 | 付费 | 10-15 秒 | 最佳质量 |
| `glm-image` | 最新模型（2025） | 付费 | ~20 秒 | HD 质量、精细图像 |

## 📐 尺寸选项

### cogview-3-flash, cogview-4, cogview-4-250304:

| 尺寸 | 宽高比 | 适用场景 |
|------|--------|----------|
| `1024x1024` | 1:1 | 通用（默认） |
| `768x1344` | 9:16 | 人像、手机竖屏 |
| `1152x864` | 4:3 | 风景 |
| `864x1152` | 3:4 | 人像 |
| `1344x768` | 16:9 | 风景、横幅 |
| `1440x720` | 2:1 | 超宽屏 |
| `720x1440` | 9:18 | 长竖屏 |

### glm-image:

| 尺寸 | 宽高比 | 适用场景 |
|------|--------|----------|
| `1280x1280` | 1:1 | 高分辨率正方形（默认） |
| `1568x1056` | 3:2 | 风景 |
| `1056x1568` | 2:3 | 人像 |
| `1472x1088` | 4:3 | 标准风景 |
| `1088x1472` | 3:4 | 标准人像 |
| `1728x960` | 16:9 | 宽风景 |
| `960x1728` | 9:16 | 长人像 |

## 💡 示例

### 简单图像生成
```bash
uv run python glm-image-generation "一只可爱的橘猫在阳光下打盹"
```

### 专业人像
```bash
uv run python glm-image-generation \
  "Professional business headshot, studio lighting" \
  -m glm-image \
  -q hd \
  -s 1280x1280
```

### 自定义尺寸风景
```bash
uv run python glm-image-generation \
  "未来科技城市夜景，高楼大厦，霓虹灯，赛博朋克风格" \
  -s 1344x768 \
  -m cogview-4
```

### 中国风
```bash
uv run python glm-image-generation \
  "中国风山水画，青山绿水，亭台楼阁，水墨画风格" \
  -s 1152x864
```

### 带用户 ID（合规）
```bash
uv run python glm-image-generation \
  "测试图片" \
  --user-id "user123456"
```

## 📁 输出

生成的图像保存到：
```
<项目根目录>/.glm_aigc/generated_<model>_<timestamp>.png
```

示例：
```
my-project/.glm_aigc/generated_cogview_3_flash_20260318_230000.png
```

## ⚠️ 故障排除

### API Key 未设置
```
✗ Error: ZHIPU_API_KEY environment variable not set

# 解决方案：
export ZHIPU_API_KEY="your-api-key-here"
```

### 模型尺寸不匹配
```
✗ API request failed: 400 Bad Request

# 解决方案：使用适合模型的尺寸
# cogview 系列：1024x1024, 768x1344 等
# glm-image：1280x1280, 1568x1056 等
```

### 付费模型警告
```
⚠️ Warning: Using premium model 'glm-image'. This may incur charges.
   Current default: cogview-3-flash (low cost)
   Continue? (y/n):
```

### 生成超时
```
✗ Generation timeout after 120s

# 解决方案：
# 1. 使用 standard 质量代替 hd
# 2. 使用较小的图像尺寸
# 3. 检查网络连接
```

### 请求频率限制
```
✗ API request failed: 429 Too Many Requests

# 解决方案：等待片刻后重试
```

## 🛠️ 开发

### 本地测试

1. 进入技能目录：
```bash
cd skills/glm-image-generation
```

2. 安装依赖：
```bash
uv sync
```

3. 使用 API Key 测试：
```bash
export ZHIPU_API_KEY="your-api-key"
uv run python glm-image-generation "test prompt"
```

### 运行测试

测试用例定义在 `evals/evals.json` 中。

## 📦 依赖

- **Python**: 3.10+
- **uv**: Python 包管理器
- **click**: CLI 界面
- **python-dotenv**: 环境管理
- **requests**: HTTP 客户端
- **pillow**: 图像处理

## 🔗 资源

- [GLM API 文档](https://open.bigmodel.cn/dev/api)
- [获取 API Key](https://open.bigmodel.cn/)
- [Skills.sh 文档](https://skills.sh/docs/cli)

## 📝 许可证

MIT License - 详见主仓库 [LICENSE](../../LICENSE) 文件。

## 🤝 贡献

欢迎贡献！请参阅主仓库的贡献指南。

## 📮 支持

- **问题反馈**: [创建 Issue](https://github.com/biiigwang/agent-skills-collection/issues)
- **作者**: [@biiigwang](https://github.com/biiigwang)

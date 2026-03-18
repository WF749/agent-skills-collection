# Agent Skills Collection

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![npx skills](https://img.shields.io/npm/v/skills.svg?style=flat-square)](https://www.npmjs.com/package/skills)

**English** | [简体中文](README.zh-CN.md)

一个精心策划的 AI Agent 技能集合，用于增强 Claude Code、Cursor、OpenCode 等 AI 编程助手。

## 📦 可用技能

| 技能 | 描述 | 安装命令 |
|-------|------|---------|
| [glm-image-generation](skills/glm-image-generation) | 使用 GLM 的文本生成图像模型（cogview-3-flash、cogview-4、glm-image）生成图像 | `npx skills add biiigwang/agent-skills-collection --skill glm-image-generation` |

## 🚀 快速开始

### 安装单个技能

```bash
# 安装到当前项目
npx skills add biiigwang/agent-skills-collection --skill glm-image-generation

# 全局安装（所有项目可用）
npx skills add biiigwang/agent-skills-collection --skill glm-image-generation -g

# 安装到指定的 Agent
npx skills add biiigwang/agent-skills-collection --skill glm-image-generation -a claude-code -a cursor
```

### 安装所有技能

```bash
# 安装所有技能到当前项目
npx skills add biiigwang/agent-skills-collection --all

# 全局安装所有技能
npx skills add biiigwang/agent-skills-collection --all -g
```

### 列出可用技能

```bash
# 列出仓库中的技能但不安装
npx skills add biiigwang/agent-skills-collection --list
```

## 📚 技能文档

每个技能都有详细的独立文档：

- **[glm-image-generation](skills/glm-image-generation/README.md)** - 使用 GLM 模型从文本提示生成图像

## 🔧 支持的 Agent

技能可以安装到以下 AI Agent：

- **Claude Code** (`claude-code`)
- **Cursor** (`cursor`)
- **OpenCode** (`opencode`)
- **GitHub Copilot** (`github-copilot`)
- **Codex** (`codex`)
- **Gemini CLI** (`gemini-cli`)
- **Windsurf** (`windsurf`)
- **Cline** (`cline`)
- 以及 [39+ 更多 Agent](https://skills.sh/docs/cli)

## 📁 项目结构

```
agent-skills-collection/
├── README.md                    # 本文件
├── README.zh-CN.md              # 中文版本
├── package.json                 # 包元数据
├── LICENSE                      # MIT 许可证
├── .gitignore                   # Git 忽略规则
├── AGENTS.md                    # AI Agent 指南
│
├── skills/                      # 技能目录
│   ├── glm-image-generation/    # GLM 图像生成技能
│   │   ├── SKILL.md             # 技能定义（必需）
│   │   ├── README.md            # 详细文档
│   │   ├── README.zh-CN.md      # 中文文档
│   │   ├── glm-image-generation.py
│   │   ├── pyproject.toml
│   │   └── evals/
│   └── [future-skills]/         # 未来技能
│
└── scripts/                     # 辅助脚本
    ├── validate.sh              # 验证技能格式
    └── install-deps.sh          # 安装依赖
```

## 🛠️ 开发

### 本地测试

1. 克隆仓库：
```bash
git clone https://github.com/biiigwang/agent-skills-collection.git
cd agent-skills-collection
```

2. 进入技能目录并安装依赖：
```bash
cd skills/glm-image-generation
uv sync
```

3. 测试技能：
```bash
export ZHIPU_API_KEY="your-api-key"
uv run python glm-image-generation "test prompt"
```

### 创建新技能

贡献新技能的步骤：

1. 在 `skills/` 下创建新目录
2. 添加带有 YAML frontmatter 的 `SKILL.md`（name + description）
3. 添加 `README.md` 详细文档
4. 本地测试技能
5. 更新根目录 `README.md` 将技能加入表格

### 验证技能

运行验证脚本检查所有技能：

```bash
./scripts/validate.sh
```

## 📝 许可证

本项目采用 MIT 许可证 - 详见 [LICENSE](LICENSE) 文件。

## 🔗 资源

- [Skills.sh 文档](https://skills.sh/docs/cli)
- [Skills.sh GitHub](https://github.com/vercel-labs/skills)
- [创建技能指南](https://resources.anthropic.com/hubfs/The-Complete-Guide-to-Building-Skill-for-Claude.pdf)

## 🤝 贡献

欢迎贡献！请随时提交 Pull Request。

1. Fork 仓库
2. 创建特性分支（`git checkout -b feature/AmazingSkill`）
3. 提交更改（`git commit -m 'Add some AmazingSkill'`）
4. 推送到分支（`git push origin feature/AmazingSkill`）
5. 打开 Pull Request

## 📮 联系

- **GitHub Issues**: [创建 Issue](https://github.com/biiigwang/agent-skills-collection/issues)
- **作者**: [@biiigwang](https://github.com/biiigwang)

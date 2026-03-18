# Agent Skills Collection

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![npx skills](https://img.shields.io/npm/v/skills.svg?style=flat-square)](https://www.npmjs.com/package/skills)

**English** | [简体中文](README.zh-CN.md)

A curated collection of AI agent skills for enhancing Claude Code, Cursor, OpenCode, and other AI coding assistants.

## 📦 Available Skills

| Skill | Description | Install Command |
|-------|-------------|-----------------|
| [glm-image-generation](skills/glm-image-generation) | Generate images using GLM's text-to-image models (cogview-3-flash, cogview-4, glm-image) | `npx skills add biiigwang/agent-skills-collection --skill glm-image-generation` |

## 🚀 Quick Start

### Install a Single Skill

```bash
# Install to your current project
npx skills add biiigwang/agent-skills-collection --skill glm-image-generation

# Install globally (available across all projects)
npx skills add biiigwang/agent-skills-collection --skill glm-image-generation -g

# Install to specific agents
npx skills add biiigwang/agent-skills-collection --skill glm-image-generation -a claude-code -a cursor
```

### Install All Skills

```bash
# Install all skills to current project
npx skills add biiigwang/agent-skills-collection --all

# Install all skills globally
npx skills add biiigwang/agent-skills-collection --all -g
```

### List Available Skills

```bash
# List skills in this repository without installing
npx skills add biiigwang/agent-skills-collection --list
```

## 📚 Skill Documentation

Each skill has its own detailed documentation:

- **[glm-image-generation](skills/glm-image-generation/README.md)** - Generate images from text prompts using GLM models

## 🔧 Supported Agents

Skills can be installed to any of these AI agents:

- **Claude Code** (`claude-code`)
- **Cursor** (`cursor`)
- **OpenCode** (`opencode`)
- **GitHub Copilot** (`github-copilot`)
- **Codex** (`codex`)
- **Gemini CLI** (`gemini-cli`)
- **Windsurf** (`windsurf`)
- **Cline** (`cline`)
- And [39+ more agents](https://skills.sh/docs/cli)

## 📁 Project Structure

```
agent-skills-collection/
├── README.md                    # This file
├── README.zh-CN.md              # Chinese version
├── package.json                 # Package metadata
├── LICENSE                      # MIT License
├── .gitignore                   # Git ignore rules
├── AGENTS.md                    # AI Agent guidelines
│
├── skills/                      # Skills directory
│   ├── glm-image-generation/    # GLM Image Generation skill
│   │   ├── SKILL.md             # Skill definition (required)
│   │   ├── README.md            # Detailed documentation
│   │   ├── README.zh-CN.md      # Chinese documentation
│   │   ├── glm-image-generation.py
│   │   ├── pyproject.toml
│   │   └── evals/
│   └── [future-skills]/         # Future skills
│
└── scripts/                     # Helper scripts
    ├── validate.sh              # Validate skill formats
    └── install-deps.sh          # Install dependencies
```

## 🛠️ Development

### Local Testing

1. Clone the repository:
```bash
git clone https://github.com/biiigwang/agent-skills-collection.git
cd agent-skills-collection
```

2. Navigate to a skill and install dependencies:
```bash
cd skills/glm-image-generation
uv sync
```

3. Test the skill:
```bash
export ZHIPU_API_KEY="your-api-key"
uv run python glm-image-generation "test prompt"
```

### Creating New Skills

To contribute a new skill:

1. Create a new directory under `skills/`
2. Add `SKILL.md` with YAML frontmatter (name + description)
3. Add `README.md` with detailed documentation
4. Test the skill locally
5. Update the root `README.md` to include your skill in the table

### Validating Skills

Run the validation script to check all skills:

```bash
./scripts/validate.sh
```

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🔗 Resources

- [Skills.sh Documentation](https://skills.sh/docs/cli)
- [Skills.sh GitHub](https://github.com/vercel-labs/skills)
- [Create Skills Guide](https://resources.anthropic.com/hubfs/The-Complete-Guide-to-Building-Skill-for-Claude.pdf)

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingSkill`)
3. Commit your changes (`git commit -m 'Add some AmazingSkill'`)
4. Push to the branch (`git push origin feature/AmazingSkill`)
5. Open a Pull Request

## 📮 Contact

- **GitHub Issues**: [Create an issue](https://github.com/biiigwang/agent-skills-collection/issues)
- **Author**: [@biiigwang](https://github.com/biiigwang)

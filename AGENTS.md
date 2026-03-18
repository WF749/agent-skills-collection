# AI Agent Guidelines

This file provides guidance for AI agents working with this repository.

## Repository Purpose

This repository contains a collection of AI agent skills that can be installed via the `npx skills` CLI tool. Each skill extends the capabilities of AI coding assistants like Claude Code, Cursor, OpenCode, and others.

## Working with Skills

### Skill Structure

Each skill in the `skills/` directory should have:

1. **SKILL.md** (required) - Skill definition with YAML frontmatter
   ```yaml
   ---
   name: skill-name
   description: Brief description of what the skill does
   ---
   ```

2. **README.md** - Detailed documentation for users
3. **Implementation files** - Scripts, code, etc.
4. **Dependencies** - `pyproject.toml`, `package.json`, etc.

### Adding a New Skill

When creating a new skill:

1. Create directory: `skills/<skill-name>/`
2. Add `SKILL.md` with name and description
3. Add `README.md` with usage instructions
4. Test locally before committing
5. Update root `README.md` to include the skill

### Skill Discovery

AI agents can discover available skills by:

1. Reading the root `README.md` skills table
2. Listing contents of `skills/` directory
3. Checking individual skill `SKILL.md` files

## Installation Commands

### Install Single Skill
```bash
npx skills add biiigwang/agent-skills-collection --skill <skill-name>
```

### Install All Skills
```bash
npx skills add biiigwang/agent-skills-collection --all
```

### Install Globally
```bash
npx skills add biiigwang/agent-skills-collection --skill <skill-name> -g
```

## Testing Skills

Before committing skill changes:

1. Navigate to skill directory
2. Install dependencies: `uv sync` or `npm install`
3. Run test commands from README
4. Verify expected outputs

## Repository Maintenance

### Validation

Run validation script to check all skills:
```bash
./scripts/validate.sh
```

### Dependencies

Keep dependencies up to date:
```bash
./scripts/install-deps.sh
```

## Best Practices

1. **Descriptive Names** - Use clear, descriptive skill names
2. **Complete Documentation** - Always include usage examples
3. **Test Before Commit** - Verify skills work locally
4. **Semantic Versioning** - Use git tags for releases
5. **License Compliance** - Respect all open source licenses

## Support

For issues or questions:
- Check individual skill READMEs
- Review skills.sh documentation: https://skills.sh/docs/cli
- Open GitHub issue: https://github.com/biiigwang/agent-skills-collection/issues

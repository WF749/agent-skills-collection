#!/bin/bash
# Install dependencies for all skills
# Uses uv for Python skills and npm for Node.js skills

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(dirname "$SCRIPT_DIR")"
SKILLS_DIR="$REPO_ROOT/skills"

echo "📦 Installing dependencies for all skills"
echo "========================================"

installed=0
skipped=0
errors=0

# Check each skill directory
for skill_dir in "$SKILLS_DIR"/*/; do
    if [ -d "$skill_dir" ]; then
        skill_name=$(basename "$skill_dir")
        echo ""
        echo "🔧 Installing: $skill_name"
        
        # Check for Python skill (pyproject.toml)
        if [ -f "$skill_dir/pyproject.toml" ]; then
            echo "  → Python skill detected (pyproject.toml)"
            
            if command -v uv &> /dev/null; then
                cd "$skill_dir"
                if uv sync; then
                    echo "  ✓ Dependencies installed with uv"
                    ((installed++))
                else
                    echo "  ✗ Failed to install dependencies"
                    ((errors++))
                fi
                cd "$REPO_ROOT"
            else
                echo "  ⚠ uv not found. Install with: curl -LsSf https://astral.sh/uv/install.sh | sh"
                ((skipped++))
            fi
        
        # Check for Node.js skill (package.json)
        elif [ -f "$skill_dir/package.json" ]; then
            echo "  → Node.js skill detected (package.json)"
            
            if command -v npm &> /dev/null; then
                cd "$skill_dir"
                if npm install; then
                    echo "  ✓ Dependencies installed with npm"
                    ((installed++))
                else
                    echo "  ✗ Failed to install dependencies"
                    ((errors++))
                fi
                cd "$REPO_ROOT"
            else
                echo "  ⚠ npm not found"
                ((skipped++))
            fi
        
        else
            echo "  ℹ No dependency file found, skipping"
            ((skipped++))
        fi
    fi
done

echo ""
echo "========================================"
echo "Installation Summary:"
echo "  Installed: $installed"
echo "  Skipped: $skipped"
echo "  Errors: $errors"
echo "========================================"

if [ $errors -gt 0 ]; then
    echo "❌ Installation completed with $errors error(s)"
    exit 1
else
    echo "✅ Installation completed successfully!"
    exit 0
fi

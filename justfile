# Default recipe to list all available commands
default:
    @just --list

# Keep this in sync with GitHub Actions workflows.
hugo_version := "0.140.2"

# Check and install all required dependencies
install:
    #!/usr/bin/env bash
    set -euo pipefail
    
    echo "Checking dependencies..."
    
    # Ensure ~/.local/bin exists
    mkdir -p ~/.local/bin
    
    # Hugo
    need_hugo=1
    if command -v hugo &> /dev/null; then
        if hugo version | grep -q "v{{hugo_version}}"; then
            echo "✓ hugo $(hugo version)"
            need_hugo=0
        else
            echo "✗ hugo wrong version ($(hugo version)); need v{{hugo_version}}"
        fi
    else
        echo "✗ hugo not found"
    fi

    if [ "$need_hugo" -eq 1 ]; then
        echo "Installing hugo v{{hugo_version}} (extended)..."
        curl -L "https://github.com/gohugoio/hugo/releases/download/v{{hugo_version}}/hugo_extended_{{hugo_version}}_linux-amd64.tar.gz" \
          | tar -xz -C ~/.local/bin hugo
        echo "✓ hugo installed: $(~/.local/bin/hugo version)"
    fi
    
    # uv
    if command -v uv &> /dev/null; then
        echo "✓ uv $(uv --version)"
    else
        echo "✗ uv not found, installing..."
        curl -LsSf https://astral.sh/uv/install.sh | sh
        echo "✓ uv installed"
    fi
    
    # Typst
    if command -v typst &> /dev/null; then
        echo "✓ typst $(typst --version)"
    else
        echo "✗ typst not found, installing..."
        curl -fsSL https://github.com/typst/typst/releases/latest/download/typst-x86_64-unknown-linux-musl.tar.xz | tar -xJ --strip-components=1 -C ~/.local/bin
        echo "✓ typst installed"
    fi
    
    
    echo ""
    echo "Syncing Python dependencies..."
    uv sync
    
    echo ""
    echo "All dependencies ready!"

# Check dependencies without installing
check:
    #!/usr/bin/env bash
    echo "Checking dependencies..."
    failed=0
    
    for cmd in hugo uv typst; do
        if command -v $cmd &> /dev/null; then
            echo "✓ $cmd"
        else
            echo "✗ $cmd not found"
            failed=1
        fi
    done
    
    if [ $failed -eq 1 ]; then
        echo ""
        echo "Run 'just install' to install missing dependencies"
        exit 1
    fi

# Install/sync Python dependencies with uv
sync:
    uv sync

# Convert all Jupyter notebooks to blog posts
convert:
    uv run python convert-notebooks.py

# Run Hugo development server
serve:
    hugo serve -D

# Build the site for production
build:
    hugo --minify

# Convert notebooks and then serve
dev: convert serve

# Convert notebooks and build for production
publish: convert build

# Clean generated files
clean:
    rm -rf public/
    rm -rf resources/_gen/

# Add a new Python dependency
add *PACKAGES:
    uv add {{ PACKAGES }}

# Remove a Python dependency
remove *PACKAGES:
    uv remove {{ PACKAGES }}

# Run arbitrary Python scripts with uv
run *ARGS:
    uv run {{ ARGS }}

# Create a new blog post (usage: just new "post-name")
new NAME:
    hugo new blog/{{ NAME }}/index.md

# Format Python code with ruff
fmt:
    uv run ruff format .

# Lint Python code with ruff
lint:
    uv run ruff check .

# Fix Python linting issues
fix:
    uv run ruff check --fix .

# Timestamp for resume build directory
timestamp := `date +%Y%m%d-%H%M`
resume_dir := "resume/build/" + timestamp

# Build resume as PDF using Typst
resume-pdf:
    mkdir -p {{resume_dir}}
    typst compile --root . resume/resume.typ {{resume_dir}}/evan-curtin-resume.pdf

# Build resume as DOCX (using python-docx for proper styling)
resume-docx:
    mkdir -p {{resume_dir}}
    uv run python resume/generate_docx.py {{resume_dir}}/evan-curtin-resume.docx

# Build both resume formats
resume: resume-pdf resume-docx
    @echo "Resume built in {{resume_dir}}/"

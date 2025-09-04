#!/usr/bin/env python3
"""
Script to validate that required context.md files exist within the project structure.
"""
import os
import sys

# Define directories where context.md is mandatory
# Adjust these paths relative to the script's expected run location (project root)
REQUIRED_CONTEXT_DIRS = [
    ".",
    "backend",
    "frontend",
    "ops",
    "docs",
    "adr",
    "templates",
    "tools",
    # Add specific app/module directories later as they are created
    # e.g., "backend/apps/accounts", "frontend/src/components/Dashboard"
]

def find_project_root(start_path):
    """Find the project root directory by looking for a known marker file/folder."""
    # Common markers for project root
    markers = ['.git', 'README.md']
    current_path = os.path.abspath(start_path)

    while True:
        if any(os.path.exists(os.path.join(current_path, marker)) for marker in markers):
            return current_path
        parent_path = os.path.dirname(current_path)
        if parent_path == current_path:  # Reached the filesystem root
            break
        current_path = parent_path

    raise FileNotFoundError("Could not find project root. No .git or README.md found.")

def validate_context_files(project_root):
    """Check for the existence of context.md in required directories."""
    missing_contexts = []
    template_path = os.path.join(project_root, "templates", "context.md")

    for dir_path in REQUIRED_CONTEXT_DIRS:
        full_path = os.path.join(project_root, dir_path)
        if os.path.isdir(full_path):
            context_file = os.path.join(full_path, "context.md")
            if not os.path.exists(context_file):
                # Check if it's the template itself
                if os.path.abspath(context_file) != os.path.abspath(template_path):
                    missing_contexts.append(dir_path)
        else:
            print(f"Warning: Required directory '{dir_path}' does not exist.")

    if missing_contexts:
        print("Error: The following directories are missing a 'context.md' file:")
        for dir_name in missing_contexts:
            print(f"  - {dir_name}")
        print("\nPlease create a 'context.md' file in each missing directory.")
        print("You can copy the template from 'templates/context.md'.")
        return False
    else:
        print("Success: All required 'context.md' files are present (or directories do not exist yet).")
        return True

if __name__ == "__main__":
    try:
        # Start searching from the script's directory
        script_dir = os.path.dirname(os.path.abspath(__file__))
        project_root = find_project_root(script_dir)

        print(f"Project root found at: {project_root}")
        is_valid = validate_context_files(project_root)

        if not is_valid:
            sys.exit(1) # Exit with error code to signal failure
        else:
            sys.exit(0) # Exit successfully

    except FileNotFoundError as e:
        print(f"Error: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)

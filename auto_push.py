import subprocess
import os
from datetime import datetime

# CHANGE THIS PATH IF NEEDED
PROJECT_PATH = r"F:\2DProject\ProjectFireRed"

def run_git_command(command):
    result = subprocess.run(
        command,
        cwd=PROJECT_PATH,
        shell=True,
        text=True,
        capture_output=True
    )
    if result.returncode != 0:
        print("❌ Error:", result.stderr)
        exit(1)
    return result.stdout

def main():
    print("🚀 Starting auto push to GitHub...")

    # Check git status
    status = run_git_command("git status --porcelain")
    if not status.strip():
        print("✅ No changes to commit.")
        return

    # Add all changes
    run_git_command("git add .")

    # Commit with timestamp
    commit_message = f"Auto update: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
    run_git_command(f'git commit -m "{commit_message}"')

    # Push to GitHub
    run_git_command("git push")

    print("✅ Successfully pushed to GitHub!")

if __name__ == "__main__":
    main()

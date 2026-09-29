"""Zip each skill for upload to claude.ai (Settings -> Capabilities -> Skills) and copy them to
.claude/skills/ for Claude Code."""

import shutil
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SKILLS = ROOT / "skills"
DIST = ROOT / "dist"


def main() -> None:
    DIST.mkdir(exist_ok=True)
    for skill_dir in sorted(p for p in SKILLS.iterdir() if (p / "SKILL.md").exists()):
        zip_path = DIST / f"{skill_dir.name}.zip"
        with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as zf:
            for file in skill_dir.rglob("*"):
                if file.is_file():
                    zf.write(file, Path(skill_dir.name) / file.relative_to(skill_dir))
        target = ROOT / ".claude" / "skills" / skill_dir.name
        shutil.rmtree(target, ignore_errors=True)
        shutil.copytree(skill_dir, target)
        print(f"{zip_path.relative_to(ROOT)}  +  {target.relative_to(ROOT)}")


if __name__ == "__main__":
    main()

# Publish Unfired on GitHub

Working repository name: `unfired`. Suggested description:

> Understand how it works. Build it open. A reverse-engineering and open-alternatives handbook with runnable labs, project templates, and worker support.

This checkout may be prepared before GitHub publication. Do not announce a URL until creation succeeds. Repo-name availability within your account and trademark clearance are separate questions; neither is assumed here.

## Verify locally

```bash
python3 -m unittest discover -s tests -v
python3 scripts/check_repo.py
git status --short
git diff --cached
```

Review staged files for personal data, credentials, former employer material, and unintended files. `.unfired/` and `output/` are private working directories, not demo content.

## Create the public repository

Requires Git, GitHub CLI (`gh`), and a working GitHub login. If `gh auth status` fails, run `gh auth login --hostname github.com` interactively on your machine. Never paste a token into chat or commit it.

From this project directory:

```bash
git init
git add README.md LICENSE .gitignore assets community docs examples handbook labs projects templates tools tests scripts .github CONTRIBUTING.md CODE_OF_CONDUCT.md SECURITY.md SUPPORT.md GOVERNANCE.md ROADMAP.md CHANGELOG.md
git diff --cached --stat
git diff --cached
git commit -m "Launch Unfired: open-source comeback kit"
gh repo create unfired --public --source=. --remote=origin --push --description "Understand how it works. Build it open. Reverse-engineering handbook, runnable labs, and open alternatives."
```

These are first-publication commands. If `origin` or the target repo already exists, inspect it before proceeding; do not delete a remote or force-push to work around a conflict. If `unfired` is unavailable under your account, choose `unfired-kit` and use that in creation and subsequent commands.

## Configure discovery and contribution

Use the actual name if you changed it:

```bash
gh repo edit --add-topic open-source --add-topic layoffs --add-topic career --add-topic reskilling --add-topic developer-tools --add-topic python
gh repo view --web
```

In repository Settings, enable Discussions if desired, enable private vulnerability reporting if available, and check Actions permissions. The included workflow runs checks with read-only repository permissions. Upload `assets/unfired-banner.svg` via a supported raster export if GitHub's social-preview uploader requires PNG/JPEG; the SVG works in the README itself.

## First release

After CI passes, create a `v0.1.0` release using [CHANGELOG.md](../CHANGELOG.md). Include the limitations and proposed-project status. Seed issues from [starter issues](../community/starter-issues.md) with `good first issue`, `help wanted`, `documentation`, and `project proposal` labels after creating those labels. Use [launch-kit.md](../community/launch-kit.md) for editable posts. Sharing text is prepared here; nothing is automatically posted to other services.

Viral reach cannot be engineered or promised. A clear demo, a useful first contribution, and respectful sharing give the project a stronger start than outrage, artificial stars, or mass promotion.

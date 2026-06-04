# Week 1 — Setting Up Your Tech Stack

**Dr. Dave Wanik · OPIM 5512**

This week is sometimes the hardest — be patient, debug carefully, and get this working. Everything else in the course depends on it.

---

## What you'll install

| Tool | Purpose |
|------|---------|
| Git | Version control |
| GitHub account | Cloud storage for your code |
| VS Code | Code editor |
| Python 3.11+ | The language |
| `venv` | Isolated environments per project |

---

## Step-by-step

### 1. Install Git
- Download from https://git-scm.com/downloads
- Accept default settings
- Confirm: open a terminal and run `git --version`

### 2. Make a GitHub account
- Go to https://github.com and sign up
- Use your UConn email, and your netID as your username

### 3. Connect Git to GitHub (first time only)
```bash
git config --global user.name "YourUsername"
git config --global user.email "you@uconn.edu"
```

### 4. Install VS Code
- Download from https://code.visualstudio.com
- Install these extensions: **Python**, **Pylance**, **Jupyter**, **GitLens**

### 5. Create your personal class repo on GitHub
- Go to https://github.com/new
- Name it `opim5512-<your-netid>` (e.g. `opim5512-dww05002`)
- Make it **private**
- Check "Initialize with README"

### 6. Clone it to your machine
```bash
cd $HOME\code\        # Windows (create this folder first if needed)
git clone https://github.com/YOUR_USERNAME/opim5512-<your-netid>.git
cd opim5512-<your-netid>
```

### 7. Make a virtual environment
```bash
python -m venv .venv
.venv\Scripts\activate      # Windows
# source .venv/bin/activate  # Mac/Linux
```

### 8. Your first commit
Edit the README.md — add "Hello World! My favorite color is ___"

```bash
git add README.md
git commit -m "first commit - hello world"
git push
```

Refresh your GitHub repo in the browser — you should see your change!

---

## Troubleshooting tips
- **`python` not found**: try `python3` or check that Python is in your PATH
- **`git push` asks for password**: use a Personal Access Token (GitHub → Settings → Developer Settings)
- **Mac users**: if you hit OS-specific bugs, ask classmates or use an LLM to debug — then reach out to Dr. Dave if truly stuck

# Data Versioning & DVC

## What is Data Versioning?

In ML projects, your model's output depends on 3 things — **code, parameters, and data**. Git handles code well, but **data files are too large** for Git (imagine pushing 10GB of images to GitHub — it breaks).

Data versioning means **tracking which version of your dataset was used to train which model**, so you can reproduce results later.

---

## What is DVC?

**DVC (Data Version Control)** is a tool that works alongside Git to version your data, models, and ML pipelines.

Think of it like this:

> Git tracks your **code**. DVC tracks your **data and models**.

---

## How it Works (Simple Idea)

Instead of storing the actual large file in Git, DVC stores a **small pointer file** (`.dvc` file) in Git that says _"the real data is stored over there (S3/Google Drive/etc.)"_.

**Example:**

- You have `data/train.csv` (500MB)
- DVC creates `data/train.csv.dvc` (tiny text file with a hash)
- You push `train.csv.dvc` to GitHub → DVC pushes the actual `train.csv` to S3/GDrive

---

## Real Working Example

Scenario: You're building a car damage detector.

You train on v1 dataset (1000 images).

Later you add 500 more images → v2 dataset.

You want to track both versions and know which model came from which data.

**Step-by-step:**

```bash
# 1. Initialize DVC in your project
git init
dvc init

# 2. Add your dataset to DVC (stops Git from tracking the big file)
dvc add data/images/

# 3. Commit the pointer file to Git
git add data/images.dvc .gitignore
git commit -m "Add dataset v1 - 1000 images"

# 4. Push actual data to remote storage (Google Drive / S3)
dvc remote add -d myremote gdrive://your-folder-id
dvc push

# --- Later, you add 500 more images ---

# 5. Re-add the updated folder
dvc add data/images/
git add data/images.dvc
git commit -m "Dataset v2 - added 500 augmented images"
dvc push

# 6. To go back to v1 data anytime:
git checkout <commit-hash-of-v1>
dvc pull   # DVC automatically fetches the v1 images
```

---

## What is a DVC Pipeline?

Instead of manually running `python preprocess.py` then `python train.py`, DVC lets you define a **pipeline** so it knows the order and re-runs only what changed.

```bash
# Example pipeline run
dvc repro   # runs all stages in order, skips unchanged ones
```

---

## Key Terms (Plain English)

| Term        | What it means                                                 |
| ----------- | ------------------------------------------------------------- |
| `.dvc file` | A small pointer file Git tracks instead of your big data file |
| `dvc push`  | Upload actual data to cloud storage                           |
| `dvc pull`  | Download data from cloud storage                              |
| `dvc repro` | Re-run your ML pipeline (only changed parts)                  |
| `cache`     | Local copy of your data so you don't re-download every time   |
| `remote`    | Where your actual data lives (S3, GDrive, Azure)              |

---

## Why Use DVC?

- ✅ Version your datasets like code
- ✅ Reproduce any past experiment with exact data used
- ✅ Share large datasets with teammates via cloud storage
- ✅ No more "which dataset did I use for that model?" confusion
- ✅ Works with any cloud (S3, GCS, Azure, Google Drive, SSH)

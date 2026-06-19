# Module 3 — Week 1: GitHub & the Cloud (GCP)

**OPIM 5512 · Dr. Dave Wanik · University of Connecticut**

---

## Why does this matter?

Your laptop sleeps, runs out of memory, and isn't always on. Real data pipelines aren't — they live in the cloud, run on a schedule or on demand, and don't depend on anyone's machine being awake. This week you take your project off your laptop and onto Google Cloud Platform.

This is exactly how data science runs in industry: code lives in a repo, executes in the cloud, and authenticates with service accounts instead of passwords pasted into a script. Getting the green check marks means your whole stack — repo, project, credentials, deployment — is wired up correctly.

---

## What you'll be able to do after this

- Explain why moving code to the cloud makes pipelines reliable and reproducible
- Create and configure a Google Cloud Platform project (billing, APIs, permissions)
- Deploy a cloud function and trigger it
- Test deployed functions and use logs to debug failures
- Authenticate with service accounts and keep credentials out of your code

---

## How to run it

This week is setup, not a script — follow the guide step by step:

1. Work through **`GCP_SETUP.md`** in this folder, top to bottom.
2. Open **`GCP_Setup_Guide_Students.ipynb`** for the annotated walkthrough.
3. Confirm the tooling is wired up:

```bash
gcloud auth login
gcloud config set project YOUR_PROJECT_ID
gcloud services enable cloudfunctions.googleapis.com
```

> **Never commit credentials.** Authenticate with a service account and keep keys in environment variables / a `.env` file (which is git-ignored).

See the slide deck in this folder (`M3_W1_GitHub_and_Cloud_GCP.pdf`) for the overview.

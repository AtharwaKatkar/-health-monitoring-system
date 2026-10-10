# Deploying to Render (Free Tier — Portfolio Link)

This guide gets your app live at a public URL like `https://health-monitoring-csi.onrender.com`.

---

## Step 1 — Install Git (if you haven't)

Download and install Git from: https://git-scm.com/download/win  
During install, keep all defaults. Then restart your terminal.

---

## Step 2 — Create a GitHub repo

1. Go to https://github.com and log in (or create a free account).
2. Click **New** (green button, top left).
3. Name it: `health-monitoring-csi`
4. Set it to **Public** (required for free Render tier).
5. Do NOT initialize with README. Click **Create repository**.
6. GitHub will show you the repo URL — copy it, e.g. `https://github.com/YourUsername/health-monitoring-csi.git`

---

## Step 3 — Push the code to GitHub

Open a terminal (PowerShell) in your project folder and run:

```powershell
cd "d:\wifi csi zip file\Non-Contact Multi-Modal Health Monitoring using Wi-Fi CSI"

git init
git add .
git commit -m "Initial deploy: Wi-Fi CSI health monitoring system"
git branch -M main
git remote add origin https://github.com/YourUsername/health-monitoring-csi.git
git push -u origin main
```

> Replace `YourUsername` with your actual GitHub username.

---

## Step 4 — Deploy on Render

1. Go to https://render.com and sign up (free, use GitHub to sign in).
2. Click **New +** → **Web Service**.
3. Click **Connect a repository** → select `health-monitoring-csi`.
4. Render will auto-detect the `render.yaml`. Leave all settings as-is.
5. Click **Create Web Service**.

Render will now:
- Install dependencies from `requirements-prod.txt`
- Start the app with Gunicorn
- Give you a URL like `https://health-monitoring-csi.onrender.com`

The first deploy takes ~5-10 minutes (PyTorch downloads). After that, it's live.

---

## Step 5 — Your portfolio URL

Once deployed, your URL is: `https://health-monitoring-csi.onrender.com`

Put this on your resume and GitHub profile.  
The app auto-seeds 5 demo patients with health metrics so it always looks great for reviewers.

---

## Notes

- **Free tier sleeps after 15 min of inactivity** — first visit after idle takes ~30 seconds to wake. This is normal for free hosting.
- **Data resets on redeploy** — SQLite is in-memory on Render's ephemeral disk. Demo data is re-seeded automatically on every start, so the app always looks good.
- **Upgrade path**: If you want persistent data, add a free PostgreSQL database on Render and set `DATABASE_URL` to the Postgres connection string. The app already reads `DATABASE_URL` from environment.

---

## Troubleshooting

- **Build fails on torch**: Make sure `requirements-prod.txt` is used (not `requirements.txt`). The `+cpu` variant is much smaller.
- **App crashes on start**: Check Render logs (Dashboard → your service → Logs tab).
- **500 errors**: Usually a missing env var. Render should auto-generate `SECRET_KEY` from `render.yaml`.

# Push to GitHub - Step by Step Guide

## Step 1: Create a GitHub Repository

1. Go to https://github.com and sign in
2. Click the **"+"** button (top right) → **"New repository"**
3. Fill in:
   - **Repository name:** `password-strength-checker`
   - **Description:** "A comprehensive password strength checker with PWA support"
   - **Public** or **Private** (your choice)
   - **DO NOT** check "Add a README file" (we already have one)
4. Click **"Create repository"**

## Step 2: Push Your Local Code

Run these commands in your terminal:

```bash
cd /Users/subbu/CascadeProjects/password-strength-checker
```

### 2a. Set your Git identity (first time only):
```bash
git config --global user.name "Your Name"
git config --global user.email "your-email@example.com"
```

### 2b. Add GitHub remote (if not already added):
```bash
git remote -v
```
If empty, add it:
```bash
git remote add origin https://github.com/YOUR_USERNAME/password-strength-checker.git
```

### 2c. Push to GitHub:
```bash
git branch -M main
git push -u origin main
```

### 2d. Enter your GitHub credentials when prompted:
- **Username:** your GitHub username
- **Password:** your GitHub password (or Personal Access Token)

> ⚠️ If you have 2FA enabled, use a Personal Access Token instead of password:
> - Go to GitHub → Settings → Developer settings → Personal access tokens → Generate new token
> - Copy the token and use it as your password

## Step 3: Verify Upload

1. Go to https://github.com/YOUR_USERNAME/password-strength-checker
2. You should see all your files there

## Step 4: Deploy to Render

Now that your code is on GitHub:

1. Go to https://render.com
2. Sign up with GitHub
3. Connect your `password-strength-checker` repository
4. Deploy backend and frontend following DEPLOYMENT_GUIDE.md

## Troubleshooting

**"Permission denied" error?**
- Check your GitHub username and password/token
- Make sure repository name is correct

**"Updates were rejected"?**
- Run: `git pull origin main --rebase` then `git push origin main`

**Empty repository on GitHub?**
- Refresh the page, it may take a moment to update


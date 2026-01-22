#!/bin/bash

echo "🚀 Password Strength Checker - Quick Deploy Script"
echo "=================================================="
echo ""
echo "This script will help you deploy your app to Render.com for 24/7 access"
echo ""

# Check if git is initialized
if [ ! -d ".git" ]; then
    echo "📦 Initializing Git repository..."
    git init
    git add .
    git commit -m "Initial commit - Password Strength Checker"
fi

echo ""
echo "📋 Deployment Steps:"
echo ""
echo "1. Go to https://render.com and sign up with GitHub"
echo ""
echo "2. Deploy Backend:"
echo "   - Click 'New +' → 'Web Service'"
echo "   - Connect this repository"
echo "   - Root Directory: 'backend'"
echo "   - Build Command: 'pip install -r requirements.txt'"
echo "   - Start Command: 'gunicorn app:app'"
echo "   - Copy your backend URL (e.g., https://your-api.onrender.com)"
echo ""
echo "3. Update API URL in frontend:"
echo "   - Edit: frontend/src/App.jsx"
echo "   - Change 'http://localhost:5000' to your Render backend URL"
echo ""
echo "4. Deploy Frontend:"
echo "   - Click 'New +' → 'Static Site'"
echo "   - Connect same repository"
echo "   - Root Directory: 'frontend'"
echo "   - Build Command: 'npm install && npm run build'"
echo "   - Publish Directory: 'dist'"
echo ""
echo "5. Install on iPhone:"
echo "   - Open https://your-frontend.onrender.com in Safari"
echo "   - Tap Share button → 'Add to Home Screen'"
echo ""
echo "✅ Your app will be accessible 24/7 from anywhere!"
echo ""

# Commit any changes
git add -A 2>/dev/null
git commit -m "Prepare for deployment" 2>/dev/null

echo "📝 Git commit created. Ready to push to GitHub!"
echo ""
echo "To push to GitHub:"
echo "   git remote add origin https://github.com/YOUR_USERNAME/password-strength-checker.git"
echo "   git push -u origin main"
echo ""
echo "Then connect your GitHub repo to Render.com"


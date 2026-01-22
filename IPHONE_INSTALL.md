# 📱 Install on iPhone - Quick Guide

## Step 1: Start the Servers

**Terminal 1 - Backend:**
```bash
cd /Users/subbu/CascadeProjects/password-strength-checker/backend
python3 app.py
```

**Terminal 2 - Frontend:**
```bash
cd /Users/subbu/CascadeProjects/password-strength-checker/frontend
npm run dev
```

## Step 2: Find Your Computer's IP Address

Run this command:
```bash
ifconfig | grep "inet " | grep -v 127.0.0.1
```

Or on Mac:
```bash
ipconfig getifaddr en0
```

You'll get something like: `192.168.0.101`

## Step 3: Access from iPhone

1. **Make sure your iPhone is on the same WiFi** as your computer
2. **Open Safari** on your iPhone (must use Safari, not Chrome)
3. **Go to:** `http://YOUR_IP_ADDRESS:3000`
   - Example: `http://192.168.0.101:3000`

## Step 4: Install the App

### Method A: Add to Home Screen (iOS Native)

1. Tap the **Share button** (square with arrow) at the bottom of Safari
2. Scroll down and tap **"Add to Home Screen"**
3. Edit the name to "PassCheck" or keep "Password Strength Checker"
4. Tap **"Add"** in the top right
5. The app icon will appear on your home screen! 🎉

### Method B: Using Install Banner (if shown)

1. Look for the purple banner at the top of the page
2. Tap **"Install"** button
3. Follow the prompts

## Step 5: Use the App

1. **Tap the icon** on your home screen
2. App opens in **full screen** (no browser UI)
3. Works **offline** after first load
4. Feels like a **native app**!

## 🎨 Customize Icons (Optional)

The app uses placeholder icons. To add custom icons:

1. **Open in browser:** `file:///Users/subbu/CascadeProjects/password-strength-checker/frontend/generate-icons.html`
2. Click **"Generate Icons"**
3. Download both icons (192x192 and 512x512)
4. Replace files in `frontend/public/` folder
5. Restart the dev server

Or create your own icons:
- Size: 192x192px and 512x512px
- Format: PNG
- Theme: Shield/Lock for security
- Save as: `icon-192.png` and `icon-512.png`

## 🔧 Troubleshooting

### Can't Access from iPhone?

**Check WiFi:**
```bash
# Make sure both devices are on same network
```

**Check Firewall:**
```bash
# Mac: System Preferences > Security & Privacy > Firewall
# Allow incoming connections for Node
```

**Try Different Port:**
```bash
# If 3000 is blocked, edit vite.config.js:
# Change port: 3000 to port: 8080
```

### Backend API Not Working?

The app has **offline fallback** - it will work without the backend, but with limited features:
- ✅ Basic password checking
- ✅ Character type validation
- ❌ Common password detection
- ❌ Advanced pattern detection
- ❌ Accurate crack time estimation

To fix:
1. Make sure backend is running
2. Update API URL in `frontend/src/App.jsx` line 28:
   ```javascript
   const response = await fetch('http://YOUR_IP:5000/api/check-password', {
   ```

### Install Option Not Showing?

- **iOS requires Safari** - Chrome/Firefox won't work
- Use **"Add to Home Screen"** method instead
- The install banner is for Android/Desktop only

### App Not Loading Offline?

- Service worker needs first successful load
- Try opening once with internet
- Check for errors in Safari's Web Inspector

## 🚀 Deploy to Production (Optional)

For permanent access without local server:

### Free Hosting Options:

**Frontend (Vercel):**
```bash
cd frontend
npm run build
npx vercel deploy
```

**Backend (Railway):**
1. Go to [railway.app](https://railway.app)
2. Connect GitHub repo
3. Deploy backend folder
4. Get production URL

**Update API URL:**
```javascript
// In frontend/src/App.jsx
const API_URL = 'https://your-backend.railway.app';
```

## 📊 Test PWA Score

1. Open Chrome DevTools (on desktop)
2. Go to **Lighthouse** tab
3. Select **Progressive Web App**
4. Click **Generate report**
5. Aim for 90+ score!

## ✅ Success Checklist

- [ ] Backend running on port 5000
- [ ] Frontend running on port 3000
- [ ] iPhone on same WiFi
- [ ] Can access app in Safari
- [ ] Added to home screen
- [ ] App opens full screen
- [ ] Password checking works
- [ ] Icons look good

## 🎉 You're Done!

Your Password Strength Checker is now a mobile app on your iPhone!

**Features:**
- 🏠 Home screen icon
- 📱 Full screen experience
- ⚡ Fast loading
- 🔒 Works offline
- 🎨 Native feel

Share the URL with friends to let them install it too!

---

**Need help?** Check [PWA_SETUP.md](PWA_SETUP.md) for detailed documentation.

# 🔒 Password Strength Checker

A comprehensive cybersecurity project that analyzes password strength in real-time with a beautiful modern UI.

## Features

### 🛡️ Security Analysis
- **Multi-factor scoring system** (0-100 scale)
- **8 security checks**:
  - Minimum length requirement
  - Uppercase letters
  - Lowercase letters
  - Numbers
  - Special characters
  - Common password detection
  - Sequential character detection
  - Repeated character detection

### ⏱️ Crack Time Estimation
- Estimates time required to crack password
- Based on character space and length
- Accounts for modern hardware capabilities

### 🎨 Modern UI
- Real-time password analysis
- Visual strength indicator with color coding
- Detailed security requirement checklist
- Actionable recommendations
- Responsive design
- Beautiful gradient background

### 🔧 Technical Stack
- **Backend**: Python with Flask
- **Frontend**: React with Vite
- **Styling**: TailwindCSS
- **Icons**: Lucide React

## Installation & Setup

### Prerequisites
- Python 3.8+
- Node.js 16+
- npm or yarn

### Backend Setup

1. Navigate to backend directory:
```bash
cd backend
```

2. Install Python dependencies:
```bash
pip install -r requirements.txt
```

3. Run the Flask server:
```bash
python app.py
```

The API will be available at `http://localhost:5000`

### Frontend Setup

1. Navigate to frontend directory:
```bash
cd frontend
```

2. Install dependencies:
```bash
npm install
```

3. Start the development server:
```bash
npm run dev
```

The app will open at `http://localhost:3000`

## Usage

### Web Interface
1. Start both backend and frontend servers
2. Open browser to `http://localhost:3000`
3. Type password in the input field
4. View real-time analysis and recommendations

### CLI Interface
Run the password checker directly from command line:
```bash
cd backend
python password_checker.py
```

### API Endpoint

**POST** `/api/check-password`

Request:
```json
{
  "password": "YourPassword123!"
}
```

Response:
```json
{
  "score": 85,
  "strength": "Very Strong",
  "feedback": ["✓ Excellent password! Keep it secure and unique."],
  "checks": {
    "length": true,
    "uppercase": true,
    "lowercase": true,
    "numbers": true,
    "special_chars": true,
    "no_common": true,
    "no_sequential": true,
    "no_repeated": true
  },
  "estimated_crack_time": "Centuries+"
}
```

## Security Features

1. **Common Password Detection**: Checks against 50+ most common passwords
2. **Pattern Detection**: Identifies sequential (abc, 123) and repeated (aaa) characters
3. **Character Diversity**: Ensures mix of uppercase, lowercase, numbers, and special characters
4. **Length Validation**: Recommends 12+ characters for optimal security
5. **Crack Time Calculation**: Realistic estimates based on modern hardware

## Project Structure

```
password-strength-checker/
├── backend/
│   ├── app.py                 # Flask API server
│   ├── password_checker.py    # Core password analysis logic
│   └── requirements.txt       # Python dependencies
├── frontend/
│   ├── src/
│   │   ├── App.jsx           # Main React component
│   │   ├── App.css           # Styles
│   │   └── main.jsx          # Entry point
│   ├── index.html
│   ├── package.json
│   ├── vite.config.js
│   ├── tailwind.config.js
│   └── postcss.config.js
└── README.md
```

## Educational Value

This project demonstrates:
- Password security best practices
- Real-time form validation
- RESTful API design
- Modern React patterns
- Responsive UI/UX design
- Client-server architecture

## License

MIT License - Feel free to use for educational purposes

## Contributing

Contributions welcome! Feel free to submit issues or pull requests.

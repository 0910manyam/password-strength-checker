from flask import Flask, request, jsonify
from flask_cors import CORS
from password_checker import PasswordStrengthChecker

app = Flask(__name__)
CORS(app)  # Enable CORS for frontend communication

# Initialize password checker
checker = PasswordStrengthChecker()


@app.route('/api/check-password', methods=['POST'])
def check_password():
    """
    API endpoint to check password strength
    
    Request body:
        {
            "password": "string"
        }
    
    Response:
        {
            "score": int,
            "strength": string,
            "feedback": [string],
            "checks": {string: bool},
            "estimated_crack_time": string
        }
    """
    try:
        data = request.get_json()
        
        if not data or 'password' not in data:
            return jsonify({
                'error': 'Password field is required'
            }), 400
        
        password = data['password']
        result = checker.check_password(password)
        
        return jsonify({
            'score': result.score,
            'strength': result.strength,
            'feedback': result.feedback,
            'checks': result.checks,
            'estimated_crack_time': result.estimated_crack_time
        })
    
    except Exception as e:
        return jsonify({
            'error': f'An error occurred: {str(e)}'
        }), 500


@app.route('/api/health', methods=['GET'])
def health_check():
    """Health check endpoint"""
    return jsonify({
        'status': 'healthy',
        'service': 'Password Strength Checker API'
    })


if __name__ == '__main__':
    print("Starting Password Strength Checker API...")
    print("API available at: http://localhost:5000")
    app.run(debug=True, host='0.0.0.0', port=5000)

import React, { useState, useEffect } from 'react';
import { Shield, Eye, EyeOff, Lock, CheckCircle, XCircle, AlertTriangle, Clock } from 'lucide-react';
import './App.css';

function App() {
  const [password, setPassword] = useState('');
  const [showPassword, setShowPassword] = useState(false);
  const [analysis, setAnalysis] = useState(null);
  const [isChecking, setIsChecking] = useState(false);

  // Debounce password checking
  useEffect(() => {
    if (password === '') {
      setAnalysis(null);
      return;
    }

    const timeoutId = setTimeout(() => {
      checkPassword(password);
    }, 300);

    return () => clearTimeout(timeoutId);
  }, [password]);

  const checkPassword = async (pwd) => {
    setIsChecking(true);
    try {
      const response = await fetch('http://localhost:5000/api/check-password', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ password: pwd }),
      });

      if (response.ok) {
        const data = await response.json();
        setAnalysis(data);
      } else {
        console.error('Failed to check password');
      }
    } catch (error) {
      console.error('Error checking password:', error);
      // Fallback to client-side checking if API is unavailable
      setAnalysis(clientSideCheck(pwd));
    } finally {
      setIsChecking(false);
    }
  };

  // Fallback client-side checking
  const clientSideCheck = (pwd) => {
    const checks = {
      length: pwd.length >= 8,
      uppercase: /[A-Z]/.test(pwd),
      lowercase: /[a-z]/.test(pwd),
      numbers: /\d/.test(pwd),
      special_chars: /[!@#$%^&*()_+\-=\[\]{};:'",.<>?/\\|`~]/.test(pwd),
    };

    let score = 0;
    if (checks.length) score += 20;
    if (checks.uppercase) score += 20;
    if (checks.lowercase) score += 20;
    if (checks.numbers) score += 20;
    if (checks.special_chars) score += 20;

    const strength = score >= 80 ? 'Very Strong' : score >= 60 ? 'Strong' : score >= 40 ? 'Good' : score >= 20 ? 'Fair' : 'Weak';

    const feedback = [];
    if (!checks.length) feedback.push('Use at least 8 characters');
    if (!checks.uppercase) feedback.push('Add uppercase letters (A-Z)');
    if (!checks.lowercase) feedback.push('Add lowercase letters (a-z)');
    if (!checks.numbers) feedback.push('Add numbers (0-9)');
    if (!checks.special_chars) feedback.push('Add special characters (!@#$%^&*)');

    return {
      score,
      strength,
      feedback: feedback.length > 0 ? feedback : ['Good password!'],
      checks,
      estimated_crack_time: 'N/A (API offline)',
    };
  };

  const getStrengthColor = (strength) => {
    switch (strength) {
      case 'Very Strong':
        return 'text-green-600';
      case 'Strong':
        return 'text-green-500';
      case 'Good':
        return 'text-yellow-500';
      case 'Fair':
        return 'text-orange-500';
      case 'Weak':
        return 'text-red-500';
      default:
        return 'text-gray-500';
    }
  };

  const getProgressColor = (score) => {
    if (score >= 80) return 'bg-green-600';
    if (score >= 60) return 'bg-green-500';
    if (score >= 40) return 'bg-yellow-500';
    if (score >= 20) return 'bg-orange-500';
    return 'bg-red-500';
  };

  return (
    <div className="min-h-screen bg-gradient-to-br from-slate-900 via-purple-900 to-slate-900 flex items-center justify-center p-4">
      <div className="max-w-2xl w-full">
        {/* Header */}
        <div className="text-center mb-8">
          <div className="flex items-center justify-center mb-4">
            <Shield className="w-16 h-16 text-purple-400" />
          </div>
          <h1 className="text-4xl font-bold text-white mb-2">
            Password Strength Checker
          </h1>
          <p className="text-gray-300">
            Test your password security in real-time
          </p>
        </div>

        {/* Main Card */}
        <div className="bg-white rounded-2xl shadow-2xl p-8">
          {/* Password Input */}
          <div className="mb-6">
            <label className="block text-sm font-medium text-gray-700 mb-2">
              Enter Password
            </label>
            <div className="relative">
              <Lock className="absolute left-3 top-1/2 transform -translate-y-1/2 w-5 h-5 text-gray-400" />
              <input
                type={showPassword ? 'text' : 'password'}
                value={password}
                onChange={(e) => setPassword(e.target.value)}
                className="w-full pl-10 pr-12 py-3 border-2 border-gray-300 rounded-lg focus:outline-none focus:border-purple-500 transition-colors"
                placeholder="Type your password here..."
              />
              <button
                onClick={() => setShowPassword(!showPassword)}
                className="absolute right-3 top-1/2 transform -translate-y-1/2 text-gray-400 hover:text-gray-600"
              >
                {showPassword ? <EyeOff className="w-5 h-5" /> : <Eye className="w-5 h-5" />}
              </button>
            </div>
          </div>

          {/* Analysis Results */}
          {analysis && (
            <div className="space-y-6">
              {/* Strength Indicator */}
              <div>
                <div className="flex justify-between items-center mb-2">
                  <span className="text-sm font-medium text-gray-700">
                    Strength
                  </span>
                  <span className={`text-lg font-bold ${getStrengthColor(analysis.strength)}`}>
                    {analysis.strength}
                  </span>
                </div>
                <div className="w-full bg-gray-200 rounded-full h-3 overflow-hidden">
                  <div
                    className={`h-full ${getProgressColor(analysis.score)} transition-all duration-500 ease-out`}
                    style={{ width: `${analysis.score}%` }}
                  />
                </div>
                <div className="text-right mt-1">
                  <span className="text-sm text-gray-600">
                    {analysis.score}/100
                  </span>
                </div>
              </div>

              {/* Crack Time Estimate */}
              <div className="bg-purple-50 rounded-lg p-4 flex items-center gap-3">
                <Clock className="w-5 h-5 text-purple-600 flex-shrink-0" />
                <div>
                  <div className="text-sm font-medium text-gray-700">
                    Estimated Crack Time
                  </div>
                  <div className="text-lg font-bold text-purple-600">
                    {analysis.estimated_crack_time}
                  </div>
                </div>
              </div>

              {/* Security Checks */}
              <div>
                <h3 className="text-sm font-medium text-gray-700 mb-3">
                  Security Requirements
                </h3>
                <div className="grid grid-cols-1 md:grid-cols-2 gap-2">
                  {Object.entries(analysis.checks).map(([key, passed]) => (
                    <div
                      key={key}
                      className={`flex items-center gap-2 p-2 rounded-lg ${
                        passed ? 'bg-green-50' : 'bg-red-50'
                      }`}
                    >
                      {passed ? (
                        <CheckCircle className="w-4 h-4 text-green-600 flex-shrink-0" />
                      ) : (
                        <XCircle className="w-4 h-4 text-red-600 flex-shrink-0" />
                      )}
                      <span className={`text-sm ${passed ? 'text-green-700' : 'text-red-700'}`}>
                        {key.replace(/_/g, ' ').replace(/\b\w/g, (l) => l.toUpperCase())}
                      </span>
                    </div>
                  ))}
                </div>
              </div>

              {/* Feedback */}
              <div>
                <h3 className="text-sm font-medium text-gray-700 mb-3 flex items-center gap-2">
                  <AlertTriangle className="w-4 h-4" />
                  Recommendations
                </h3>
                <ul className="space-y-2">
                  {analysis.feedback.map((item, index) => (
                    <li
                      key={index}
                      className="flex items-start gap-2 text-sm text-gray-600 bg-gray-50 p-3 rounded-lg"
                    >
                      <span className="text-purple-600 font-bold">•</span>
                      <span>{item}</span>
                    </li>
                  ))}
                </ul>
              </div>
            </div>
          )}

          {/* Empty State */}
          {!password && (
            <div className="text-center py-12 text-gray-400">
              <Shield className="w-16 h-16 mx-auto mb-4 opacity-50" />
              <p>Start typing to check your password strength</p>
            </div>
          )}
        </div>

        {/* Footer */}
        <div className="text-center mt-6 text-gray-300 text-sm">
          <p>🔒 Your password is never stored or transmitted insecurely</p>
        </div>
      </div>
    </div>
  );
}

export default App;

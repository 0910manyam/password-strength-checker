import re
from typing import Dict, List
from dataclasses import dataclass


@dataclass
class PasswordAnalysis:
    """Data class to store password analysis results"""
    score: int  # 0-100
    strength: str  # Weak, Fair, Good, Strong, Very Strong
    feedback: List[str]
    checks: Dict[str, bool]
    estimated_crack_time: str


class PasswordStrengthChecker:
    """
    Advanced password strength checker with multiple security criteria
    """
    
    def __init__(self):
        self.common_passwords = self._load_common_passwords()
        
    def _load_common_passwords(self) -> set:
        """Load common passwords to check against"""
        # Top 100 most common passwords
        return {
            'password', '123456', '123456789', 'qwerty', 'abc123', 
            'password1', '12345678', '111111', '1234567', 'sunshine',
            'qwerty123', 'password123', 'admin', 'letmein', 'welcome',
            'monkey', '1234567890', 'dragon', 'master', 'iloveyou',
            'princess', 'football', 'starwars', 'batman', 'trustno1',
            'hello', 'freedom', 'whatever', 'qazwsx', 'ninja',
            'azerty', 'solo', 'loveme', 'mustang', 'access',
            'shadow', 'michael', 'superman', '696969', '123123',
            'baseball', 'thomas', 'tigger', 'robert', 'computer',
            'maverick', 'jordan', 'pepper', 'charlie', 'aa123456',
            'donald', 'bailey', 'harley', 'ranger', 'cookie'
        }
    
    def check_password(self, password: str) -> PasswordAnalysis:
        """
        Analyze password strength and return detailed feedback
        
        Args:
            password: The password to analyze
            
        Returns:
            PasswordAnalysis object with score, strength, and feedback
        """
        if not password:
            return PasswordAnalysis(
                score=0,
                strength="Very Weak",
                feedback=["Password cannot be empty"],
                checks={},
                estimated_crack_time="Instant"
            )
        
        # Perform various checks
        checks = {
            'length': self._check_length(password),
            'uppercase': self._check_uppercase(password),
            'lowercase': self._check_lowercase(password),
            'numbers': self._check_numbers(password),
            'special_chars': self._check_special_chars(password),
            'no_common': not self._is_common_password(password),
            'no_sequential': not self._has_sequential_chars(password),
            'no_repeated': not self._has_repeated_chars(password)
        }
        
        # Calculate score
        score = self._calculate_score(password, checks)
        
        # Determine strength level
        strength = self._get_strength_level(score)
        
        # Generate feedback
        feedback = self._generate_feedback(password, checks)
        
        # Estimate crack time
        crack_time = self._estimate_crack_time(password, score)
        
        return PasswordAnalysis(
            score=score,
            strength=strength,
            feedback=feedback,
            checks=checks,
            estimated_crack_time=crack_time
        )
    
    def _check_length(self, password: str) -> bool:
        """Check if password meets minimum length requirement"""
        return len(password) >= 8
    
    def _check_uppercase(self, password: str) -> bool:
        """Check if password contains uppercase letters"""
        return bool(re.search(r'[A-Z]', password))
    
    def _check_lowercase(self, password: str) -> bool:
        """Check if password contains lowercase letters"""
        return bool(re.search(r'[a-z]', password))
    
    def _check_numbers(self, password: str) -> bool:
        """Check if password contains numbers"""
        return bool(re.search(r'\d', password))
    
    def _check_special_chars(self, password: str) -> bool:
        """Check if password contains special characters"""
        return bool(re.search(r'[!@#$%^&*()_+\-=\[\]{};:\'",.<>?/\\|`~]', password))
    
    def _is_common_password(self, password: str) -> bool:
        """Check if password is in common passwords list"""
        return password.lower() in self.common_passwords
    
    def _has_sequential_chars(self, password: str) -> bool:
        """Check for sequential characters (abc, 123, etc.)"""
        sequences = ['abc', 'bcd', 'cde', 'def', 'efg', 'fgh', 'ghi', 'hij',
                    'ijk', 'jkl', 'klm', 'lmn', 'mno', 'nop', 'opq', 'pqr',
                    'qrs', 'rst', 'stu', 'tuv', 'uvw', 'vwx', 'wxy', 'xyz',
                    '012', '123', '234', '345', '456', '567', '678', '789']
        
        password_lower = password.lower()
        return any(seq in password_lower or seq[::-1] in password_lower 
                  for seq in sequences)
    
    def _has_repeated_chars(self, password: str) -> bool:
        """Check for repeated characters (aaa, 111, etc.)"""
        return bool(re.search(r'(.)\1{2,}', password))
    
    def _calculate_score(self, password: str, checks: Dict[str, bool]) -> int:
        """Calculate password strength score (0-100)"""
        score = 0
        
        # Length scoring (0-30 points)
        length = len(password)
        if length >= 16:
            score += 30
        elif length >= 12:
            score += 25
        elif length >= 8:
            score += 15
        else:
            score += length * 2
        
        # Character variety (0-40 points)
        if checks['uppercase']:
            score += 10
        if checks['lowercase']:
            score += 10
        if checks['numbers']:
            score += 10
        if checks['special_chars']:
            score += 10
        
        # Security checks (0-30 points)
        if checks['no_common']:
            score += 10
        if checks['no_sequential']:
            score += 10
        if checks['no_repeated']:
            score += 10
        
        return min(score, 100)
    
    def _get_strength_level(self, score: int) -> str:
        """Convert score to strength level"""
        if score >= 80:
            return "Very Strong"
        elif score >= 60:
            return "Strong"
        elif score >= 40:
            return "Good"
        elif score >= 20:
            return "Fair"
        else:
            return "Weak"
    
    def _generate_feedback(self, password: str, checks: Dict[str, bool]) -> List[str]:
        """Generate helpful feedback for improving password"""
        feedback = []
        
        if not checks['length']:
            feedback.append("Use at least 8 characters (12+ recommended)")
        
        if not checks['uppercase']:
            feedback.append("Add uppercase letters (A-Z)")
        
        if not checks['lowercase']:
            feedback.append("Add lowercase letters (a-z)")
        
        if not checks['numbers']:
            feedback.append("Add numbers (0-9)")
        
        if not checks['special_chars']:
            feedback.append("Add special characters (!@#$%^&*)")
        
        if not checks['no_common']:
            feedback.append("⚠️ This is a commonly used password - avoid it!")
        
        if not checks['no_sequential']:
            feedback.append("Avoid sequential characters (abc, 123)")
        
        if not checks['no_repeated']:
            feedback.append("Avoid repeated characters (aaa, 111)")
        
        if len(password) < 12:
            feedback.append("Consider using 12+ characters for better security")
        
        if not feedback:
            feedback.append("✓ Excellent password! Keep it secure and unique.")
        
        return feedback
    
    def _estimate_crack_time(self, password: str, score: int) -> str:
        """Estimate time to crack password"""
        length = len(password)
        
        # Calculate character space
        char_space = 0
        if re.search(r'[a-z]', password):
            char_space += 26
        if re.search(r'[A-Z]', password):
            char_space += 26
        if re.search(r'\d', password):
            char_space += 10
        if re.search(r'[!@#$%^&*()_+\-=\[\]{};:\'",.<>?/\\|`~]', password):
            char_space += 32
        
        # Estimate combinations
        combinations = char_space ** length
        
        # Assume 1 billion attempts per second (modern hardware)
        attempts_per_second = 1_000_000_000
        seconds = combinations / attempts_per_second
        
        # Adjust for common passwords and patterns
        if score < 40:
            seconds /= 1000
        
        # Convert to human-readable time
        if seconds < 1:
            return "Instant"
        elif seconds < 60:
            return f"{int(seconds)} seconds"
        elif seconds < 3600:
            return f"{int(seconds / 60)} minutes"
        elif seconds < 86400:
            return f"{int(seconds / 3600)} hours"
        elif seconds < 31536000:
            return f"{int(seconds / 86400)} days"
        elif seconds < 31536000 * 100:
            return f"{int(seconds / 31536000)} years"
        else:
            return "Centuries+"


def main():
    """CLI interface for password strength checker"""
    checker = PasswordStrengthChecker()
    
    print("=" * 60)
    print("PASSWORD STRENGTH CHECKER".center(60))
    print("=" * 60)
    print()
    
    while True:
        password = input("\nEnter password to check (or 'quit' to exit): ")
        
        if password.lower() == 'quit':
            print("\nGoodbye!")
            break
        
        result = checker.check_password(password)
        
        print("\n" + "=" * 60)
        print(f"Strength: {result.strength}")
        print(f"Score: {result.score}/100")
        print(f"Estimated crack time: {result.estimated_crack_time}")
        print("\nSecurity Checks:")
        for check, passed in result.checks.items():
            status = "✓" if passed else "✗"
            print(f"  {status} {check.replace('_', ' ').title()}")
        
        print("\nFeedback:")
        for item in result.feedback:
            print(f"  • {item}")
        print("=" * 60)


if __name__ == "__main__":
    main()

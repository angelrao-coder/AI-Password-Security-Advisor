
import re

COMMON_PASSWORDS = [
    "password", "123456", "12345678",
    "qwerty", "admin", "letmein",
    "welcome", "iloveyou"
]


def analyze_password(password):

    score = 0
    checks = []

    # Length check
    if len(password) >= 12:
        score += 25
        checks.append(("Length (12+ characters)", True))
    else:
        checks.append(("Length (12+ characters)", False))

    # Uppercase check
    if re.search(r"[A-Z]", password):
        score += 15
        checks.append(("Uppercase letters", True))
    else:
        checks.append(("Uppercase letters", False))

    # Lowercase check
    if re.search(r"[a-z]", password):
        score += 15
        checks.append(("Lowercase letters", True))
    else:
        checks.append(("Lowercase letters", False))

    # Number check
    if re.search(r"[0-9]", password):
        score += 15
        checks.append(("Numbers", True))
    else:
        checks.append(("Numbers", False))

    # Special character check
    if re.search(r"[^A-Za-z0-9]", password):
        score += 15
        checks.append(("Special characters", True))
    else:
        checks.append(("Special characters", False))

    # Common password check
    if password.lower() not in COMMON_PASSWORDS:
        score += 15
        checks.append(("Not a common password", True))
    else:
        checks.append(("Not a common password", False))

    return score, checks


def get_strength(score):

    if score >= 80:
        return "STRONG"

    elif score >= 50:
        return "MODERATE"

    else:
        return "WEAK"


def generate_prompt(score, checks):

    passed = []
    failed = []

    for name, status in checks:

        if status:
            passed.append(name)
        else:
            failed.append(name)

    prompt = f"""
You are an expert Cybersecurity Password Security Advisor.

Your task is to analyze password security characteristics.

PASSWORD SECURITY SCORE: {score}/100

PASSED SECURITY CHECKS:
{passed}

FAILED SECURITY CHECKS:
{failed}

INSTRUCTIONS:

1. Explain the security weaknesses.
2. Suggest three ways to improve password security.
3. Explain the importance of strong passwords.
4. Use simple and understandable language.
5. Never request or reveal the actual password.
6. Do not claim that a password is impossible to crack.

OUTPUT FORMAT:

Security Analysis:
Weaknesses:
Recommendations:
Final Security Advice:

Keep your response concise and educational.
"""

    return prompt

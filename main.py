
from password_analyzer import analyze_password, get_strength
from prompt_engine import generate_prompt


def display_banner():

    print("=" * 55)
    print("       AI PASSWORD SECURITY ADVISOR")
    print("=" * 55)

    print("Cybersecurity + Prompt Engineering Project")
    print("Developed using Python")
    print("=" * 55)


def main():

    display_banner()

    print("\nIMPORTANT:")
    print("Use only sample passwords.")
    print("Never enter your real password.")

    password = input("\nEnter a sample password: ")

    if not password:
        print("\nPlease enter a password.")
        return

    score, checks = analyze_password(password)

    strength = get_strength(score)

    print("\n" + "=" * 55)
    print("          PASSWORD SECURITY REPORT")
    print("=" * 55)

    print(f"\nSecurity Score: {score}/100")
    print(f"Password Strength: {strength}")

    print("\nSECURITY CHECKS:")

    for name, status in checks:

        if status:
            print(f"[PASS] {name}")

        else:
            print(f"[FAIL] {name}")

    prompt = generate_prompt(score, checks)

    print("\n" + "=" * 55)
    print("          PROMPT ENGINEERING MODULE")
    print("=" * 55)

    print("\nGenerated AI Prompt:")
    print(prompt)

    print("=" * 55)

    print("\nAI RECOMMENDATIONS:")

    failed_checks = [
        name for name, status in checks if not status
    ]

    if failed_checks:

        print("\nAreas that need improvement:")

        for item in failed_checks:
            print(f"- Improve {item}")

    else:

        print("All basic security checks passed!")

    print("\nThank you for using AI Password Security Advisor!")
    print("=" * 55)


if __name__ == "__main__":
    main()

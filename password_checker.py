import re

def check_password_strength(password):
    """
    Checks the strength of a password based on length, numbers, and special characters.
    Returns a score, a strength label, and a list of feedback messages.
    """
    score = 0
    feedback = []
    
    # Criteria 1: Length
    if len(password) < 8:
        feedback.append("Password is too short. It should be at least 8 characters long.")
    else:
        score += 1
        
    # Criteria 2: Numbers
    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("Password should contain at least one number.")
        
    # Criteria 3: Uppercase Letters
    if re.search(r"[A-Z]", password):
        score += 1
    else:
        feedback.append("Password should contain at least one uppercase letter.")
        
    # Criteria 4: Lowercase Letters
    if re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("Password should contain at least one lowercase letter.")
        
    # Criteria 5: Special Characters
    if re.search(r"[ !@#$%^&*()_+\-=\[\]{};':\"\\|,.<>/?]", password):
        score += 1
    else:
        feedback.append("Password should contain at least one special character (e.g., !@#$%).")
        
    # Determine Strength Label
    if score == 5:
        strength = "Very Strong"
    elif score >= 3:
        strength = "Strong"
    elif score >= 2:
        strength = "Medium"
    else:
        strength = "Weak"
        
    return strength, feedback

def main():
    print("--- Password Strength Checker ---")
    print("Type 'exit' or 'quit' to stop the program.\n")
    
    while True:
        try:
            password = input("Enter a password to check: ")
        except (EOFError, KeyboardInterrupt):
            print("\nExiting...")
            break
            
        if password.lower() in ['exit', 'quit']:
            break
            
        if not password:
            print("Please enter a password.\n")
            continue
            
        strength, feedback = check_password_strength(password)
        
        print(f"\nStrength: {strength.upper()}")
        
        if feedback:
            print("Suggestions to improve:")
            for tip in feedback:
                print(f"- {tip}")
        else:
            print("Great job! Your password meets all the criteria.")
            
        print("-" * 30 + "\n")

if __name__ == "__main__":
    main()

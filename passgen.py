import secrets
import string

def generate_password(length, complexity):
    """Generates a password based on the specified length and complexity level.
    
    Args:
        length: The desired length of the password.
        complexity: A string indicating the desired complexity level (e.g., "strong", "medium", "weak").
        
    Returns:
        A string representing the generated password.
    """
    if length < 1:
        raise ValueError("Password length must be at least 1.")
    
    if complexity == "strong":
        if length < 8:
            raise ValueError("Strong passwords should be at least 8 characters long.")
        charset = string.ascii_letters + string.digits + string.punctuation
        password = [
            secrets.choice(string.ascii_lowercase),
            secrets.choice(string.ascii_uppercase),
            secrets.choice(string.digits),
            secrets.choice(string.punctuation)
        ]
        password += [secrets.choice(charset) for _ in range(length - 4)]
    
    elif complexity == "medium":
        if length < 6:
            raise ValueError("Medium passwords should be at least 6 characters long.")
        charset = string.ascii_letters + string.digits
        password = [secrets.choice(charset) for _ in range(length)]
    
    else:  # weak
        if length < 4:
            raise ValueError("Weak passwords should be at least 4 characters long.")
        charset = string.ascii_lowercase
        password = [secrets.choice(charset) for _ in range(length)]
    
    secrets.SystemRandom().shuffle(password)  # Shuffle to ensure randomness
    return ''.join(password)

def generate_password_list(num_passwords, length, complexity):
    """Generates a list of passwords based on the specified number, length, and complexity.
    
    Args:
        num_passwords: The number of passwords to generate.
        length: The desired length of each password.
        complexity: A string indicating the desired complexity level.
        
    Returns:
        A list of generated passwords.
    """
    if num_passwords < 1:
        raise ValueError("Number of passwords must be at least 1.")
    
    passwords = []
    for _ in range(num_passwords):
        password = generate_password(length, complexity)
        passwords.append(password)
    return passwords

if __name__ == "__main__":
    try:
        num_passwords = int(input("Enter the number of passwords to generate: "))
        password_length = int(input("Enter the desired password length: "))
        complexity = input("Enter the desired complexity level (strong, medium, weak): ").strip().lower()
        
        # Validate complexity input
        if complexity not in ["strong", "medium", "weak"]:
            raise ValueError("Complexity level must be 'strong', 'medium', or 'weak'.")

        passwords = generate_password_list(num_passwords, password_length, complexity)
        print("\nGenerated Passwords:")
        for password in passwords:
            print(password)
    except ValueError as e:
        print(f"Error: {e}")

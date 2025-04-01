import random
import string

def generate_password(length=12, use_lowercase=True, use_uppercase=True, 
                     use_digits=True, use_special=True, special_chars='!@#$%^&*()'):
    """
    Generate a random password with specified criteria.
    
    Parameters:
    - length: Length of the password (default: 12)
    - use_lowercase: Include lowercase letters (default: True)
    - use_uppercase: Include uppercase letters (default: True)
    - use_digits: Include digits (default: True)
    - use_special: Include special characters (default: True)
    - special_chars: Custom set of special characters (default: '!@#$%^&*()')
    
    Returns:
    - Generated password as a string
    """
    
    # Create character pool based on selected criteria
    character_pool = ''
    
    if use_lowercase:
        character_pool += string.ascii_lowercase
    if use_uppercase:
        character_pool += string.ascii_uppercase
    if use_digits:
        character_pool += string.digits
    if use_special:
        character_pool += special_chars
    
    # Verify at least one character type is selected
    if not character_pool:
        raise ValueError("At least one character type must be selected")
    
    # Verify password length is sufficient
    if length < 4:
        raise ValueError("Password length must be at least 4 characters")
    
    # Generate password ensuring at least one character from each selected type
    password = []
    
    # Add at least one character from each selected type
    if use_lowercase:
        password.append(random.choice(string.ascii_lowercase))
    if use_uppercase:
        password.append(random.choice(string.ascii_uppercase))
    if use_digits:
        password.append(random.choice(string.digits))
    if use_special:
        password.append(random.choice(special_chars))
    
    # Fill the rest with random characters from the pool
    remaining_length = length - len(password)
    password.extend(random.choice(character_pool) for _ in range(remaining_length))
    
    # Shuffle to avoid predictable patterns
    random.shuffle(password)
    
    return ''.join(password)

# Example usage
if __name__ == "__main__":
    print("Simple Password Generator")
    print("-" * 25)
    
    try:
        length = int(input("Enter password length (default 12): ") or 12)
        lowercase = input("Include lowercase letters? (y/n, default y): ").lower() != 'n'
        uppercase = input("Include uppercase letters? (y/n, default y): ").lower() != 'n'
        digits = input("Include digits? (y/n, default y): ").lower() != 'n'
        special = input("Include special characters? (y/n, default y): ").lower() != 'n'
        
        password = generate_password(
            length=length,
            use_lowercase=lowercase,
            use_uppercase=uppercase,
            use_digits=digits,
            use_special=special
        )
        
        print("\nGenerated Password:", password)
        print("Password length:", len(password))
    except ValueError as e:
        print("Error:", e)
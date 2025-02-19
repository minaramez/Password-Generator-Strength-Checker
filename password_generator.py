#!/usr/bin/env python3

import random
import string
import re
import math
from collections import Counter

print("")
print("")
print("Script written by: Mina Ramez Farag")
print("")
print("       *****************************************************")
print("       *******PASSWORD GENERATOR AND STRENGTH CHECKER*******")
print("       *****************************************************")
print("")


def generate_secure_password():
    length = 16
    characters = string.ascii_letters + string.digits + string.punctuation
    
    while True:
        secure_password = ''.join(random.SystemRandom().choice(characters) for _ in range(length))

        # Ensure the password meets the desired criteria
        has_uppercase = any(char.isupper() for char in secure_password)
        has_lowercase = any(char.islower() for char in secure_password)
        has_digit = any(char.isdigit() for char in secure_password)
        has_special = any(char in string.punctuation for char in secure_password)

        if has_uppercase and has_lowercase and has_digit and has_special:
            entropy = calculate_entropy(secure_password)
            if entropy >= 80:
                break

    return secure_password


def calculate_entropy(password):
    char_sets = [
        string.ascii_lowercase,
        string.ascii_uppercase,
        string.digits,
        string.punctuation
    ]
    
    char_pool = sum(any(c in char_set for c in password) for char_set in char_sets)
    
    if char_pool == 0:
        return 0
    
    entropy = len(password) * math.log2(char_pool * len(set(password)))
    return entropy

def analyze_password_strength(password):
    min_length = 12

    
    has_uppercase = any(char.isupper() for char in password)
    has_lowercase = any(char.islower() for char in password)
    has_digit = any(char.isdigit() for char in password)
    has_special = any(char in string.punctuation for char in password)
    
    #check password length
    if len(password) < min_length:
        return "Password is too short. Minimum length should be {} characters.".format(min_length)
    
    if not (has_uppercase and has_lowercase and has_digit and has_special):
        return "Password should include at least one uppercase, lowercase, digit, and special character."
    
    #calculate entropy
    entropy = calculate_entropy(password)
    if entropy < 70:  
        return "Password entropy is too low. Use a more complex and unpredictable password."
    
    return "Password is strong."

while True:
    print("")
    print("Choose an option:")
    print("1. Generate a secure password")
    print("2. Test the strength of a password")
    choice = input("Enter your choice (1, 2, or 'quit' to exit): ")

    if choice == '1':
        secure_password = generate_secure_password()
        print("")
        print("Generated secure password:", secure_password)

    elif choice == '2':
        print("")
        password = input("Enter a password to analyze: ")
        result = analyze_password_strength(password)
        print(result)

    elif choice.lower() == 'quit':
        break

    else:
        print("Invalid choice. Please select 1, 2, or type 'quit' to exit.")

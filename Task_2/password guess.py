import re
password = input("Enter your password to evaluate: ")
strength = 0
if len(password) >= 8:
    strength += 1
else:
    print("Password must be at least 8 characters long.")
if re.search(r'[A-Z]', password):
    strength += 1
else:
    print("Password must contain at least one uppercase letter.")
if re.search(r'[a-z]', password):
    strength += 1
else:
    print("Password must contain at least one lowercase letter.")
if re.search(r'\d', password):
    strength += 1
else:
    print("Password must contain at least one digit.")
if re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
    strength += 1
else:
    print("Password must contain at least one special character.")
if strength == 5:
    print("Password strength: Strong password")
elif strength == 4:
    print("Password strength: Moderate password")
else:
    print("Password strength: Weak password")

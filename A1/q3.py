password = input("Enter the password: ")

is_length_valid = 6 <= len(password) <= 16
has_lower = False
has_upper = False
has_digit = False
has_special = False

for char in password:
    if 'a' <= char <= 'z':
        has_lower = True
    elif 'A' <= char <= 'Z':
        has_upper = True
    elif '0' <= char <= '9':
        has_digit = True
    elif char in "$#@":
        has_special = True

if not is_length_valid:
    print("Password length must be between 6 and 16 characters.")
if not has_lower:
    print("Password must contain at least one lowercase letter.")
if not has_upper:
    print("Password must contain at least one uppercase letter.")
if not has_digit:
    print("Password must contain at least one digit.")
if not has_special:
    print("Password must contain at least one special character ($, #, @).")

if is_length_valid and has_lower and has_upper and has_digit and has_special:
    print("Password is valid.")

import re
import random

old_passwords = ["Admin@123", "Hello@123", "Password@123"]

password = input("Enter Password: ")

score = 0

# Length Check
if len(password) >= 8:
    score += 1

# Complexity Checks
if re.search("[A-Z]", password):
    score += 1

if re.search("[a-z]", password):
    score += 1

if re.search("[0-9]", password):
    score += 1

if re.search("[@#$%^&*!]", password):
    score += 1

# Uniqueness Check
if password not in old_passwords:
    score += 1
else:
    print("Password already used before!")

# Strength Analysis
if score <= 2:
    print("Strength: Weak")
elif score <= 4:
    print("Strength: Medium")
else:
    print("Strength: Strong")

# Strong Password Alternative
if score < 6:
    strong_pass = "User@" + str(random.randint(1000,9999))
    print("Suggested Strong Password:", strong_pass)

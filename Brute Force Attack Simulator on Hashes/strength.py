import math

def entropy(password):
    charset = 0
    if any(c.islower() for c in password): charset += 26
    if any(c.isupper() for c in password): charset += 26
    if any(c.isdigit() for c in password): charset += 10
    if any(c in "!@#$%^&*()" for c in password): charset += 10
    return round(len(password) * math.log2(charset), 2) if charset else 0

def strength(password):
    e = entropy(password)
    if e < 30: return "Very Weak"
    if e < 50: return "Weak"
    if e < 70: return "Medium"
    if e < 90: return "Strong"
    return "Very Strong"

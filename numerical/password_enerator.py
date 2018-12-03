from random import SystemRandom
sr = SystemRandom()

def generate_password(length, valid_chars = None):
    if valid_chars == None:
        valid_chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        valid_chars += valid_chars.lower() + "0123456789"

    password = ""
    counter = 0
    while counter < length:
        rnum = sr.randint(0, 128)
        char = chr(rnum)
        if char in valid_chars:
            password += chr(rnum)
            counter += 1
    return password


print("Automatically generated password by Python: ", generate_password(15))
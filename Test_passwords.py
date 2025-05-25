
import re

def is_valid_password(password):
    if len(password) != 8:
        return False
    if not re.search(r"[A-Za-z]", password):
        return False
    if not re.search(r"\d", password):
        return False
    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        return False
    return True

print("Testing password validation...")
print(is_valid_password("Abc@1234"))  
print(is_valid_password("abcdefgh"))  
print(is_valid_password("A1@abcd"))   
print(is_valid_password("A1@abcdef")) 

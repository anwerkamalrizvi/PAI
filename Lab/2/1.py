import re
def is_valid_password(password):


    if len(password) < 8:
        return False
    
    if not re.search(r'[a-zA-Z]', password):
        return False
    

    if not re.search(r'\d', password):
        return False
    
    if not re.search(r'[@#$%]', password):
        return False
    return True
test_passwords = ["abc123", "password123", "Pass@123", "Short1#", "Valid@1234"]
for pwd in test_passwords:
    print(f"'{pwd}': {is_valid_password(pwd)}")
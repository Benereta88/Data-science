# Uppgift 7
# Skapa en funktion validate_password(password) som kontrollerar att lösenordet är minst 8 tecken långt och innehåller minst en siffra.

def validate_password(legth=8):
    import random 
    import string
    
    validate_password = ''.join(random.choices(string.ascii_lowercase + string.digits, k = legth))
    return validate_password

validate_password = validate_password(8)
print("Generete_password:", validate_password)
   
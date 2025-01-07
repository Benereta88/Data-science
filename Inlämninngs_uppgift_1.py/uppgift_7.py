# Uppgift 7
# Skapa en funktion validate_password(password) som kontrollerar att lösenordet är minst 8 tecken långt och innehåller minst en siffra.

def validate_password(password: str) -> bool:
    """
    Kontrollerar att lösenordet är minst 8 tecken långt och innehåller minst en siffra.
    """
    # Kontrollera om lösenordet är minst 8 tecken långt och innehåller minst en siffra
    if len(password) >= 8 and any(char.isdigit() for char in password):
        return True
    return False

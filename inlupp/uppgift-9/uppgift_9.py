# Uppgift 9
# Skapa en funktion is_palindrome(string) som kontrollerar om en given sträng är ett palindrom (dvs. samma framifrån och bakifrån).


def is_palindrome(string: str) -> bool: #
    return string == string[::-1] # Retunerar True om strängen är samma framifrån och bakifrån, annan False

print(is_palindrome("radar") == True)
print(is_palindrome("python") == False)
print(is_palindrome("") == True)


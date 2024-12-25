import random
import string

def generete_password(legth=18):
    characters = string.ascii_letters + string.digits
    return "".join(random.choice(characters)for _ in range(legth))

generete_password = generete_password(8)
print("Generete_password:", generete_password)
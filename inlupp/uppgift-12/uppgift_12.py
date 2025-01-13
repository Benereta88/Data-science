# Uppgift 12
# Skapa en funktion create_student_register(students) som tar emot en lista med namn och ålder och returnerar en dictionary där namnet är nyckeln och åldern är värdet.

def create_student_register(students: list) -> dict:
    return {name: age for name, age in students}

from uppgift_12 import create_student_register

def test_create_student_register():
    students = [("Anna", 20), ("Bertil", 25), ("Cecilia", 22)]
    assert create_student_register(students) == {"Anna": 20, "Bertil": 25, "Cecilia": 22}

# Kör testfunktionen
test_create_student_register()
print("Alla tester passerade.")

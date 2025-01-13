# Uppgift 12
# Skapa en funktion create_student_register(students) som tar emot en lista med namn och ålder och returnerar en dictionary där namnet är nyckeln och åldern är värdet.


def test_create_student_register_empty():
        students = []
        assert create_student_register(students) == {}

def test_create_student_register_single():
        students = [("David", 30)]
        assert create_student_register(students) == {"David": 30}

def create_student_register(students):
    return {name: age for name, age in students}

students = [("Anna", 20), ("Bertil", 25), ("Cecilia", 22)]
print(create_student_register(students) == {"Anna": 20, "Bertil": 25, "Cecilia": 22})

# Uppgift 6
# Skapa en funktion multiplication_table(n, limit) som returnerar multiplikationstabellen för n upp till limit i en lista.
# Testa funktionen multiplication_table

def multiplication_table(n, limit): 
    # Skapa en lista som innehåller multiplikationerna av n upp till limit
    return [n * i for i in range(1, limit + 1)]

# Testa funktionen
print(multiplication_table(2, 3) == [2, 4, 6])
print(multiplication_table(3, 5) == [3, 6, 9, 12, 15])


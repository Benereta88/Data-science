# Uppgift 2
# Skapa en funktion sum_list(numbers) som returnerar summan av alla siffror i listan.


def sum_list(numbers: list[int]) -> int: # Funktionen tar en parameter nummers av datatypen list[int] och retunerar en int.
    return sum(numbers) # Retunerar summan av alla siffror i listan.

print (sum_list([1, 2, 3, 4, 5, 6]))
print(sum_list([1, 2, 3]) == 6)
print(sum_list([]) == 0)
print(sum_list([-1, -1, 2]) == 0)
    








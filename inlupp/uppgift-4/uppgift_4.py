# Uppgift 4
# Skapa en funktion fibonacci(n) som returnerar en lista med de första n Fibonacci-talen.
 # Funktionen har en parameter n som är ett heltal och retunerar en lista med de första n fibonacci-talen.

def fibonacci(n: int) -> list[int]: # Funktionen 
   
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    
    fib_sequence = [0, 1]
    while len(fib_sequence) < n:
        next_value = fib_sequence[-1] + fib_sequence[-2]
        fib_sequence.append(next_value)
        return fib_sequence

print(fibonacci(5) == [0, 1, 1, 2, 3])
print(fibonacci(0) == []) 
print(fibonacci(1) == [0])




   
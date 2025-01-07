# Uppgift 4
# Skapa en funktion fibonacci(n) som returnerar en lista med de första n Fibonacci-talen.

def fibonacci(n: int) -> list:
    """
    Returnerar en lista med de första n Fibonacci-talen.
    """
    # Om n är 0, returnera en tom lista
    if n == 0:
        return []
    
    # För n == 1, returnera listan med endast 0
    if n == 1:
        return [0]
    
    # Starta med de två första Fibonacci-talen [0, 1]
    fib_sequence = [0, 1]
    
    # Lägg till Fibonacci-tal tills listan har n tal
    for i in range(2, n):
        next_fib = fib_sequence[-1] + fib_sequence[-2]
        fib_sequence.append(next_fib)
    
    return fib_sequence

# Uppgift 4
# Skapa en funktion fibonacci(n) som returnerar en lista med de första n Fibonacci-talen.
 # Funktionen har en parameter n som är ett heltal och retunerar en lista med de första n fibonacci-talen.

def fibonacci(n: int) -> list[int]:
        if n <= 0:
            return []
        elif n == 1:
            return [0]
        elif n == 2:
            return [0, 1]
        
        fib_list = [0, 1]
        for i in range(2, n):
            fib_list.append(fib_list[-1] + fib_list[-2])
        
        return fib_list

print(fibonacci(5))
print(fibonacci(0)) 
print(fibonacci(1))



   
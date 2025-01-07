# Uppgift 3
# Hitta det största talet i en lista
# uppgift_3.py

def max_in_list(numbers: list[int]) -> int:
    """
    Returnerar det största talet i en lista av heltal.
    """
    if not numbers:  # Om listan är tom
        raise ValueError("Listan får inte vara tom")
    
    return max(numbers)  # Använder den inbyggda max() för att hitta största talet


print(max_in_list([1, 2, 3])) 
print(max_in_list([-5, 0, 5])) 
print(max_in_list([10]))



      


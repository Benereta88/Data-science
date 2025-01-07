# Uppgift 3
# Hitta det största talet i en lista
# uppgift_3.py

def max_in_list(numbers: list) -> int:
    highest = numbers[0] 
    for num in numbers:
        if num > highest:
            highest = num
    return highest
        
    
print(max_in_list([1, 2, 3]) == 3)
print(max_in_list([-5, 0, 5]) == 5) 
print(max_in_list([10]) == 10)



      


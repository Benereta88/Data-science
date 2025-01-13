# Uppgift 3
# Hitta det största talet i en lista

def max_in_list(numbers: list) -> int: # Tar en lista av heltal och returnerar det största talet.
    highest = numbers[0] # Sätter första talet i listan som det högsta.
    for num in numbers: 
        if num > highest: 
            highest = num
    return highest
        
    
print(max_in_list([1, 2, 3]) == 3)
print(max_in_list([-5, 0, 5]) == 5) 
print(max_in_list([10]) == 10)



      


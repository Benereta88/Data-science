# Opnnar en fil för att skriva till den 

with open("data.csv", "w") as file:
    file.write("Name, Age, City\n")
    file.write("John, 25, Stockholm\n")
    file.write("Anna, 30, Malmö\n")
    file.write("Cecilia, 36, Uppsala\n")

    # Öppnar en fil för att skriva till den
with open("data.csv", "r") as file:
    for line in file:
        print(line.strip())
        


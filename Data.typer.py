# Python - Datatyper
# Datatyper är en grundläggande byggsten i alla programmeringsspråk. De bestämmer vilken typ av data en variabel kan hålla och vilka operationer som kan utföras på den. I Python är datatyper dynamiska, vilket innebär att du inte behöver deklarera dem explicit.

# Olika datatyper 

# Int
# Heltal används för att representera heltalsvärden, både positiva och negativa.

x = 10
y = -5
print(type(x)) # Output: <clas 'int'>
print(type(y)) # Output: <clas 'int'>

  #Floats
# Floats används för att representera decimaltal.

x =10.5
y = -4.5
print(type(x)) # Output: <clas float'>
print(type(y)) # Output: <clas float'>

 # Strings
# Strings används för att representera text. De omges av enkla eller dubbla citationstecken.

name = "Anna"
greeting = "Hello"
y = -4.5
print(type(name)) # Output: <clas str'>
print(name + "" + greeting) # Output: Anna, Hello

# Booleans
# Booleans representerar två värden: True och False. De används ofta i villkorssatser.

is_active = True
has_error = False
print(type(is_active)) # Output: <class 'bool'>
print(is_active and has_error) # Output: False

# Lists
# Lists är samlingar av element som kan innehålla olika datatyper. De omges av hakparenteser.

numbers = [1, 2, 3, 4, 5]
mixed = ["Anna", 23, True]
print(type(numbers)) # Output: <class 'list'>
print(numbers[0]) # Output: 1

# Tuples
# Tuples är liknande listor men är oföränderliga (immutable). De omges av parenteser.

coordinates = (10, 20)
print(type(coordinates)) # Output: <class 'tuple'>
print (coordinates[0]) # Output: 10

# Sets
# Sets är en samling av unika element. De omges av klamrar.

unique_numbers = {1, 2, 3, 4, 5}
print(type(unique_numbers)) # Output: <'class 'set'>
print (unique_numbers)       # Output: {1, 2, 3, 4, 5}

# DictionarieS
# Dictionaries används för att lagra key-value-par. De omges av klamrar.

person = { "name": "Anna", "age": 24}
print(type(person)) # Output: <class 'disc'>
print(person["name", "age"]) # Output: Anna, 24


# Datatypskonvertering
# Python tillåter konvertering mellan olika datatyper vid behov. Här är några vanliga konverteringar:
  
x = 10  # Integrer
y = float(x)  # Convert to float

print(type(y)) # Output: <class 'float'>

z = str(x) # Output: < Convert to string 
print(type(z)) # Output: < class 'str'>

  
# Bra praxis
# 1. Använd lämpliga datatyper för att förbättra kodens läsbarhet och effektivitet. 
# 2. Var medveten om vilka operationer som stöds av varje datatyp.
# 3. Var försiktig vid typkonvertering för att undvika oväntade fel.

# Övningar
# 1. Skapa variabler av varje datatyp som nämnts ovan och skriv ut deras typer med type().
# 2. Skapa en lista som innehåller minst tre olika datatyper och iterera igenom den för att skriva ut varje elements typ.
# 3. Konvertera ett heltal till en sträng och kombinera det med en annan sträng i en utskrift.
 # 
x = 10
x_str = str(x)
print("The number is: " + x_str)


# Extra fron lärare

# heltal = 10
# flyttal = 3.14
# text = "Python är roligt"
# sanningsvärde = True

# print(type(heltal))
# print(type(flyttal))
# print(type(text))
# print(type(sanningsvärde))

x = "123"
y = 2
z = int(x) * y
print(z)



x = 0.1 + 0.2

print(x)

x = 10
y = 3

# (+, -, *, /, //, %, **)
print(x + y)
print(x - y)
print(x * y)
print(x / y)
print(x // y)
print(x % y)
print(x ** y)


pi = 3.14
print(int(pi))
x = int(pi)
print(x)

heltal = 5
y = float(heltal)
print(y)

resultat = round(0.00012 + 0.00018, 4)  # Avrunda till 1 decimal
print(resultat)  # Output: 0.3


# tal1 = 0.1
# tal2 = 0.2
# tal1 = int(tal1 * 10)
# tal2 = int(tal2 * 10)
# print(tal1 + tal2)

# korrektSvar = (tal1 + tal2) / 10

# print(korrektSvar)

print("Hej" * 3)

text = "DataScience"

print(text[0])

print(text[-1])

print(text[0],text[1])

print(text[0:5])

text = " Python är roligt "

no_whitespace = text.strip()

print(no_whitespace)

fantastico = no_whitespace.replace("roligt", "fantastiskt")

print(fantastico)

UPPER = fantastico.upper()

print(UPPER)


name = input("Vad heter du? ")
age = input("Hur gammal är du? ")

print(f"Hej, {name}! Du är {age} år ung.")


my_list = ["a", "b", "c", "d"]
print(my_list[0])  # Output: a

print(my_list[-2])

# Lista med heltal
numbers = [1, 2, 3, 4, 5]

# Tom lista
empty_list = []
print(empty_list)

print(type(empty_list))

if empty_list == "[]":
    print("Listan är tom 1")

if empty_list == []:
    print(empty_list == [])
    print("Listan är tom 2")

if empty_list:
    print("Listan är tom 3")

if not empty_list:
    print("Listan är tom 4")

listaMedEttElement = [1]

if listaMedEttElement:
    print("Listan är inte tom 5")

if not listaMedEttElement:
    print("Listan är tom 6")

listaMedFlera = [1,2,4]

if listaMedFlera:
    print("Listan är inte tom 7")

# Blandade datatyper
mixed_list = [1, "text", True]

print(mixed_list[0])
print(mixed_list[1])
print(mixed_list[2])

print(mixed_list)

longList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(longList[0:5])

reallyLongList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

print(reallyLongList[0:])
print(reallyLongList[4:])
print(reallyLongList[:14])
print(reallyLongList[3:14])
print(reallyLongList[-1:0])

reallyLongList.reverse()
print(reallyLongList) #för att visa tvärtom fråm 20.....1

# print(reallyLongList.reverse())


my_list = ["äpple", "banan", "körsbär"]

for fruit in my_list:
    if fruit != "körsbär":
      print("Jag gillar " + fruit)
    else:
      print("Jag gillar inte " + fruit)




reallyLongList = ["äpple", "banan", "körsbär", "druva", "apelsin", "päron", "kiwi", "mango", "passionsfrukt", "ananas"]
print(len(reallyLongList))
x = 1
for i, fruit in enumerate(reallyLongList):
  if i  == (i+1):
   continue
if (i+1) % 3 == 0:
   print(fruit)
x += 1
x = x + 1
print(type(x))
print("x är:")
print(x)


reallyLongList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

for number in reallyLongList:
    if number % 2 == 0:
        print(number)

for number in reallyLongList:
    if number % 2 != 0:
        print(number)
        ''''''

# Ursprunglig lista
my_lista = ["stockholm", "malmö", "karlstad", "örebro", "lulea"]

print(my_lista)

# Lägg till en ny stad i slutet av listan
my_lista.append("göteborg")

# Ta bort den andra staden i listan (index 1)
del my_lista[1]

# Skriv ut alla städer med en for-loop
for stad in my_lista:
    print(stad)

# Uppdatera varje stad i listan till stor begynnelsebokstav
my_lista = [stad.capitalize() for stad in my_lista]


# Skriv ut den uppdaterade listan
print("Uppdaterade städer:", my_lista)

x = 10
y = 5

print(x > 5 and y < 10)  # Output: True
print(x > 5 or y < 10)  # Output: 
print(x > 5 and y < 4)  # Output: 
print(x > 5 or y < 4)  # Output:

z = 3

print(x > 5 or y < 4 and z == 3)  # Output:
print(x > 5 or y < 4 and z != 3)  # Output:

print(x > 15 or y < 4 and z != 3)  # Output:


print(x > 5 and y < 5 and z == 3)  # Output:

# Överkurs
print(x > 5 and y <= 5 and z == 3)  # Output:
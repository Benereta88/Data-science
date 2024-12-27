# Python - Dictionaries

# En dictionary (eller "ordbok") i Python är en samling av nyckel-värde-par. 
# Det är en mycket användbar datastruktur när du behöver associera unika nycklar med specifika värden.

# Skapa en dictionary
# Du kan skapa en dictionary med hjälp av klamrar ({ }) och separera nycklar och värden med kolon ( : ).

person = {
"name": "Anna",
"age": 24,
"city": "Stockholm"
}
print(person) # Output: {"name": "Anna", "age": 24, "city": "Stockholm"}

# Åtkomst till värden
# Du kan komma åt ett värde genom att använda dess nyckel inom hakparenteser ( ).

print(person["name"]) # Output: Anna
print(person["age"]) # Output: 24

# Lägg till eller uppdatera nyckel-värde-par
  # Lägg till ett nytt par

person["profesion"] = "Engineer"
print(person) # Output: {"name": "Anna", "age": 24, "city": "Stockholm", "profesion": "Engenieer"}

# Uppdatera ett benefit par
person["profesion"] = "Data manager"
print(person) # Output:{"name": "Anna", "age": 24, "city": "Stockholm", "profesion": "Data manager"}

# Ta bort ett nyckel-värde-par

# Ta bort en nyckel med del
del person["city"]
print(person) # Output: {"name": "Anna", "age": 24, "profesion": "Data manager"}
 # Använd pop för att ta bort och få tillbacka värdet
age = person.pop("city")
print("city") # Output: "Stockholm"
print(person)  # Output: {"name": "Anna", "age": 24, "profesion": "Data manager"}


# Dictionary-metoder

# keys()        Returnerar en vy av alla nycklar i dictionaryn.

print(person.keys())  # Output: dict_keys(['namn', 'yrke'])

# values()      Returnerar en vy av alla värden i dictionaryn.

print(person.values()) # Output: dict_values(['Anna', 'Data manager'])

# items()       Returnerar en vy av alla nyckel-värde-par som tuples.

print(person.intems()) # Output: dict_items([('namn', 'Anna'), ('yrke', 'Dta manager')])

# get()         Hämtar ett värde för en nyckel utan att kasta ett fel om nyckeln inte finns.

print(person.get("namn"))  # Output: Anna
print(person.get("age","Okänd"))  # Output: Okänd

# update()      Lägger till eller uppdaterar flera nyckel-värde-par.

person.uppdate({"age": 25, "city": "Malmö"})
print(person)   # Output: {'namn': 'Anna', 'yrke': 'Data manager', 'age': 25, 'city': 'Malmö'}

# Loopa över en dictionary

# Du kan iterera över nycklar, värden eller båda samtidigt i en dictionary.

# Interera över nycklar
for key in person:
  print(key)

  # Interera över värden
  for value in person:
    print(value)

    # Interera över nyckel-värde-par
    for key, value in person.intems():
      print(f"{key}: {value}")

# Nästlade dictionaries
# Dictionaries kan innehålla andra dictionaries som värden.

famity = {
  "mather":{"name": "Mira", "age": 46},
  "father":{"name": "Mico", "age": 50}
}
print(family["mather"]["name"])  # Output: Mira

# Övningar
# 1. Skapa en dictionary för en bok med nycklarna "titel", "författare" och "år". Lägg till en ny nyckel "genre".  

book = {
  "title": "Tänk rätt bli framgångsrik",
  "author": "Napoleon Hill",
  "year": 1981
}


print(book)  # Output: book = {"title": "Tänk rätt bli framgångsrik", "author": "Napoleon Hill", "year": 1981}

# 2. Skapa en nästlad dictionary som representerar en skolklass med elever och deras betyg.
# 3. Iterera över en dictionary och skriv ut alla nyckel-värde-par.
# 4. Använd   för att hämta värdet av en nyckel, och ange ett standardvärde om nyckeln inte finns.
 


# Extra fron läraren
produkt = {
  "namn": "Laptop", 
  "pris": 10000, 
  "lager": 50
}
print(produkt)
# 1. Skriv ut produktes pris.
print(produkt["pris"])
# 2. Lägg till en ny nyckel för "kategori".
produkt["kategori"] = "Datorer"
print(produkt)
# 3. Ändra värdet på "lager" till 40.
produkt["lager"] = "40"
print(produkt)
''''''




person = { 
    "name": "Anna",
    "age": 25,
    "city": "Stockholm"

}
# 1. Interera genom dictionaryn 

for attribyt, varde in person.items():
    print (f"Personens {attribyt} är {varde}")

    
# 2. Skriv ut varje nyckel och värde
for key, value in person.items():
 print(f"{key}: {value}")

''''''
names = ["Anna", "Mia", "Lela", "Akila", "Eva"]
print(names)
names.append("Akila")



''''''
x = input("Skriv ett tal: ")
while True:
 x = int(input("Skriv ett tal: "))
 if x > 0:
  print("Talet är positivt")
 elif x < 0:
   print("Talet är negativt")
else:
  print("Talet är noll")
  fortsatt = input("Vill du forsatta)(j/n): ")
  if forsatt == "n":
   print("Hej då!")
   "break"
   ''''''
   password = " "
while password != "hemligt":
    password = input("Ange lösenord: ")
    print("Rätt lösenord") 
    
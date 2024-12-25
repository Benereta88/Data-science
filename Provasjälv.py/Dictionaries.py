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
    
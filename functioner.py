# Python - Funktioner
# Funktioner är en viktig del av programmering eftersom de tillåter återanvändning av kod och förbättrar strukturen och läsbarheten i ett program. I Python kan du skapa egna funktioner med nyckelordet , och språket erbjuder även en mängd inbyggda funktioner. 

# Skapa en funktion. En funktion skapas med nyckelordet def följt av funktionsnamnet och parenteser. Kolon ( : ) markerar början av funktionsblocket, och koden inuti blocket måste vara indenterad.
# Exempel på en enkel funktion

def hälsa():
    print("Hej, hur mår du? ")

    hälsa()  # Output: Hej hur mår du?

# Funktioner med parametrar
# Du kan skicka värden till en funktion genom att använda parametrar.
# Flera parametrar kan separeras med kommatecken.

# Exempel på funktion med parametrar

def hälsa_namn(namn):
    print(f"Hej,{namn}! ")

    hälsa_namn("Anna")  # output: Hej, Anna!

    #Flera parameter kan separeras med kommatecken.
    def summera(a, b):
        print(a + b)
        summera(3, 5) # Output: 8
 
# Returvärden
# Funktion som retunerar ett värde
# En funktion kan returnera ett värde med hjälp av nyckelordet return.
# Exempel på funktion med returvärde

def multiplicera(a, b):
    return a * b

resultat = multiplicera(4, 2)
print(resultat)  # Output: 8

# Standardvärden för parametrar
# Parametrar kan ha standardvärden, vilket gör dem valfria vid anrop.

def hälsa_namn(namn = "världen!"):
    print(f"Hej,{namn}!")

    hälsa_namn()   # Output: Hej, världen!
    hälsa_namn("Anna") # Output: Hej, Anna!

# Anonyma funktioner (Lambda)
# Anonyma funktioner skapas med nyckelordet lambda och används ofta för korta, tillfälliga funktioner.
# Exempel på lambda-funktion

kvadrat = lambda x: x ** 2
print(kvadrat(4))   # Output: 16

# Övningar
# 1. Skriv en funktion som tar två tal som argument och returnerar deras summa.
# 2. Skapa en funktion som tar en lista som argument och returnerar den största siffran i listan.
# 3. Använd en lambda-funktion för att skapa en lista med kvadrater av talen 1 till 10.

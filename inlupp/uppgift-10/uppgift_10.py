# Uppgift 10
# Skapa en funktion celsius_to_fahrenheit(celsius) som konverterar en temperatur från Celsius till Fahrenheit.

def celsius_to_fahrenheit(celsius: float) -> float:
    """
    Konverterar en temperatur från Celsius till Fahrenheit.

    Parametrar:
    celsius (float): Temperaturen i Celsius.

    Returnerar:
    float: Temperaturen i Fahrenheit.
    """
    # Multiplicera Celsius-värdet med 9/5 och lägg till 32 för att få Fahrenheit-värdet
    return (celsius * 9/5) + 32

    # Testfall för att verifiera att funktionen fungerar korrekt
print(celsius_to_fahrenheit(0) == 32)
print(celsius_to_fahrenheit(100) == 212)
print(celsius_to_fahrenheit(-40) == -40)

   

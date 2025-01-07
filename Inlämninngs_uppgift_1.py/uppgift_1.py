# Uppgift 1
# Skapa en funktion is_odd(x) som returnerar True om x är udda och False om x är jämnt.
# def funktions_namn(variabel_namn: datatyp) -> returtyp:
# Exempel: def is_odd(x: int) -> bool:
# Förklaring: Funktionens namn är is_odd och tar en parameter x av datatypen int. Funktionen returnerar en bool.


# Funktionen is_odd tar ett argument x av typen int.
# Inuti funktionen används modulusoperatorn % för att k x int
# Om resten inte är 0 (dvs. talet är udda) returneras True, annars False.

from uppgift_1 import is_odd # Importera is_odd från uppgift_1.py
def is_odd(x: int) -> bool:
    """
    Returnerar True om x är udda, annars False.
    """  
    return x % 2 == 0

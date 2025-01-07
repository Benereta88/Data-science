# Exempel 1

Kontrollera om ett tal är jämnt.

## Beskrivning

Skapa en funktion is_even(number) som returnerar True om talet är jämnt och False annars.

### Funktionens Signatur

```python
def is_even(number: int) -> bool:
    """
    Returnerar True om talet är jämnt, annars False.
    """
    pass
```

### Exempel

```python
>>> is_even(2)
True
>>> is_even(3)
False
>>> is_even(0)
True
>>> is_even(-1)
False
```
# för att testa om det cod funkar så kontrollerar jag med 
pytest inlupp/exempel/test_exempel_1.py 
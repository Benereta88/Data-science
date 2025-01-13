# Uppgift 11
# Skapa en funktion word_count(text) som returnerar antalet ord i en given text.

def word_count(text: str) -> int: 
    return len(text.split())

# Test av funktionen
print(word_count("hello world") == 2)
print(word_count("") == 0)
print(word_count("Python är fantastiskt!") == 3)


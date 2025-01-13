#tryck på terminalen och skriv: python3 -m pip install pandas 
# eller 
# pip3 install pandas

# Kontrollera installationen:
import pandas as pd
print(pd.__version__)

# Konventionen är att importera Pandas som pd.
# Används för att hantera data i tabellform.
import pandas as pd

# Skapa en dataframe fron en dictionary 
data = {
 "Name": ["Anna", "Björn", "Cecilia"],
 "Age": [25, 30, 27],
 "City": ["Stockholm", "Göteborg", "Malmö"]
}

# Konventionen är att importera Pandas som pd.
# Används för att hantera data i tabellform.
# Kom igång med Pandas
df = pd.DataFrame(data)
print(df.iloc[0]) # skriver ut första raden



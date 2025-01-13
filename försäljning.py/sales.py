
# Steg 1: Läs in data
import pandas as pd
# Steg 1.1: Installera openpyxl vi kör detta i terminalen
#försäljning.py % /usr/local/bin/python3 -m pip install openpyxl Collecting openpyxl

# Läs in data 
df = pd.read_csv("sales.csv")
print(df.head())

 # steg 2: Lägg till en ny kolumn
import pandas as pd 

# Läg till kolumnen Total Sales 
df["Total Sales"] = df["Price"] * df["Quantity"]
print (df)

 # Steg 3: Filtrera data

import pandas as pd

# Filtrera data där Total Sales är större än 500
filtered_df = df[df["Total Sales"] > 500]

# Skriv ut det filtrerade DataFrame
print(filtered_df)

# Steg 4: Gruppera och summera 

summary_df = df.groupby("Product")["Total Sales"].sum()
# printera ut summeringen
print(summary_df)

# Steg 5: Exportera data
# Spara filtrerad data till en ny Csv-fil
filtered_df.to_csv("filtered_sales.csv", index=False)

#Spara summerad data till en Excel-fil
summary_df.to_excel("sales_summary.xlsx", sheet_name="Summary")



#  Steg 6: Kontrollera att filarna har skapats

# Kontrollera att filerna har skapats
try:
    with open("filtered_sales.csv", "r") as file:
        print("filtered_sales.csv har skapats.")
except FileNotFoundError:
    print("filtered_sales.csv har INTE skapats.")

try:
    with open("sales_summary.xlsx", "r") as file:
        print("sales_summary.xlsx har skapats.")
except FileNotFoundError:
    print("sales_summary.xlsx har INTE skapats.")
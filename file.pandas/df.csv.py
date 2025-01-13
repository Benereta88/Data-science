
df.to_csv("output.csv") # sparar dataframen till en csv-fil
df= pd.read_csv("output.csv") #läser in en csv_fil
df = df.filtren[0] # filtrerar datafram i kolumn 1

print(df) # skriver ut dataframen

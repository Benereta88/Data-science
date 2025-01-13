print(df)
df = pd.read_csv("data.csv")
print(df.head()) # skriver ut de första 5 raderna
print(df.tail()) # skriver ut de sista 5 raderna 
print(df.info()) # skriver ut information om dataframen
print(df.iloc[0]) # skriver ut första raden
print(df.filtrerar(df["Age"])) # filtrerar datafram med en kolumn
print(df.describe()) # skriver ut statistik om dataframen
print(df.sort_values ("Age")) # sorterar dataframe efter en kolumn
print(df.drop("Age", axis=1)) # tar bort en kolumn

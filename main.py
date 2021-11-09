import pandas as pd
from src.cleaning import *

df = pd.read_csv("data/IMDb movies.csv",encoding = "ISO-8859-1")
# Parámetros API
token = "k_uzahin65"
url = "https://imdb-api.com/en/API/SearchMovie/k_uzahin65/Interstellar"
parameters = {"Authorization": f"token {token}"}


nolan = filter_by(df,"director","Christopher Nolan")
print(nolan)
avengers = filter_by(df,"production_company", "Marvel Studios")

nolan['budget'].apply(cambioBudget)
avengers['budget'].apply(cambioBudget)

#exporto(nolan)
nolan.to_csv("data/nolan.csv", index =False)



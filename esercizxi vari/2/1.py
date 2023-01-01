"""
Si consideri il seguente dataset:
https://raw.githubusercontent.com/fivethirtyeight/data/master/nba-elo/nbaallelo.csv
1 - si effettui la stampa delle prime 5 righe e delle ultime 10.
2 - Si stampino le informazioni e i dati statistici.
3 - Si stampi la dimensione.
4 - Si scelga una colonna e si sostituiscano i valori con NaN, considerando solo i primi 20 elementi
di quella colonna.
5 - Si verifichino i tipi di dati che formano il dataset e si convertano nel giusto valore.
6 - Infine si crei un sottodataset che contenga solo i primi 100 record
"""
import pandas as pd

url = "https://raw.githubusercontent.com/fivethirtyeight/data/master/nba-elo/nbaallelo.csv"
nba = pd.read_csv(url)

# PUNTO 1
print(nba.head())
print(nba.tail(10))

# PUNTO 2
print(nba.info())
print(nba.describe())

# PUNTO 3
print(nba.shape)


# PUNTO 4
"""
NO
gameIdMask = nba["game_id"] == "NaN"
print(gameIdMask.head(20))
"""
nba["game_id"] = nba["game_id"].replace(["194611010TRH"], "NaN")
nba["game_id"] = nba["game_id"].replace(["194611020CHS"], "NaN")
nba["game_id"] = nba["game_id"].replace(["194611020DTF"], "NaN")
nba["game_id"] = nba["game_id"].replace(["194611020PRO"], "NaN")
nba["game_id"] = nba["game_id"].replace(["194611020STB"], "NaN")
nba["game_id"] = nba["game_id"].replace(["194611030CLR"], "NaN")
nba["game_id"] = nba["game_id"].replace(["194611040PIT"], "NaN")
nba["game_id"] = nba["game_id"].replace(["194611050BOS"], "NaN")
nba["game_id"] = nba["game_id"].replace(["194611050DTF"], "NaN")
nba["game_id"] = nba["game_id"].replace(["194611070GSW"], "NaN")

print(nba["game_id"].head(20))

# PUNTO 5
nba["game_id"] = nba["game_id"].astype('category')
nba["lg_id"] = nba["lg_id"].astype('category')
nba["date_game"] = pd.to_datetime(nba["date_game"])
nba["team_id"] = nba["team_id"].astype('category')
nba["fran_id"] = nba["fran_id"].astype('category')
nba["opp_id"] = nba["opp_id"].astype('category')
nba["opp_fran"] = nba["opp_fran"].astype('category')
nba["game_location"] = nba["game_location"].astype('category')
nba["game_result"] = nba["game_result"].astype('category')
nba["notes"] = nba["notes"].astype('category')

print(nba.dtypes)

# PUNTO 6
nbaNew = nba.head(100)
print(nbaNew)

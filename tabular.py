import pandas as pd
from tabulate import tabulate

df = pd.read_csv(open("GFG.csv", encoding="utf8"))

df2 = df[df.genre == 'metal']
df3 = df[df.genre == 'blues']
df4 = df[df.genre == 'dance']
df5 = df[df.genre == 'jazz']
frames = [df2, df3, df4, df5]
result = pd.concat(frames)
req = result[['track', 'artist', 'spotify_id']]
final = req.sample(n=21)
print(tabulate(final, headers = 'keys', tablefmt = 'psql'))

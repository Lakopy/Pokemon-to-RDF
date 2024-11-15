import pandas as pd 

df = pd.read_csv('pokemon.csv', encoding='utf-8')

df_new = df

df_new['forme'] = df_new['forme'].str.replace(" ", "")
df_new['forme'] = df_new['forme'].str.replace("%", "Percent")
df_new.rename(columns={'percemt-male': 'percentmale', 'percent-female': 'percentfemale', 'pre-evolution': 'preevolution', 'egg-group1': 'egggroup1', 'egg-group2': 'egggroup2'}, inplace=True)

df.to_csv('pokemon_clean.csv', index=False)
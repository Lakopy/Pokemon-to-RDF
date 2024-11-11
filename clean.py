import pandas as pd

df = pd.read_csv(r'C:\Users\joako\Documents\Tareas\watos\proyecto\movesets.csv')

for i in range(1, 175):
    column_name = f'move{i}'
    if column_name in df.columns:  # Verificar que la columna existe en el DataFrame
        df[column_name] = df[column_name].str.replace(r'^.*? - ', '', regex=True)


df.to_csv(r'C:\Users\joako\Documents\Tareas\watos\proyecto\moveset2.csv', index=False)


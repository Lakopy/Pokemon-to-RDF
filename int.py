import pandas as pd

df = pd.read_csv(r'C:\Users\joako\Documents\Tareas\watos\proyecto\moveset2.csv')
if 'ndex' in df.columns:
    df['ndex'] = df['ndex'].fillna(0).astype(int)

output_path = r'C:\Users\joako\Documents\Tareas\watos\proyecto\movesets3.csv'
df.to_csv(output_path, index=False)

print(f"Archivo modificado guardado en: {output_path}")

import pandas as pd

df = pd.read_csv('./Pokemon-to-RDF/movesets2.csv')
if 'ndex' in df.columns:
    df['ndex'] = df['ndex'].fillna(0).astype(int)

output_path = './Pokemon-to-RDF/movesets3.csv'
df.to_csv(output_path, index=False)


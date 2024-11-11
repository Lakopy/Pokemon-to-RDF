# Pokémon Movesets RDF Conversion

This branch uses the **Movesets** dataset from [Kaggle](https://www.kaggle.com/datasets/mylesoneill/pokemon-sun-and-moon-gen-7-stats?select=movesets.csv), which contains Pokémon movesets data up to Generation 7. The goal of this branch is to clean and transform this dataset into an RDF format, making it accessible for semantic web applications and SPARQL queries.

## Process Overview

1. **Data Cleaning**:
   - The `clean.py` and `int.py` scripts preprocess the movesets data, handling inconsistencies or missing values as needed.

2. **RDF Transformation**:
   - After cleaning, the `rdf.py` script converts the data into RDF format, generating `movesets.ttl`, a Turtle file with moveset information for all 802 Pokémon (including Mega Evolutions and regional forms).

## Files

- **movesets.csv**: The original dataset containing movesets for Generation 7 Pokémon.
- **clean.py** and **int.py**: Scripts for preprocessing and cleaning the raw data.
- **rdf.py**: The script used to convert the cleaned data into RDF format.
- **movesets.ttl**: The resulting RDF file containing the complete moveset information for each Pokémon.

## Usage

1. First run `clean.py` and then `int.py` to preprocess `movesets.csv`.
2. Execute `rdf.py` to generate `movesets.ttl` in RDF format.

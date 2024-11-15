# Pokémon Movesets RDF Conversion

This branch uses the **Movesets** dataset from [Kaggle](https://www.kaggle.com/datasets/mylesoneill/pokemon-sun-and-moon-gen-7-stats?select=movesets.csv), which contains Pokémon movesets data up to Generation 7. The goal of this branch is to clean and transform this dataset into an RDF format, making it accessible for semantic web applications and SPARQL queries.

## Process Overview

1. **Data Cleaning**:
   - The `clean.py` and `int.py` scripts preprocess the movesets data.

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
=======
# Linked Data Project: Pokémon Dataset to RDF

This repository contains a project for the course **"The Web of Data" (Linked Data)** from the Faculty of Physical and Mathematical Sciences at the University of Chile. The project involves converting three datasets obtained from Kaggle into RDF format, enabling data querying using Semantic Web technologies and SPARQL.

## Project Overview

The project focuses on representing data related to Pokémon and their moves up to Generation 7 in RDF format. By converting the datasets into RDF, we make it possible to perform complex queries on Pokémon data, such as finding moves of a specific type learned by a particular Pokémon or retrieving all Pokémon that can learn a certain move.

## Datasets

The following datasets from Kaggle are used in this project:

- **pokemon.csv**: General information on Pokémon species and attributes (source: [pokemon.csv on Kaggle](https://www.kaggle.com/datasets/mylesoneill/pokemon-sun-and-moon-gen-7-stats?select=pokemon.csv))
- **moves.csv**: Detailed information on moves available to Pokémon (source: [moves.csv on Kaggle](https://www.kaggle.com/datasets/mylesoneill/pokemon-sun-and-moon-gen-7-stats?select=moves.csv))
- **movesets.csv**: Movesets associated with each Pokémon species (source: [movesets.csv on Kaggle](https://www.kaggle.com/datasets/mylesoneill/pokemon-sun-and-moon-gen-7-stats?select=movesets.csv))

## Tools and Technologies

This project utilizes tools from the Semantic Web, allowing data to be structured in RDF format and queried using SPARQL. The RDF files generated from these datasets enable queries of interest, including:

- **Example Queries**:
  - Finding moves of a specific type that a certain Pokémon can learn.
  - Retrieving all Pokémon capable of learning a particular move.

## Usage

Instructions for running the data conversion scripts and performing SPARQL queries are included in this repository. 

This project demonstrates the application of Linked Data principles in organizing and querying structured Pokémon data.

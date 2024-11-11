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

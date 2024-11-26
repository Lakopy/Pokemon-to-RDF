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


## Queries

This section lists the SPARQL queries included in the project, along with a brief description of their functionality.

### List of Queries

1. **Strongest STAB Attack**
   - Finds the Pokémon with the strongest Same-Type Attack Bonus (STAB) moves, considering their effective power based on stats and move category.

2. **Fastest Support Pokémon**
   - Identifies the fastest Pokémon with support moves (Status category) and lists all their moves.

3. **Hazard Removal Pokémon**
   - Lists Pokémon capable of using moves to remove entry hazards (e.g., Defog, Rapid Spin).

4. **Top Coverage Pokémon**
   - Finds the Pokémon with the highest type coverage based on the variety of move types they can use.

5. **Tankiest Pokémon**
   - Determines the Pokémon with the highest combined HP, Defense, and Special Defense.

6. **Pokémon with the Most Moves**
   - Identifies the Pokémon with the largest number of distinct moves available in their moveset.

7. **Pokémon with Priority Moves**
   - Lists Pokémon that can use priority moves, ordered by the highest priority.

8. **Faster Pokémon**
   - Identifies Pokémon that are faster than a specific Pokémon (e.g., Pikachu).

9. **Abilities by Move Usage**
   - Finds Pokémon with specific abilities (e.g., Sturdy) that can use a specified move (e.g., Self-Destruct).

10. **Compatibility of Pokémon and Moves**
    - Lists Fire-type Pokémon that can learn Grass-type moves.

11. **Find Pokémon by Move**
    - Identifies Pokémon that can use a specific move (e.g., Trick Room).

12. **First Partner Pokémon**
    - Lists starter Pokémon with abilities like Overgrow, Blaze, or Torrent, ordered by National Dex number.

### How to Use

1. Install **Apache Jena Fuseki** on your machine.
2. Upload the `merge.ttl` file as the dataset in the Fuseki server.
3. Use the queries from `queries.txt` to interact with the dataset via the Fuseki query interface.

Enjoy exploring the data!

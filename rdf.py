import csv
from rdflib import Graph, URIRef, Literal, Namespace, RDF, XSD

EX = Namespace("http://example.org/")

g = Graph()
g.bind("ex", EX)

with open(r"C:\Users\joako\Documents\Tareas\watos\proyecto\movesets3.csv", newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        pokemon_uri = URIRef(EX + "pokemon/" + row['forme'].replace(" ", "_"))

        moveset_uri = URIRef(EX + "moveset/" + row['ndex'] + "/" + row['forme'].replace(" ", "_"))
        g.add((moveset_uri, RDF.type, EX.Moveset))
        g.add((moveset_uri, EX.forPokemon, pokemon_uri))

        for i in range(1, 175):
            move_column = f"move{i}"
            move_name = row.get(move_column)
            if move_name: 
                move_uri = URIRef(EX + "move/" + move_name.replace(" ", "_"))
                g.add((moveset_uri, EX.moves, move_uri))

with open("movesets.ttl", "w") as f:
    f.write(g.serialize(format="turtle"))

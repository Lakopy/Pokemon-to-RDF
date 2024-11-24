with open('merge.ttl', 'w', encoding='utf-8') as merge:

  with open('moves.ttl', 'r', encoding='utf-16') as moves:
    merge.write('# MOVES\n')
    for line in moves:
      merge.write(line)

  with open('pokemon.ttl', 'r', encoding='utf-16') as pokemon:
    merge.write('# POKEMON\n')
    for line in pokemon:
      merge.write(line)

  
  with open('movesets.ttl', 'r', encoding='utf-8') as movesets:
    merge.write('# MOVESETS\n')
    for line in movesets:
      merge.write(line)

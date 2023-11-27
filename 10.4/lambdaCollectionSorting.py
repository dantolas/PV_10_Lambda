vysledky = [
    ("Karel", 31),
    ("Petr", 10),
    ("Honza", 52),
    ("Eva", 61),
    ("Katka", 0),
]

print(sorted(vysledky,key= lambda soutezici:soutezici[1]))
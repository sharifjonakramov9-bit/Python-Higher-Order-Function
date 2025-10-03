from pprint import pprint

people = [
  {"name": "Ali", "age": 25},
  {"name": "Sami", "age": 19},
  {"name": "Lola", "age": 31}
]

x = sorted(people, key=lambda p: p["age"], reverse=True)

pprint(list(x))


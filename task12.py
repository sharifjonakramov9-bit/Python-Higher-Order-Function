students = [
  {"name": "Aziz", "grade": 89},
  {"name": "Kamola", "grade": 95},
  {"name": "Javlon", "grade": 76}
]

x = sorted(students, key=lambda s: s["grade"], reverse=True)

print(x)

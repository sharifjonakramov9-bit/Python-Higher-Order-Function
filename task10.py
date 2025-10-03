text = ["apple", "34", "banana", "100", "abc", "75"]

x = filter(
    lambda t: t.isdigit(),
    text
)

print(list(x))

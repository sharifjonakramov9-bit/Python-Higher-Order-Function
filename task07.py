prices = ["$120", "$340", "$50", "$90"]

x = map(
    lambda p: p.replace("$", ""),
    prices
)

print(list(x))


products = [
    {
        "name": "samsung s22",
        "price": 310,
        "quantity": 6
    },
    {
        "name": "samsung s23",
        "price": 350,
        "quantity": 4
    },
    {
        "name": "samsung s24",
        "price": 430,
        "quantity": 3
    },
]

x = filter(
    lambda products: (products["price"] * products["quantity"]) > 1450,
    products
)

print(list(x))

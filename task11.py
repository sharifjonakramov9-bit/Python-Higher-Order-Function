nums = list(range(1, 21))

x = filter(
    lambda n: n % 2 == 0,
    nums
)

print(list(x))

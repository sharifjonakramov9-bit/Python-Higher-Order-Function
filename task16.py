data = [123, "apple", "banana", "cat", 456, "mango", "elephant"]

x = filter(
    lambda d: len(d) > 5,
    data
)

print(list(x))
# tushunmadim
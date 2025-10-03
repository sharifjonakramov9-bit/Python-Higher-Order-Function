emails = ["ali@gmail.com", "vali@yahoo.com", "sami@gmail.com", "bek@outlook.com"]

x = filter(
    lambda e: e.endswith("gmail.com"),
    emails
)

print(list(x))

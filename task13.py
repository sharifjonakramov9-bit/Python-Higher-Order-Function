sentence = "Functional programming in Python is very powerful and elegant"

idk = sentence.split()
x = sorted(idk, key=len, reverse=True)[:3]

print(x)

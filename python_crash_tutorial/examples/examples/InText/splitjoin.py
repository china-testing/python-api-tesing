# splitjoin.py

print('"Hello, world.".split() =', "Hello, world.".split())

print('"123-45---6".split("-") =', "123-45---6".split("-"))

print('"  First      Last ".split() =', "  First      Last ".split())

print('"".join(["one", "two", "three"]) =', "".join(["one", "two", "three"]))

print('" ".join(["one", "two", "three"]) =', " ".join(["one", "two", "three"]))


print(list("mouse"))

s = "Hello, world?"
print(s)
chars = list(s)
chars[-1] = "!"
s = "".join(chars)
print(s)

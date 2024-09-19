from functools import reduce

vowels = ["a", "e", "i", "o", "u"]

s = input().lower()

print(reduce(lambda x, y: x if y in vowels else f"{x}.{y}", s, ""))

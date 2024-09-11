input()
words = input().split(" ")
tem = words[0]
for word in words[1:]:
    if len(f"{tem} {word}") <= 80:
        tem += f" {word}"
    else:
        print(tem)
        tem = word
print(tem)

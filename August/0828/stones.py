input()

pre_color = "P"
count = 0

for s in input():
    if (s == pre_color):
        count += 1
    pre_color = s

print(count)

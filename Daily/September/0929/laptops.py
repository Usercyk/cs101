laptops = []
for _ in range(int(input())):
    laptops.append(tuple(map(int, input().split())))

laptops.sort()

for i in range(len(laptops)-1):
    if laptops[i][0]==laptops[i+1][0]:
        continue
    if laptops[i][1]>laptops[i+1][1]:
        print("Happy Alex")
        break
else:
    print("Poor Alex")
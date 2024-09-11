y = int(input())
print("Y" if y % 4 == 0 and (y % 100 != 0 or y % 400 == 0) else "N")

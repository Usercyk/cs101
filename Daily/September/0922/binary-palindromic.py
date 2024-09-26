s = bin(int(input()))[2:]
print("Yes" if s == "".join(reversed(s)) else "No")

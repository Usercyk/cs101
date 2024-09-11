s = input()
n = int(s, 2)
m = n ^ (((1 << len(s))) - 1)

flag_n = (n & n << 1 & n << 2 & n << 3 & n << 4 & n << 5 & n << 6) != 0
flag_m = (m & m << 1 & m << 2 & m << 3 & m << 4 & m << 5 & m << 6) != 0

print("YES" if flag_n or flag_m else "NO")

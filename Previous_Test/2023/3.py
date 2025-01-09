from math import floor, log2


s = input()
n = len(s)
m = floor(log2(n))
ans = ""
for i in range(m+1):
    ans += s[2**i-1]+s[2**(m-i)-1]
ans = ans[:m+1]
print(ans)
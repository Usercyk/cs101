k = int(input()) % 26
s = input()
res = ""
for c in s:
    if c.islower():
        res += chr(ord("a")+(ord(c)-ord("a")-k) % 26)
    else:
        res += chr(ord("A")+(ord(c)-ord("A")-k) % 26)
print(res)

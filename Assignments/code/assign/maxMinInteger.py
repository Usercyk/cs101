_, s, = input(), input().split()
max_len = max(len(p) for p in s)
s.sort(key=lambda x: x*(__import__("math").ceil(2*max_len/len(x))), reverse=True)
print("".join(s), "".join(reversed(s)))

input()
nums = map(int, input().split())
cur = -1
length = 0
max_length = 0
for n in nums:
    if n >= cur:
        length += 1
    else:
        length = 1
    if length > max_length:
        max_length = length
    cur = n

print(max_length)

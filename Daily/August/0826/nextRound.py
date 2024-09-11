n, k = map(int, input().split())
finishers = map(int, input().split())

cur_score = 1000
advancers = 0

for f in finishers:
    if (f == 0):
        break
    elif (f == cur_score):
        advancers += 1
    else:
        if (advancers >= k):
            break
        advancers += 1
        cur_score = f

print(advancers)

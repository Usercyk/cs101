# constants
MAXD = int(1e9+7)
# input
n, d = map(int, input().split())
# input lst
# use removed to mark, instead of truly remove the value
lst = []
removed = []
removed_total = 0
for _ in range(n):
    lst.append(int(input()))
    removed.append(0)

# if lst is empty, just finish
while removed_total < n:
    # find all numbers that can swap to the 1st place
    # just sort swapable later
    swapable = []

    # mark the minimum and maximum, instead of using min or max method
    preMin = MAXD
    preMax = -MAXD

    for i in range(len(lst)):
        # if it is removed before, just pass this, instead of truly remove the value
        if removed[i]:
            continue

        # update the minimum and maximum
        # obviously, lst[i]-d <= lst[i] <= lst[i]+d
        preMin = min(preMin, lst[i])
        preMax = max(preMax, lst[i])

        # check if it is swapable
        if preMax-d <= lst[i] <= preMin+d:
            # add to the swapable list, sort and print later
            swapable.append(lst[i])
            # mark it is removed
            removed[i] = 1
            removed_total += 1

    # print the sorted swapable
    print(*sorted(swapable), sep="\n")

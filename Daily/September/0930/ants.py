for _ in range(int(input())):
    l, _ = map(int, input().split())
    ants = map(int, input().split())
    mins = []
    maxs = []
    for ant in ants:
        mins.append(min(ant, l-ant))
        maxs.append(max(ant, l-ant))
    print(max(mins), max(maxs))

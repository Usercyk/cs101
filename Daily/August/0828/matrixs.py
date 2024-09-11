for i in range(5):
    s = input().split(" ")
    try:
        j = s.index("1")
        print(abs(i-2)+abs(j-2))
    except:
        continue

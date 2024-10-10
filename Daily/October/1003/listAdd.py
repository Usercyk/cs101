def modifiedInput(rev=False):
    input()
    _dict = {}
    _map = map(int, input().split())
    for p in _map:
        try:
            _dict[p] += 1
        except:
            _dict[p] = 1
    _set = sorted(_dict.keys(), reverse=rev)
    _len = len(_set)
    return _dict, _set, _len


for _ in range(int(input())):
    s = int(input())

    a_dict, a_set, a_len = modifiedInput()

    b_dict, b_set, b_len = modifiedInput(True)

    i, j, res = 0, 0, 0
    while i < a_len and j < b_len:
        if a_set[i]+b_set[j] > s:
            j += 1
            continue
        if a_set[i]+b_set[j] < s:
            i += 1
            continue
        res += a_dict[a_set[i]]*b_dict[b_set[j]]
        i += 1
        j += 1
    print(res)
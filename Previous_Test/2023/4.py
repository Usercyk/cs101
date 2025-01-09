def dfs(blocks, word, step, used):
    if step == len(word):
        return "YES"
    for i in range(4):
        if word[step] in blocks[i]:
            if not used[i]:
                used[i] = True
                if dfs(blocks, word, step+1, used) == "YES":
                    return "YES"
                used[i] = False
    return "NO"


N = int(input())
blocks = [set(input()) for _ in range(4)]
for _ in range(N):
    word = input()
    used = [False]*4
    print(dfs(blocks, word, 0, used))

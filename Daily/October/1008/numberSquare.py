# 0<=5z-3y,2x+3y-5z,5z-2x<=n
# 5z max

n = int(input())
for z in range(3*n//5+1, n//5-1, -1):
    for y in range(5*z//3+1, (5*z-n)//3-1, -1):
        for x in range(5*z//2+1, (5*z-n)//2-1, -1):
            if 0 <= 2*x+3*y-5*z <= n and 0 <= 5*z-3*y <= n and 0 <= 5*z-2*x <= n:
                print(5*z)
                exit()

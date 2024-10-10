n, l = map(int, input().split())
a = sorted(map(int, input().split()))
diff = (a[i+1]-a[i] for i in range(len(a)-1))
print(max(*diff, 2*a[0], 2*(l-a[-1]))/2)

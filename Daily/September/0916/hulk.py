n = int(input())
if n%2==1:
    print("I hate that I love that " * (n//2) + "I hate it")
else:
    print("I hate that I love that " * (n//2-1) + "I hate that I love it")
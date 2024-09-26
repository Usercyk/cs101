from datetime import date, timedelta

day = date.fromisoformat(input())
res = day+timedelta(days=int(input()))

print(res.isoformat())

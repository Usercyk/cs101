from datetime import date
for _ in range(int(input())):
    s = input()
    print(date.fromisoformat(f"{s[:4]}-{s[4:6]}-{s[6:]}").strftime("%A"))

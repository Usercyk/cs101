import re

pattern = r"^[^@|.](?!.*@.*@)(?!(.*@\.))(?!(.*\.@))(?=.*@)(?=(.*@.*\..*)).*[^@|.]$"

while True:
    try:
        case = input().strip()
        if re.match(pattern, case):
            print("YES")
        else:
            print("NO")
    except EOFError:
        break

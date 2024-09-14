from functools import reduce
print(reduce(lambda x, y: x+y.lower() if y.isupper()
      else x+y.upper() if y.islower() else x+y, input(), ""))

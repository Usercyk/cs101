roman = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}


def romanToArabic(r):
    r = r.replace("CM", "DCD").replace("CD", "CCCC").replace("XC", "LXL").replace(
        "XL", "XXXX").replace("IX", "VIV").replace("IV", "IIII")
    return (sum(roman[p] for p in r))


def arabicToRoman(a):
    r: str = a//1000 * "M"+a % 1000//500 * "D"+a % 500//100*"C" + \
        a % 100//50 * "L"+a % 50//10 * "X"+a % 10//5*"V"+a % 5*"I"
    r = r.replace("IIII", "IV").replace("VIV", "IX").replace("XXXX", "XL").replace(
        "LXL", "XC").replace("CCCC", "CD").replace("DCD", "CM")
    return r


s = input()
if s[0] in roman:
    print(romanToArabic(s))
else:
    print(arabicToRoman(int(s)))

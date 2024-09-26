left_2x2_in_3x3 = [0, 5, 3, 1]
while True:
    s = input().strip()
    if s == "0 0 0 0 0 0":
        break
    res = 0
    a = list(map(int, s.split()))
    # 装入6，5，4，1个1箱；装入3，4个1箱
    res += a[5]+a[4]+a[3]+(a[2]+3)//4
    # 装入2
    left_2x2 = a[3]*5+left_2x2_in_3x3[a[2] % 4]
    if a[1] > left_2x2:
        res += (a[1]-left_2x2+8)//9
    # 装入1
    left_1x1 = 36*res-36*a[5]-25*a[4]-16*a[3]-9*a[2]-4*a[1]
    if a[0] > left_1x1:
        res += (a[0]-left_1x1+35)//36
    print(res)

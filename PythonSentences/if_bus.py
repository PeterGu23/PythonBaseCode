left_money = int(input("请刷卡："))
num = int(input("看看还有几个空位："))
if left_money > 2:
    print ("你可以乘坐本次班车！")
    if num > 0:
        print ("你可以坐下！")
    else :
        print ("没有座位了！")
else:
    print ("你不可以坐本次班车！")



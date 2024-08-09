"""  条件语句（if、elif、else） """
""" if 条件1:
    # 当条件1为真时执行的代码块
    pass
elif 条件2:
    # 当条件1为假且条件2为真时执行的代码块
    pass
else:
    # 当所有条件都为假时执行的代码块
    pass """
import sys

sys.stdout.reconfigure(encoding='utf-8')
x = 10
if x > 5:
    print("x 大于 5")
x = 3
if x > 5:
    print("x 大于 5")
else:
    print("x 小于或等于 5")

x = 0
if x > 0:
    print("x 是正数")
elif x < 0:
    print("x 是负数")
else:
    print("x 是零")

x = 10
y = 5
if x > 5:
    if y > 5:
        print("x 和 y 都大于 5")
    else:
        print("x 大于 5，但 y 小于或等于 5")
else:
    print("x 小于或等于 5")

x = 10
y = 5
if x > 5 and y > 5:
    print("x 和 y 都大于 5")
elif x > 5 or y > 5:
    print("x 或 y 大于 5")
else:
    print("x 和 y 都小于或等于 5")

   

print("你好，世界")


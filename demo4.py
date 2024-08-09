""" 循环（for、while） """
import sys

sys.stdout.reconfigure(encoding='utf-8')

""" for 变量 in 序列:
    # 循环体
    pass """
# 遍历列表
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

# 遍历字符串
for char in "hello":
    print(char)

# 使用range函数
for i in range(5):
    print(i)  # 输出: 0 1 2 3 4
""" 
 while 条件:
    # 循环体
    pass
 """
# 基本while循环
count = 0
while count < 5:
    print(count)
    count += 1

# 无限循环
# while True:
#     print("This is an infinite loop")

for i in range(10):
    if i == 5:
        break
    print(i)  # 输出: 0 1 2 3 4

for i in range(10):
    if i % 2 == 0:
        continue
    print(i)  # 输出: 1 3 5 7 9

for i in range(3):
    for j in range(2):
        print(f"i={i}, j={j}")

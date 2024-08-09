""" 函数 """
import sys

sys.stdout.reconfigure(encoding='utf-8')

""" def 函数名(参数1, 参数2, ...):
    # 函数体
    return 返回值
 """
def greet():
    print("Hello, World!")

greet()  # 调用函数

def greet(name):
    print(f"Hello, {name}!")

greet("Alice")  # 调用函数

def add(a, b):
    return a + b

result = add(3, 5)
print(result)  # 输出: 8

def greet(name="World"):
    print(f"Hello, {name}!")

greet()  # 输出: Hello, World!
greet("Alice")  # 输出: Hello, Alice!


def sum_all(*args):
    total = 0
    for num in args:
        total += num
    return total

result = sum_all(1, 2, 3, 4)
print(result)  # 输出: 10

def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_info(name="Alice", age=25)
# 输出:
# name: Alice
# age: 25

add = lambda a, b: a + b
result = add(3, 5)
print(result)  # 输出: 8



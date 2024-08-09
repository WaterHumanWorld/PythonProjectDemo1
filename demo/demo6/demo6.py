""" 模块和包 """
import sys

sys.stdout.reconfigure(encoding='utf-8')

import mymodule

mymodule.greet("Alice")  # 输出: Hello, Alice!
result = mymodule.add(3, 5)
print(result)  # 输出: 8
print(mymodule.my_variable)  # 输出: 10


from mymodule import greet, add

greet("Alice")  # 输出: Hello, Alice!
result = add(3, 5)
print(result)  # 输出: 8


import mypackage.mymodule

mypackage.mymodule.greet("Alice")  # 输出: Hello, Alice!
result = mypackage.mymodule.add(3, 5)
print(result)  # 输出: 8
print(mypackage.mymodule.my_variable)  # 输出: 10

from mypackage.mymodule import greet, add

greet("Alice")  # 输出: Hello, Alice!
result = add(3, 5)
print(result)  # 输出: 8


#内置模块
import math

print(math.pi)  # 输出: 3.141592653589793
print(math.sqrt(16))  # 输出: 4.0

#4. 第三方模块
import requests

response = requests.get("https://www.example.com")
print(response.text)

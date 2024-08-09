import sys

sys.stdout.reconfigure(encoding='utf-8')

def add(x, y):
    """加法函数"""
    return x + y

def subtract(x, y):
    """减法函数"""
    return x - y

def multiply(x, y):
    """乘法函数"""
    return x * y

def divide(x, y):
    """除法函数"""
    if y != 0:
        return x / y
    else:
        return "错误：除数不能为零"

def main():
    print("选择操作：")
    print("1. 加法")
    print("2. 减法")
    print("3. 乘法")
    print("4. 除法")

    while True:
        choice = input("请输入你的选择(1/2/3/4): ")

        if choice in ['1', '2', '3', '4']:
            num1 = float(input("输入第一个数字: "))
            num2 = float(input("输入第二个数字: "))

            if choice == '1':
                print(f"{num1} + {num2} = {add(num1, num2)}")

            elif choice == '2':
                print(f"{num1} - {num2} = {subtract(num1, num2)}")

            elif choice == '3':
                print(f"{num1} * {num2} = {multiply(num1, num2)}")

            elif choice == '4':
                print(f"{num1} / {num2} = {divide(num1, num2)}")

            next_calculation = input("是否继续计算？(yes/no): ")
            if next_calculation.lower() != 'yes':
                break
        else:
            print("无效输入，请重新输入")

if __name__ == "__main__":
    main()

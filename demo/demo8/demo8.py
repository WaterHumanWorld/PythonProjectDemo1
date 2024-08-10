#打包成 windows   图形化.exe
# 标准图形化 库 使用 库学习
import tkinter as tk

def say_hello():
    print("Hello, World!")

root = tk.Tk()
root.title("Tkinter Example")

hello_button = tk.Button(root, text="Say Hello", command=say_hello)
hello_button.pack()

root.mainloop()

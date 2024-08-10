import tkinter as tk

def say_hello():
    print("Hello, World!")

root = tk.Tk()
root.title("Tkinter Example")
root.geometry("300x200")

label = tk.Label(root, text="欢迎使用Tkinter")
label.pack()

hello_button = tk.Button(root, text="Say Hello", command=say_hello)
hello_button.pack()

entry = tk.Entry(root)
entry.pack()

text = tk.Text(root)
text.pack()

var = tk.IntVar()
checkbutton = tk.Checkbutton(root, text="选择我", variable=var)
checkbutton.pack()

var_radio = tk.IntVar()
radiobutton1 = tk.Radiobutton(root, text="选项1", variable=var_radio, value=1)
radiobutton2 = tk.Radiobutton(root, text="选项2", variable=var_radio, value=2)
radiobutton1.pack()
radiobutton2.pack()

listbox = tk.Listbox(root)
listbox.pack()
listbox.insert(tk.END, "选项1")
listbox.insert(tk.END, "选项2")

menu = tk.Menu(root)
root.config(menu=menu)
file_menu = tk.Menu(menu)
menu.add_cascade(label="文件", menu=file_menu)
file_menu.add_command(label="打开", command=say_hello)

root.mainloop()

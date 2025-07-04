import tkinter as tk

window = tk.Tk()
window.title("Basic Calculator")
window.geometry("320x450")
window.configure(bg="#222")

expression = ""

def press(num):
    global expression
    expression += str(num)
    equation.set(expression)

def clear():
    global expression
    expression = expression[:-1]
    equation.set(expression)

def reset():
    global expression
    expression = ""
    equation.set("")

def equal():
    global expression
    try:
        total = str(eval(expression))
        equation.set(total)
        expression = total
    except:
        equation.set("Error")
        expression = ""

equation = tk.StringVar()

entry_field = tk.Entry(window, textvariable=equation, font=('Arial', 20), bd=10, insertwidth=2,
                       width=14, borderwidth=4, justify='right', bg="#ddd")
entry_field.grid(row=0, column=0, columnspan=4, pady=20)

def create_button(text, row, col, cmd=None, color="#333", fg="white", colspan=1):
    return tk.Button(window, text=text, padx=20, pady=20, bd=5, fg=fg, bg=color,
                     font=('Arial', 14), command=cmd or (lambda: press(text))
                    ).grid(row=row, column=col, columnspan=colspan, sticky="nsew")

create_button('7', 1, 0)
create_button('8', 1, 1)
create_button('9', 1, 2)
create_button('/', 1, 3)

create_button('4', 2, 0)
create_button('5', 2, 1)
create_button('6', 2, 2)
create_button('*', 2, 3)

create_button('1', 3, 0)
create_button('2', 3, 1)
create_button('3', 3, 2)
create_button('-', 3, 3)

create_button('0', 4, 0)
create_button('.', 4, 1)
create_button('C', 4, 2, cmd=clear, color="#e67e22")   
create_button('+', 4, 3)

create_button('Reset', 5, 0, cmd=reset, color="#c0392b", colspan=2)  
create_button('=', 5, 2, cmd=equal, color="#27ae60", colspan=2)     

for i in range(6):
    window.grid_rowconfigure(i, weight=1)
for j in range(4):
    window.grid_columnconfigure(j, weight=1)

window.mainloop()

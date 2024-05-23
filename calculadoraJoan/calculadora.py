import tkinter as tk

def press(key):
    exp.insert(tk.END, key)
    
def clear():
    exp.delete(0, tk.END)
    
def calculate():
    result = eval(exp.get())
    exp.delete(0, tk.END)
    exp.insert(tk.END, result)

root = tk.Tk()
root.title("Calculadora")

exp = tk.Entry(root, width=30, borderwidth=5)
exp.grid(row=0, column=0, columnspan=4)

buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    'C', '0', '=', '+'
]

row = 1
col = 0
for button in buttons:
    if button == '=':
        tk.Button(root, text=button, command=calculate).grid(row=row, column=col)
    elif button == 'C':
        tk.Button(root, text=button, command=clear).grid(row=row, column=col)
    else:
        tk.Button(root, text=button, command=lambda b=button: press(b)).grid(row=row, column=col)
    col += 1
    if col > 3:
        col = 0
        row += 1

root.mainloop()
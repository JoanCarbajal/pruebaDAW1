import tkinter as tk

# Función para manejar la entrada y operaciones
def click(event):
    text = event.widget.cget("text")
    if text == "=":
        try:
            result = str(eval(entry_var.get()))
            entry_var.set(result)
        except Exception as e:
            entry_var.set("Error")
    elif text == "C":
        entry_var.set("")
    else:
        entry_var.set(entry_var.get() + text)

# Crear la ventana principal
root = tk.Tk()
root.title("Calculadora")

# Variable para la entrada
entry_var = tk.StringVar()

# Crear el cuadro de entrada
entry = tk.Entry(root, textvar=entry_var, font=('Arial', 18), bd=10, insertwidth=4, width=14, borderwidth=4, relief='ridge')
entry.grid(row=0, column=0, columnspan=4)

# Crear botones
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    'C', '0', '=', '+'
]

# Configurar los botones en la cuadrícula
row_val = 1
col_val = 0
for button in buttons:
    btn = tk.Button(root, text=button, font=('Arial', 18), bd=5, padx=10, pady=10)
    btn.grid(row=row_val, column=col_val, padx=5, pady=5)
    btn.bind("<Button-1>", click)
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

# Iniciar el bucle principal de la aplicación
root.mainloop()

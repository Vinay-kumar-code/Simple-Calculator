# Simple Calculator with GUI in Python
import tkinter as tk
from tkinter import messagebox

def on_button_click(value):
    current = entry.get()
    if value == "C":
        entry.delete(0, tk.END)
    elif value == "=":
        try:
            result = eval(current)
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(result))
        except Exception as e:
            messagebox.showerror("Error", "Invalid calculation.")
    else:
        entry.insert(tk.END, value)

root = tk.Tk()
root.title("Simple GUI Python Calculator")

entry = tk.Entry(root, width=20, font=("Arial", 18), bd=5, insertwidth=4, justify='right')
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Button layout
buttons = [
    ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
    ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
    ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
    ("C", 4, 0), ("0", 4, 1), ("=", 4, 2), ("+", 4, 3),
]

for (text, row, col) in buttons:
    button = tk.Button(root, text=text, padx=20, pady=20, font=("Arial", 18),
                       command=lambda t=text: on_button_click(t))
    button.grid(row=row, column=col, padx=5, pady=5)

root.mainloop()

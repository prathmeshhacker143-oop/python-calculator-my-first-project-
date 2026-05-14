import tkinter as tk
from math import *
import cmath

root = tk.Tk()
root.title("Advanced Engineering Calculator")
root.geometry("520x760")
root.configure(bg="#0f172a")

equation = ""
history = []

display = tk.Entry(
    root,
    font=("Arial", 26),
    bd=0,
    justify="right",
    bg="#e2e8f0",
    fg="black"
)

display.pack(fill="both", padx=15, pady=15, ipady=20)

history_box = tk.Text(
    root,
    height=6,
    bg="#1e293b",
    fg="white",
    font=("Arial", 12)
)

history_box.pack(fill="both", padx=15, pady=5)

def press(value):
    global equation
    equation += str(value)
    display.delete(0, tk.END)
    display.insert(tk.END, equation)

def clear():
    global equation
    equation = ""
    display.delete(0, tk.END)

def backspace():
    global equation
    equation = equation[:-1]
    display.delete(0, tk.END)
    display.insert(tk.END, equation)

def calculate():
    global equation

    try:
        result = str(eval(equation))

        history.append(f"{equation} = {result}")
        history_box.insert(tk.END, f"{equation} = {result}\n")

        display.delete(0, tk.END)
        display.insert(tk.END, result)

        equation = result

    except:
        display.delete(0, tk.END)
        display.insert(tk.END, "Error")
        equation = ""

def to_binary():
    global equation
    try:
        result = bin(int(eval(equation)))
        display.delete(0, tk.END)
        display.insert(tk.END, result)
        equation = result
    except:
        display.insert(tk.END, " Error")

def to_hex():
    global equation
    try:
        result = hex(int(eval(equation)))
        display.delete(0, tk.END)
        display.insert(tk.END, result)
        equation = result
    except:
        display.insert(tk.END, " Error")

def factorial_calc():
    global equation
    try:
        result = factorial(int(eval(equation)))
        display.delete(0, tk.END)
        display.insert(tk.END, result)
        equation = str(result)
    except:
        display.insert(tk.END, " Error")

btn_style = {
    "font": ("Arial", 14),
    "bg": "#334155",
    "fg": "white",
    "bd": 0,
    "width": 6,
    "height": 2,
    "activebackground": "#475569"
}

frame = tk.Frame(root, bg="#0f172a")
frame.pack()

buttons = [
    ('7',1,0), ('8',1,1), ('9',1,2), ('/',1,3), ('sqrt(',1,4), ('C',1,5),
    ('4',2,0), ('5',2,1), ('6',2,2), ('*',2,3), ('pi',2,4), ('⌫',2,5),
    ('1',3,0), ('2',3,1), ('3',3,2), ('-',3,3), ('e',3,4), ('%',3,5),
    ('0',4,0), ('.',4,1), ('+',4,2), ('(',4,3), (')',4,4), ('=',4,5),
    ('sin(',5,0), ('cos(',5,1), ('tan(',5,2), ('log10(',5,3), ('log(',5,4), ('pow(',5,5),
    ('asin(',6,0), ('acos(',6,1), ('atan(',6,2), ('degrees(',6,3), ('radians(',6,4), ('exp(',6,5),
    ('x²',7,0), ('x³',7,1), ('!',7,2), ('BIN',7,3), ('HEX',7,4), ('j',7,5),
]

for (text,row,col) in buttons:

    if text == 'C':
        btn = tk.Button(frame, text=text, command=clear,
                        bg="#ef4444", fg="white",
                        font=("Arial",14), width=6, height=2)

    elif text == '⌫':
        btn = tk.Button(frame, text=text, command=backspace,
                        bg="#f59e0b", fg="white",
                        font=("Arial",14), width=6, height=2)

    elif text == '=':
        btn = tk.Button(frame, text=text, command=calculate,
                        bg="#22c55e", fg="white",
                        font=("Arial",14), width=6, height=2)

    elif text == 'x²':
        btn = tk.Button(frame, text=text,
                        command=lambda: press("**2"), **btn_style)

    elif text == 'x³':
        btn = tk.Button(frame, text=text,
                        command=lambda: press("**3"), **btn_style)

    elif text == '!':
        btn = tk.Button(frame, text=text,
                        command=factorial_calc, **btn_style)

    elif text == 'BIN':
        btn = tk.Button(frame, text=text,
                        command=to_binary, **btn_style)

    elif text == 'HEX':
        btn = tk.Button(frame, text=text,
                        command=to_hex, **btn_style)

    elif text == 'j':
        btn = tk.Button(frame, text=text,
                        command=lambda: press("j"), **btn_style)

    else:
        btn = tk.Button(frame, text=text,
                        command=lambda t=text: press(t),
                        **btn_style)

    btn.grid(row=row, column=col, padx=4, pady=4)

root.mainloop()
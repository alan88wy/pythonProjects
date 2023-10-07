# Calculator v3

'''
Simple calculator using tkinter.

To run:
    
    python calculator_inter.py
'''

import tkinter as tk
import math

nominator = ""
denominator = ""
operator = ""
calculation = ""
current_input= ""

    
def add_to_calculation(symbol):

    global nominator
    global denominator
    global operator
    global calculation
    global current_input 
    
    symbol = str(symbol)
    
    if symbol == "+/-":
        if current_input != "":
            if current_input[0] == "-":
                current_input = current_input[1:]
            else:
                current_input = '-' + current_input

    elif symbol == '%':
        
        if current_input != "":
            current_input = str(eval(nominator + "*" + current_input + "/ 100"))
        else:
            clear_field()
            delete_result()
    elif symbol == "CE":
        current_input = ""
    elif symbol == 'C':
        clear_field()
        delete_result()
    elif symbol in "+-*/":
        if nominator != "" and operator != "" and current_input != "":
            denominator = current_input
            current_input = ""
            calculate()
            
        if current_input != "":
            nominator = current_input
            operator = symbol
            denominator = ""
            current_input = ""
    elif symbol == "=":
        calculate_result()
    elif symbol == "1/x":
        if current_input in "+-/*" or current_input == "0" or current_input == "":
            clear_field()
            current_input = ""
            delete_result()
            insert_result(1.0, "Invalid denominator!")
            return
        
        if (current_input.isdigit()):
            current_input = str(1/int(current_input))
        else:
            current_input = str(1/float(current_input))
        
    elif symbol == "sqrt":
        if current_input in "+-/*" or current_input == "0" or current_input == "":
            clear_field()
            current_input = ""
            delete_result()
            insert_result(1.0, "Invalid value!")
            return

        if (current_input.isdigit()):
            current_input = str(math.sqrt(int(current_input)))
        else:
            current_input = str(math.sqrt(float(current_input)))
        
    elif symbol == "x2":
        if current_input in "+-/*" or current_input == "0" or current_input == "":
            clear_field()
            current_input = ""
            delete_result()
            insert_result(1.0, "Invalid value!")
            return
        
        if (current_input.isdigit()):
            current_input = str(int(current_input)**2)
        else:
            current_input = str(float(current_input)**2)
        
    else: # 0-9
        current_input += symbol
        
    show_calculation()
    
def calculate():
    global nominator
    global denominator
    global operator
    global calculation
    global current_input
       
    try:
        res = str(eval(nominator + operator + denominator))
        nominator = ""
        denominator = ""
        operator = ""
        current_input = res
        calculation=res
        delete_result()
        insert_result(1.0, res)
    except:
        clear_field()
        current_input = ""
        delete_result()
        insert_result(1.0, "ERROR")
            
def calculate_result():
    global nominator
    global denominator
    global operator
    global calculation
    global current_input        
    
    if current_input == "":
        if nominator == "":
            clear_field()
            delete_result()
        elif operator == "/":
            print_error("Divid by zero")
            return
        else:
            denominator = ""
            operator = ""
    elif nominator == "":
        nominator = current_input
        denominator = ""
        operator = ""
    else:
        denominator = current_input
        current_input = ""
                
    calculate()
    
#     current_input = ""

def clear_field():
    global nominator
    global denominator
    global operator
    global calculation
    global current_input
    
    nominator = ""
    denominator = ""
    operator = ""
    calculation = ""
    current_input = ""
    
def delete_result():
    result.config(state="normal")
    result.delete(1.0, "end")
    result.config(state="disabled")
    
def insert_result(pos = "1.0", res=""):
    result.config(state="normal")
    result.insert(pos, res)
    result.config(state="disabled")
    
def print_error(msg="ERROR"):
    clear_field()
    insert_result(msg)

def show_calculation():
    
    global nominator
    global denominator
    global operator
    global current_input
    
    res = nominator + operator + current_input
    
    if res == "":
        res = "0"
        
    delete_result()
    insert_result(1.0, res)
    insert_result("end", "\n")   # put a line break to advance to line 2
#     inp.insert('end', "Line 2")  # insert line 2

#     inp.get(1.0, '2.0 -1 chars')  # To get Line 1
#     inp.get(2.0, 'end - 1 chars') # To get Line 2

def key_press(a): 
    global nominator
    global denominator
    global operator
    global current_input
    
    if a.keysym == "Delete" or a.keysym == "C" or a.keysym =="c":
        clear_field()
        delete_result()
    elif a.keysym == "Return" or a.char == "=":
        calculate_result()
    elif a.keysym == "BackSpace":
        if current_input != "":
            current_input = current_input[:-1]
            if current_input == "":
                current_input = ""
        elif operator != "":
            operator = ""
        elif nominator != "":
            nominator = nominator[:-1]
        else:
            current_input = ""
        show_calculation()
    elif a.char in "0123456789.+-*/%":
        add_to_calculation(a.char)
        
root = tk.Tk()
root.geometry("600x600")
root.title("Calculator")

# Binding keypad

for i in range(10):
    root.bind(str(i), key_press)
    
for i in "+-*/=.%":
    root.bind(str(i), key_press)
    
root.bind('<Delete>', key_press)
root.bind('<Return>', key_press)
root.bind('<BackSpace>', key_press)
root.bind("c", key_press)
root.bind("C", key_press)

# label = tk.Label(root, text="Calculator", font=('Arial', 16))
# label.pack(padx=20, pady=1)

result = tk.Text(root, height=1, font=('Arial', 72))
result.pack(padx=10, pady=8)
insert_result(1.0, "0")

# button = tk.Button(root, text='Click Me !', font=('Arial', 18))
# button.pack(padx=10, pady=10)

buttonframe = tk.Frame(root)
buttonframe.columnconfigure(0, weight=1)
buttonframe.columnconfigure(1, weight=1)
buttonframe.columnconfigure(2, weight=1)
buttonframe.columnconfigure(3, weight=1)

btn_width=5
btn_height=2
btn_font=('Arial', 18)
btn_relief = "groove"

btn1 = tk.Button(buttonframe, text='%', width=btn_width, height=btn_height, font=btn_font, relief=btn_relief, command=lambda: add_to_calculation('%'))
btn1.grid(row=0, column=0, sticky=tk.W+tk.E) # can also use 'news' = north, east, west, south

btn2 = tk.Button(buttonframe, text='CE', width=btn_width, height=btn_height, font=btn_font, relief=btn_relief, command=lambda: add_to_calculation('CE'))
btn2.grid(row=0, column=1, sticky=tk.W+tk.E)

btn3 = tk.Button(buttonframe, text='C', width=btn_width, height=btn_height, font=btn_font, relief=btn_relief, command=lambda: add_to_calculation('C'))
btn3.grid(row=0, column=2, sticky=tk.W+tk.E)

btn4 = tk.Button(buttonframe, text=bytes([246]).decode('cp437'), width=btn_width, height=btn_height, font=btn_font, relief=btn_relief, command=lambda: add_to_calculation('/'))
btn4.grid(row=0, column=3, sticky=tk.W+tk.E)

btn5 = tk.Button(buttonframe, text='¹/x', width=btn_width, height=btn_height, font=btn_font, relief=btn_relief, command=lambda: add_to_calculation('1/x'))
btn5.grid(row=1, column=0, sticky=tk.W+tk.E) # can also use 'news' = north, east, west, south

btn6 = tk.Button(buttonframe, text="x" + bytes([253]).decode('cp437'), width=btn_width, height=btn_height, font=btn_font, relief=btn_relief, command=lambda: add_to_calculation('x2'))
btn6.grid(row=1, column=1, sticky=tk.W+tk.E)

btn7 = tk.Button(buttonframe, text=bytes([253]).decode('cp437') + bytes([251]).decode('cp437')+'x', width=btn_width, height=btn_height, font=btn_font, relief=btn_relief, command=lambda: add_to_calculation('sqrt'))
btn7.grid(row=1, column=2, sticky=tk.W+tk.E)

btn8 = tk.Button(buttonframe, text=bytes([246]).decode('cp437'), width=btn_width, height=btn_height, font=btn_font, relief=btn_relief, command=lambda: add_to_calculation('/'))
btn8.grid(row=1, column=3, sticky=tk.W+tk.E)

btn9 = tk.Button(buttonframe, text='7', width=btn_width, height=btn_height, font=btn_font, relief=btn_relief, command=lambda: add_to_calculation(7))
btn9.grid(row=2, column=0, sticky=tk.W+tk.E)

btn10 = tk.Button(buttonframe, text='8', width=btn_width, height=btn_height, font=btn_font, relief=btn_relief, command=lambda: add_to_calculation(8))
btn10.grid(row=2, column=1, sticky=tk.W+tk.E)

btn11 = tk.Button(buttonframe, text='9', width=btn_width, height=btn_height, font=btn_font, relief=btn_relief, command=lambda: add_to_calculation(9))
btn11.grid(row=2, column=2, sticky=tk.W+tk.E)

btn12 = tk.Button(buttonframe, text='x', width=btn_width, height=btn_height, font=btn_font, relief=btn_relief, command=lambda: add_to_calculation('*'))
btn12.grid(row=2, column=3, sticky=tk.W+tk.E)

btn13 = tk.Button(buttonframe, text='4', width=btn_width, height=btn_height, font=btn_font, relief=btn_relief, command=lambda: add_to_calculation(4))
btn13.grid(row=3, column=0, sticky=tk.W+tk.E)

btn14 = tk.Button(buttonframe, text='5', width=btn_width, height=btn_height, font=btn_font, relief=btn_relief, command=lambda: add_to_calculation(5))
btn14.grid(row=3, column=1, sticky=tk.W+tk.E)

btn15 = tk.Button(buttonframe, text='6', width=btn_width, height=btn_height, font=btn_font, relief=btn_relief, command=lambda: add_to_calculation(6))
btn15.grid(row=3, column=2, sticky=tk.W+tk.E)

btn16 = tk.Button(buttonframe, text=chr(45), width=btn_width, height=btn_height, font=btn_font, relief=btn_relief, command=lambda: add_to_calculation('-'))
btn16.grid(row=3, column=3, sticky=tk.W+tk.E)

btn17 = tk.Button(buttonframe, text='1', width=btn_width, height=btn_height, font=btn_font, relief=btn_relief, command=lambda: add_to_calculation(1))
btn17.grid(row=4, column=0, sticky=tk.W+tk.E)  

btn18 = tk.Button(buttonframe, text='2', width=btn_width, height=btn_height, font=btn_font, relief=btn_relief, command=lambda: add_to_calculation(2))
btn18.grid(row=4, column=1, sticky=tk.W+tk.E)

btn19 = tk.Button(buttonframe, text='3', width=btn_width, height=btn_height, font=btn_font, relief=btn_relief, command=lambda: add_to_calculation(3))
btn19.grid(row=4, column=2,  sticky=tk.W+tk.E)

btn20 = tk.Button(buttonframe, text=chr(43), width=btn_width, height=btn_height, font=btn_font, relief=btn_relief, command=lambda: add_to_calculation('+'))
btn20.grid(row=4, column=3,  sticky=tk.W+tk.E)

btn21 = tk.Button(buttonframe, text='+/-', width=btn_width, height=btn_height, font=btn_font, relief=btn_relief, command=lambda: add_to_calculation('+/-'))
btn21.grid(row=5, column=0, sticky=tk.W+tk.E)  # can also use 'news' = north, east, west, south

btn22 = tk.Button(buttonframe, text='0', width=btn_width, height=btn_height, font=btn_font, relief=btn_relief, command=lambda: add_to_calculation(0))
btn22.grid(row=5, column=1, sticky=tk.W+tk.E)

btn23 = tk.Button(buttonframe, text='.', width=btn_width, height=btn_height, font=btn_font, relief=btn_relief, command=lambda: add_to_calculation('.'))
btn23.grid(row=5, column=2,  sticky=tk.W+tk.E)

btn24 = tk.Button(buttonframe, text='=', width=btn_width, height=btn_height, font=btn_font, relief=btn_relief, command=calculate_result)
btn24.grid(row=5, column=3,  sticky=tk.W+tk.E)

buttonframe.pack(padx=10, pady=10, fill=tk.X)  # can also use fill='x'

show_calculation()

root.mainloop()
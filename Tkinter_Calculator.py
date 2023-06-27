# Import packages
from tkinter import *
from customtkinter import *
import tkinter.messagebox
import math
import numpy as np

'''
Functions
'''
# Function to add in the entry of text display
def button_click(char):
    global calc_operator
    calc_operator += str(char)
    text_input.set(calc_operator)

# Function to clear the whole entry of text display
def button_clear_all():
    global calc_operator
    calc_operator = ""
    text_input.set("")

# Function to delete one by one from the last in the entry of text display
def button_delete():
    global calc_operator
    text = calc_operator[:-1]
    calc_operator = text
    text_input.set(text)

# Function to calculate the factorial of a number
def factorial(n):
    if n==0 or n==1:
        return 1
    else:
        return n*factorial(n-1)

def fact_func():
    global calc_operator
    try:
        result = str(factorial(int(calc_operator)))
        calc_operator = result
        text_input.set(result)
    except Exception as e:
        tkinter.messagebox.showinfo("Error"," ".join(str(e).split()[:2]))
        button_clear_all()

# Function to calculate trigonometric numbers of an angle
def trig_sin():
    global calc_operator
    try:
        result = str(math.sin(math.radians(int(eval(calc_operator)))))
        calc_operator = result
        text_input.set(result)
    except Exception as e:
        tkinter.messagebox.showinfo("Error"," ".join(str(e).split()[:2]))
        button_clear_all()

def trig_cos():
    try:
        global calc_operator
        result = str(math.cos(math.radians(int(eval(calc_operator)))))
        calc_operator = result
        text_input.set(result)
    except Exception as e:
        tkinter.messagebox.showinfo("Error"," ".join(str(e).split()[:2]))
        button_clear_all()
def trig_tan():
    try:
        global calc_operator
        result = str(math.tan(math.radians(int(eval(calc_operator)))))
        calc_operator = result
        text_input.set(result)
    except Exception as e:
        tkinter.messagebox.showinfo("Error"," ".join(str(e).split()[:2]))
        button_clear_all()

def trig_cot():
    try:
        global calc_operator
        result = str(1/math.tan(math.radians(int(eval(calc_operator)))))
        calc_operator = result
        text_input.set(result)
    except Exception as e:
        tkinter.messagebox.showinfo("Error"," ".join(str(e).split()[:2]))
        button_clear_all()

# Function to find the square root of a number
def square_root():
    global calc_operator
    if int(calc_operator)>=0:
        temp = str(eval(calc_operator+'**(1/2)'))
        calc_operator = temp
        text_input.set(temp)
    else:
        tkinter.messagebox.showinfo("Error","Invalid Input")
        button_clear_all()

# Function to find the third root of a number
def third_root():
    global calc_operator
    if int(calc_operator)>=0:
        temp = str(eval(calc_operator+'**(1/3)'))
        calc_operator = temp
        text_input.set(temp)
    else:
        tkinter.messagebox.showinfo("Error","Invalid Input")
        button_clear_all()

# Function to change the sign of number
def sign_change():
    global calc_operator
    if(len(calc_operator)==0):
        return
    if calc_operator[0]=='-':
        temp = calc_operator[1:]
    else:
        temp = '-'+calc_operator
    calc_operator = temp
    text_input.set(temp)    

# Function to calculate the percentage of a number
def percent():
    global calc_operator
    try:
        temp = str(eval(calc_operator+'/100'))
        calc_operator = temp
        text_input.set(temp)
    except Exception as e:
        tkinter.messagebox.showinfo("Error"," ".join(str(e).split()[:2]))
        button_clear_all()

# Funtion to find the result of an operation
def button_equal():
    try:
        global calc_operator
        temp_op = str(eval(calc_operator))
        text_input.set(temp_op)
        calc_operator = temp_op
    except Exception as e:
        tkinter.messagebox.showinfo("Error"," ".join(str(e).split()[:4]))
        button_clear_all()

'''
Variables
'''
sin, cos, tan = math.sin, math.cos, math.tan
log, ln = math.log10, math.log
e = math.exp
p = math.pi
E = '*10**'

tk_calc = CTk()
# tk_calc.configure(bg="#293C4A", bd=10)
tk_calc.title("Scientific Calculator")
tk_calc.resizable(0,0)

calc_operator = ""
text_input = StringVar()

text_display = CTkEntry(tk_calc, font=('sans-serif', 20, 'bold'), textvariable=text_input,insertwidth = 5, justify='right',
                        width=350,height=40).grid(columnspan=5, pady = 10)

'''
Buttons
'''
#--1st row--
# Absolute value of a number
abs_value = CTkButton(tk_calc, font=('sans-serif', 20, 'bold'), text='abs',width=80,
                   command=lambda:button_click('abs(')).grid(row=1, column=0,padx=5,pady=5,sticky="nsew")
# Remainder of a division
modulo = CTkButton(tk_calc, font=('sans-serif', 20, 'bold'), text='mod',width=80,
                command=lambda:button_click('%')).grid(row=1, column=1, padx=5,pady=5,sticky="nsew")
# Integer division quotient
int_div = CTkButton(tk_calc, font=('sans-serif', 20, 'bold'), text='div',width=80,
                 command=lambda:button_click('//')).grid(row=1, column=2, padx=5,pady=5,sticky="nsew")
# Factorial of a number
factorial_button = CTkButton(tk_calc, font=('sans-serif', 20, 'bold'), text='x!',width=80,
                   command=fact_func).grid(row=1, column=3, padx=5,pady=5,sticky="nsew")
# Euler's number e
eulers_num = CTkButton(tk_calc, font=('sans-serif', 20, 'bold'), text='e',width=80,
                    command=lambda:button_click(str(math.exp(1)))).grid(row=1, column=4, padx=5,pady=5,sticky="nsew")

#--2nd row--
# Sine of an angle in degrees
sine = CTkButton(tk_calc, font=('sans-serif', 20, 'bold'), text='sin',width=80,
             command=trig_sin).grid(row=2, column=0, padx=5,pady=5,sticky="nsew")
# Cosine of an angle in degrees
cosine = CTkButton(tk_calc, font=('sans-serif', 20, 'bold'), text='cos',width=80,
             command=trig_cos).grid(row=2, column=1, padx=5,pady=5,sticky="nsew")
# Tangent of an angle in degrees
tangent = CTkButton(tk_calc, font=('sans-serif', 20, 'bold'), text='tan',width=80,
             command=trig_tan).grid(row=2, column=2, padx=5,pady=5,sticky="nsew")
# Cotangent of an angle in degrees
cotangent = CTkButton(tk_calc, font=('sans-serif', 20, 'bold'), text='cot',width=80,
             command=trig_cot).grid(row=2, column=3, padx=5,pady=5,sticky="nsew")
# Pi(3.14...) number 
pi_num = CTkButton(tk_calc, font=('sans-serif', 20, 'bold'), text='π',width=80,
                command=lambda:button_click(str(math.pi))).grid(row=2, column=4,padx=5,pady=5, sticky="nsew")

#--3rd row--
# Power of 2
second_power = CTkButton(tk_calc, font=('sans-serif', 20, 'bold'), text='x\u00B2',width=80,
             command=lambda:button_click('**2')).grid(row=3, column=0, padx=5,pady=5,sticky="nsew")
# Power of 3
third_power = CTkButton(tk_calc, font=('sans-serif', 20, 'bold'), text='x\u00B3',width=80,
             command=lambda:button_click('**3')).grid(row=3, column=1, padx=5,pady=5,sticky="nsew")
# Power of n
nth_power = CTkButton(tk_calc, font=('sans-serif', 20, 'bold'), text='x^n',width=80,
             command=lambda:button_click('**')).grid(row=3, column=2, padx=5,pady=5,sticky="nsew")
# Inverse number
inv_power = CTkButton(tk_calc, font=('sans-serif', 20, 'bold'), text='x\u207b\xb9',width=80,
             command=lambda:button_click('**(-1)')).grid(row=3, column=3,padx=5,pady=5, sticky="nsew")
# Powers of 10
tens_powers = CTkButton(tk_calc, font=('sans-serif', 15, 'bold'), text='10^x',width=80,
                     command=lambda:button_click('10**')).grid(row=3, column=4,padx=5,pady=5, sticky="nsew")

#--4th row--
# Square root of a number
square_root = CTkButton(tk_calc, font=('sans-serif', 20, 'bold'), text='\u00B2\u221A',width=80,
                     command=square_root).grid(row=4, column=0, padx=5,pady=5,sticky="nsew")
# Third root of a number
third_root = CTkButton(tk_calc, font=('sans-serif', 20, 'bold'), text='\u00B3\u221A',width=80,
                    command=third_root).grid(row=4, column=1, padx=5,pady=5,sticky="nsew")
# nth root of a number
nth_root = CTkButton(tk_calc, font=('sans-serif', 20, 'bold'), text='\u221A',width=80,
                  command=lambda:button_click('**(1/')).grid(row=4, column=2, padx=5,pady=5,sticky="nsew")
# Logarithm of a number with base 10
log_base10 = CTkButton(tk_calc, font=('sans-serif', 16, 'bold'), text='log\u2081\u2080',width=80,
                   command=lambda:button_click('log(')).grid(row=4, column=3, padx=5,pady=5,sticky="nsew")
# Logarithm of a number with base e (ln)
log_basee = CTkButton(tk_calc, font=('sans-serif', 20, 'bold'), text='ln',width=80,
                   command=lambda:button_click('ln(')).grid(row=4, column=4, padx=5,pady=5,sticky="nsew")

#--5th row--
# Add a left parentheses
left_par = CTkButton(tk_calc, font=('sans-serif', 20, 'bold'), text='(',width=80,
                  command=lambda:button_click('(')).grid(row=5, column=0, padx=5,pady=5,sticky="nsew")
# Add a right parentheses
right_par = CTkButton(tk_calc, font=('sans-serif', 20, 'bold'), text=')',width=80,
                   command=lambda:button_click(')')).grid(row=5, column=1, padx=5,pady=5,sticky="nsew")   
# Change the sign of a number
signs = CTkButton(tk_calc, font=('sans-serif', 20, 'bold'), text='\u00B1',width=80,
               command=sign_change).grid(row=5, column=2, padx=5,pady=5,sticky="nsew")
# Transform number to percentage
percentage = CTkButton(tk_calc, font=('sans-serif', 20, 'bold'), text='%',width=80,
               command=percent).grid(row=5, column=3, padx=5,pady=5,sticky="nsew")
# Calculate the function e^x
ex = CTkButton(tk_calc, font=('sans-serif', 20, 'bold'), text='e^x',width=80,
               command=lambda:button_click('e(')).grid(row=5, column=4, padx=5,pady=5,sticky="nsew")

#--6th row--
button_7 = CTkButton(tk_calc, font=('sans-serif', 20, 'bold'), text='7',width=80,
                  command=lambda:button_click('7')).grid(row=6, column=0, padx=5,pady=5,sticky="nsew")
button_8 = CTkButton(tk_calc, font=('sans-serif', 20, 'bold'), text='8',width=80,
                  command=lambda:button_click('8')).grid(row=6, column=1, padx=5,pady=5,sticky="nsew")
button_9 = CTkButton(tk_calc, font=('sans-serif', 20, 'bold'), text='9',width=80,
                  command=lambda:button_click('9')).grid(row=6, column=2, padx=5,pady=5,sticky="nsew")
delete_one = CTkButton(tk_calc, font=('sans-serif', 20, 'bold'),width=80,
              text='DEL', command=button_delete).grid(row=6, column=3, padx=5,pady=5,sticky="nsew")
delete_all = CTkButton(tk_calc, font=('sans-serif', 20, 'bold'),width=80,
              text='AC', command=button_clear_all).grid(row=6, column=4, padx=5,pady=5,sticky="nsew")

#--7th row--
button_4 = CTkButton(tk_calc, font=('sans-serif', 20, 'bold'), text='4',width=80,
                  command=lambda:button_click('4')).grid(row=7, column=0, padx=5,pady=5,sticky="nsew")
button_5 = CTkButton(tk_calc, font=('sans-serif', 20, 'bold'), text='5',width=80,
                  command=lambda:button_click('5')).grid(row=7, column=1, padx=5,pady=5,sticky="nsew")
button_6 = CTkButton(tk_calc, font=('sans-serif', 20, 'bold'), text='6',width=80,
                  command=lambda:button_click('6')).grid(row=7, column=2, padx=5,pady=5,sticky="nsew")
mul = CTkButton(tk_calc, font=('sans-serif', 20, 'bold'), text='*',width=80,
             command=lambda:button_click('*')).grid(row=7, column=3, padx=5,pady=5,sticky="nsew")
div = CTkButton(tk_calc, font=('sans-serif', 20, 'bold'), text='/',width=80,
             command=lambda:button_click('/')).grid(row=7, column=4, padx=5,pady=5,sticky="nsew")

#--8th row--
button_1 = CTkButton(tk_calc, font=('sans-serif', 20, 'bold'), text='1',width=80,
                  command=lambda:button_click('1')).grid(row=8, column=0, padx=5,pady=5,sticky="nsew")
button_2 = CTkButton(tk_calc, font=('sans-serif', 20, 'bold'), text='2',width=80,
                  command=lambda:button_click('2')).grid(row=8, column=1, padx=5,pady=5,sticky="nsew")
button_3 = CTkButton(tk_calc, font=('sans-serif', 20, 'bold'), text='3',width=80,
                  command=lambda:button_click('3')).grid(row=8, column=2, padx=5,pady=5,sticky="nsew")
add = CTkButton(tk_calc, font=('sans-serif', 20, 'bold'), text='+',width=80,
             command=lambda:button_click('+')).grid(row=8, column=3, padx=5,pady=5,sticky="nsew")
sub = CTkButton(tk_calc, font=('sans-serif', 20, 'bold'), text='-',width=80,
             command=lambda:button_click('-')).grid(row=8, column=4, padx=5,pady=5,sticky="nsew")

#--9th row--
button_0 = CTkButton(tk_calc, font=('sans-serif', 20, 'bold'), text='0',width=80,
                  command=lambda:button_click('0')).grid(row=9, column=0, padx=5,pady=5,sticky="nsew")
point = CTkButton(tk_calc, font=('sans-serif', 20, 'bold'), text='.',width=80,
               command=lambda:button_click('.')).grid(row=9, column=1, padx=5,pady=5,sticky="nsew")
exp = CTkButton(tk_calc, font=('sans-serif', 16, 'bold'), text='EXP',width=80,
             command=lambda:button_click(E)).grid(row=9, column=2, padx=5,pady=5,sticky="nsew")
equal = CTkButton(tk_calc, font=('sans-serif', 20, 'bold'), text='=',width=160,
               command=button_equal).grid(row=9, columnspan=2, column=3, padx=5,pady=5,sticky="nsew")


tk_calc.mainloop()

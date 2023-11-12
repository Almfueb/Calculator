from tkinter import *
import math


window = Tk()
window.title("Calculator program")
window.geometry("500x550")
window.configure(bg="#423c3a")

equation_text = ""

equation_label = StringVar()

label = Label(window, textvariable=equation_label, font=('consolas',20), bg="white", width=27, height=2, bd=4, relief="ridge")
label.pack(pady=10)


frame = Frame(window)
frame.pack(pady=10)

def button_press(num):

    global equation_text
    if num == 'x':
        num = '*'
    elif num == '÷':
        num = '/'
    equation_label.set(equation_text)
    equation_text = equation_text + str(num)
    equation_label.set(equation_text)

def equals():

    global equation_text

    try:
        total = eval(equation_text)
        if isinstance(total, float):
            if total.is_integer():
                total = int(total)
            else:
                total = round(total, 2)
        equation_label.set(total)
        equation_text = str(total)

    except SyntaxError:
        equation_label.set("syntax error")
        equation_text = ""

    except ZeroDivisionError:
        equation_label.set("arithmetic error")
        equation_text = ""

def percent():
    global equation_text
    try:
        result = str(eval(equation_text) / 100)
        equation_label.set(result)
        equation_text = result
    except:
        equation_label.set("Error")
        equation_text = ""

def square_root():
    global equation_text
    try:
        result = math.sqrt(eval(equation_text))
        equation_label.set(result)
        equation_text = str(result)
    except:
        equation_label.set("Error")
        equation_text = ""

def factorial():
    global equation_text
    try:
        result = math.factorial(int(equation_text))
        equation_label.set(result)
        equation_text = str(result)
    except ValueError:
        equation_label.set("Invalid input for factorial")
    except Exception as e:
        equation_label.set("Error")
        equation_text = ""

def kuadrat():
    global equation_text
    try:
        result = eval(equation_text)**2
        equation_label.set(result)
        equation_text = str(result)
    except:
        equation_label.set("Error")
        equation_text = ""

def log():
    global equation_text
    try:
        result = math.log10(eval(equation_text))
        if result.is_integer():
            result = int(result)
        equation_label.set(result)
        equation_text = str(result)
    except ValueError:
        equation_label.set("Invalid input for logarithm")
    except:
        equation_label.set("Error")
        equation_text = ""

def In():
    global equation_text
    try:
        result = math.log(eval(equation_text))
        if result.is_integer():
            result = int(result)
        equation_label.set(result)
        equation_text = str(result)
    except ValueError:
        equation_label.set("Invalid input for logarithm")
    except:
        equation_label.set("Error")
        equation_text = ""

def PI():
    pi_value = math.pi
    equation_label.set(pi_value)
    equation_text = str(pi_value)






def clear_label():

    global equation_text
    equation_label.set("")
    equation_text = ""

def backspace():
    global equation_text
    equation_text = equation_text[:-1]
    equation_label.set(equation_text)

def evaluate(event=None):
    equals()

def key_press(event):
    if event.char.isdigit()or event.char in ['+', '-', 'x', '/', '.', '%', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0']:
        button_press(event.char)

    elif event.keysym == 'BackSpace':
        backspace()

    elif event.keysym == 'Return':
        evaluate()

    elif event.keysym == 'Escape':
        clear_label()

    elif event.keysym == 'c':
        quit()


window.bind("<Key>", key_press)

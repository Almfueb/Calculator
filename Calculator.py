from tkinter import *

def button_press(num):

    global equation_text
    if num == 'x':
        num = '*'
    elif num == '÷':
        num = '/'
    equation_text = equation_text + str(num)
    equation_label.set(equation_text)

def equals():

    global equation_text

    try:

        total = str(eval(equation_text))
        equation_label.set(total)
        equation_text = total

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


window = Tk()
window.title("Calculator program")
window.geometry("500x550")

equation_text = ""

equation_label = StringVar()

label = Label(window, textvariable=equation_label, font=('consolas',20), bg="white", width=27, height=2, bd=4, relief="ridge")
label.pack(pady=10)


frame = Frame(window)
frame.pack(pady=10)

window.bind("<Key>", key_press)

button1 = Button(frame, text=1, height=4, width=9, font=35,command=lambda: button_press(1))
button1.grid(row=0, column=0)

button2 = Button(frame, text=2, height=4, width=9, font=35,command=lambda: button_press(2))
button2.grid(row=0, column=1)

button3 = Button(frame, text=3, height=4, width=9, font=35,command=lambda: button_press(3))
button3.grid(row=0, column=2)

button4 = Button(frame, text=4, height=4, width=9, font=35,command=lambda: button_press(4))
button4.grid(row=1, column=0)

button5 = Button(frame, text=5, height=4, width=9, font=35,command=lambda: button_press(5))
button5.grid(row=1, column=1)

button6 = Button(frame, text=6, height=4, width=9, font=35,command=lambda: button_press(6))
button6.grid(row=1, column=2)

button7 = Button(frame, text=7, height=4, width=9, font=35,command=lambda: button_press(7))
button7.grid(row=2, column=0)

button8 = Button(frame, text=8, height=4, width=9, font=35,command=lambda: button_press(8))
button8.grid(row=2, column=1)

button9 = Button(frame, text=9, height=4, width=9, font=35,command=lambda: button_press(9))
button9.grid(row=2, column=2)

button0 = Button(frame, text=0, height=4, width=9, font=35,command=lambda: button_press(0))
button0.grid(row=3, column=1)

plus = Button(frame, text='+', height=4, width=9, font=35,command=lambda: button_press('+'))
plus.grid(row=0, column=3)

minus = Button(frame, text='-', height=4, width=9, font=35,command=lambda: button_press('-'))
minus.grid(row=1, column=3)

multiply = Button(frame, text='x', height=4, width=9, font=35, command=lambda: button_press('x'))
multiply.grid(row=2, column=3)

divide = Button(frame, text='÷', height=4, width=9, font=35,command=lambda: button_press('/'))
divide.grid(row=3, column=3)

decimal = Button(frame, text='.', height=4, width=9, font=35,command=lambda: button_press('.'))
decimal.grid(row=3, column=0)

clear = Button(frame, text='clear', height=4, width=9, font=35,command=clear_label)
clear.grid(row=3, column=2)

percent = Button(frame, text='%', height=4, width=11, font=35, command=percent)
percent.grid(row=4, column=0, columnspan=2)

equal = Button(frame, text='=', height=4, width=11, font=35, command=equals)
equal.grid(row=4, column=2, columnspan=2)

window.mainloop()

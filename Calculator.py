from tkinter import *
from func import *
import math

button1 = Button(frame, text=1, height=4, width=9, bg="gray", fg="white",font=35,command=lambda: button_press(1))
button1.grid(row=1, column=1)

button2 = Button(frame, text=2, height=4, width=9, bg="gray", fg="white",font=35,command=lambda: button_press(2))
button2.grid(row=1, column=2)

button3 = Button(frame, text=3, height=4, width=9, bg="gray", fg="white",font=35,command=lambda: button_press(3))
button3.grid(row=1, column=3)

button4 = Button(frame, text=4, height=4, width=9, bg="gray", fg="white",font=35,command=lambda: button_press(4))
button4.grid(row=2, column=1)

button5 = Button(frame, text=5, height=4, width=9, bg="gray", fg="white",font=35,command=lambda: button_press(5))
button5.grid(row=2, column=2)

button6 = Button(frame, text=6, height=4, width=9, bg="gray", fg="white",font=35,command=lambda: button_press(6))
button6.grid(row=2, column=3)

button7 = Button(frame, text=7, height=4, width=9, bg="gray", fg="white",font=35,command=lambda: button_press(7))
button7.grid(row=3, column=1)

button8 = Button(frame, text=8, height=4, width=9, bg="gray", fg="white",font=35,command=lambda: button_press(8))
button8.grid(row=3, column=2)

button9 = Button(frame, text=9, height=4, width=9, bg="gray", fg="white",font=35,command=lambda: button_press(9))
button9.grid(row=3, column=3)

button0 = Button(frame, text=0, height=4, width=9, bg="gray", fg="white",font=35,command=lambda: button_press(0))
button0.grid(row=4, column=2)

plus = Button(frame, text='+', height=4, width=9, bg="#505050", fg="white",font=35,command=lambda: button_press('+'))
plus.grid(row=3, column=4)

minus = Button(frame, text='-', height=4, width=9, bg="#505050", fg="white",font=35,command=lambda: button_press('-'))
minus.grid(row=2, column=4)

multiply = Button(frame, text='x', height=4, width=9, bg="#505050", fg="white",font=35, command=lambda: button_press('*'))
multiply.grid(row=1, column=4)

divide = Button(frame, text='÷', height=4, width=9, bg="#505050", fg="white",font=35,command=lambda: button_press('/'))
divide.grid(row=3, column=0)

decimal = Button(frame, text=',', height=4, width=9, bg="#505050", fg="white",font=200,command=lambda: button_press(','))
decimal.grid(row=4, column=3)

clear = Button(frame, text='Clear', height=4, width=9, bg="#505050", fg="white",font=35,command=clear_label)
clear.grid(row=4, column=1)

percent = Button(frame, text='%', height=4, width=9, bg="#505050", fg="white",font=35, command=percent)
percent.grid(row=0, column=3)

equal = Button(frame, text='=', height=4, width=9, bg="#505050", fg="white",font=35, command=equals)
equal.grid(row=4, column=4)

delete_button = Button(frame, text='Delete', height=4, bg="#505050", fg="white",width=9, font=35, command=backspace)
delete_button.grid(row=0, column=4)

factorial_button = Button(frame, text='!', height=4, bg="#505050", fg="white",width=9, font=35, command=factorial)
factorial_button.grid(row=0, column=2)

kuadrat_button = Button(frame, text='^2', height=4, bg="#505050", fg="white",width=9, font=35, command=kuadrat)
kuadrat_button.grid(row=2, column=0)

sqrt_button = Button(frame, text='√', height=4, bg="#505050", fg="white",width=9, font=35, command=square_root)
sqrt_button.grid(row=1, column=0)

log_button = Button(frame, text='log', height=4, bg="#505050", fg="white",width=9, font=35, command=log)
log_button.grid(row=0, column=0)

log_button = Button(frame, text='In', height=4, bg="#505050", fg="white",width=9, font=35, command=In)
log_button.grid(row=0, column=1)

pi_button = Button(frame, text='π', height=4, bg="#505050", fg="white",width=9, font=35, command=PI)
pi_button.grid(row=4, column=0)

window.mainloop()

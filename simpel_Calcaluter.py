import tkinter as tk
from tkinter import *

# from numpy import equal

expression = ""
def press(num):
    global expression
    expression = expression + str(num)
    equation.set(expression)

def equalpress():
    try:
        global expression
        total = str(eval(expression))
        equation.set(total)
        expression = ""
    except:
        equation.set("error")
        expression = ""

def Clear():
    global expression
    expression = ""
    equation.set("")


    
    

# root = tk.Tk()
# root.title("Welcome to my calculator")
# search_box = tk.Canvas(root, width=400, height=200)
# search_box.pack()

if __name__ == "__main__":
    top = Tk()
    top.geometry("450x500") 
    top.title("My Calculator")
    equation= StringVar()
    expression_field = Entry(top, text="",textvariable=equation ,width=19, font=("Arial", 30))
    expression_field.place(x=12, y=20)
    btn_1 = Button(top, text="1",width=4, fg='white', bg='black',command=lambda: press(1), font=("Arial", 20))
    btn_1.place(x=15, y=110)
    btn_2 = Button(top, text="2",width=4, fg='white', bg='black',command=lambda: press(2), font=("Arial", 20))
    btn_2.place(x=95, y=110)
    btn_3 = Button(top, text="3",width=4, fg='white', bg='black',command=lambda: press(3), font=("Arial", 20))
    btn_3.place(x=175, y=110)
    btn_4 = Button(top, text="4",width=4, fg='white', bg='black',command=lambda: press(4), font=("Arial", 20))
    btn_4.place(x=15, y=170)
    btn_5 = Button(top, text="5",width=4, fg='white', bg='black',command=lambda: press(5), font=("Arial", 20))
    btn_5.place(x=95, y=170)
    btn_6 = Button(top, text="6",width=4, fg='white', bg='black',command=lambda: press(6), font=("Arial", 20))
    btn_6.place(x=175, y=170)
    btn_7 = Button(top, text="7",width=4, fg='white', bg='black',command=lambda: press(7), font=("Arial", 20))
    btn_7.place(x=15, y=230)
    btn_8 = Button(top, text="8",width=4, fg='white', bg='black',command=lambda: press(8), font=("Arial", 20))
    btn_8.place(x=95, y=230)
    btn_9 = Button(top, text="9",width=4,fg='white' ,bg='black',command=lambda: press(9), font=("Arial", 20))
    btn_9.place(x=175, y=230)
    btn_0 = Button(top, text="0",width=4, fg='white', bg='black',command=lambda: press(0), font=("Arial", 20))
    btn_0.place(x=15, y=290)
    btn_det = Button(top, text="00",width=4, fg='white', bg='black',command=lambda: press("00"), font=("Arial", 20))
    btn_det.place(x=95, y=290)
    btn_new_0 = Button(top, text=".",width=4, fg='white', bg='black',command=lambda: press("."), font=("Arial", 20))
    btn_new_0.place(x=175, y=290)
    btn_clear = Button(top, text="Clear",width=4, fg='white', bg='#f00',command=Clear, font=("Arial", 20))
    btn_clear.place(x=280, y=110)
    # btn_new_1 = Button(top, text="<=",width=4, fg='white', bg='black',command=Clear_one, font=("Arial", 20))
    # btn_new_1.place(x=280, y=170)
    # btn_new_1 = Button(top, text="",width=4, fg='white', bg='black',command=Clear, font=("Arial", 20))
    # btn_new_1.place(x=280, y=230)
    # btn_new_1 = Button(top, text="",width=4, fg='white', bg='black',command=Clear, font=("Arial", 20))
    # btn_new_1.place(x=280, y=290)
    btn_pl = Button(top, text="+",width=4, fg='white', bg='black',command=lambda: press("+"), font=("Arial", 20))
    btn_pl.place(x=360, y=110)
    btn_ne = Button(top, text="-",width=4, fg='white', bg='black',command=lambda: press("-"), font=("Arial", 20))
    btn_ne.place(x=360, y=170)
    btn_mu = Button(top, text="X",width=4, fg='white', bg='black',command=lambda: press("*"), font=("Arial", 20))
    btn_mu.place(x=360, y=230)
    btn = Button(top, text="/",width=4, fg='white', bg='black',command=lambda: press("/"), font=("Arial", 20))
    btn.place(x=360, y=290)
    btn_eq = Button(top, text="=",width=22, fg='white', bg='#f00',command=equalpress ,font=("Arial", 25))
    btn_eq.place(x=15, y=420)
    

    top.mainloop()
from cgitb import text
from tkinter import Button, Entry, Label, PhotoImage, StringVar, messagebox
import tkinter as tk
import random

root = tk.Tk()
root.title('Number Guessing Game')
root.geometry('600x410+250+150')


number = random.randint(1, 11)

def exit():
    root.quit()
    
def check_anwser():
    global number
    global user_hint
    
    user_input = int(enter_number.get())
    
    if user_input == number:
        user_hint.set('You Win')
        chack_button.pack_forget()
        
    elif user_input > number:
        user_hint.set('Number less kar plase')
    
    elif user_input < number:
        user_hint.set('Number Greater kar plase')
    
    else:
        user_hint.set('In cokrat')
    
    

game_back_img = PhotoImage(file='png.png')
game_back_imges = Label(root, image=game_back_img)
game_back_imges.place(x=0, y=0)

icon = PhotoImage(file='puzzle.png')
root.iconphoto(False, icon)

game_name = Label(root, text='Number Guessing Game', fg='#C0392B', font=('Arial', 25))
game_name.place(x=120, y=20)

game_range = Label(root, text='Range of Game 1 to 10', fg='#D35400', font=('Arial', 15))
game_range.place(x=210, y=80)

enter_number = Entry(root, bg='#566573', fg='White', font=('Arial', 16), bd=3)
enter_number.pack()
enter_number.place(x=170, y=130, width=290)

user_hint = StringVar()
user_hint.set('output Answer')
guess = Label(root, textvariable=user_hint, font=('arial', 18), fg='#C0392B')
guess.pack()
guess.place(y=200, x=210)

chack_button = Button(root, text='Chack', fg='white', bg='#A93226', font=('arial', 13), command=check_anwser)
chack_button.pack()
chack_button.place(x=250, y=260, width=120) 

exit_button = Button(root, text='EXIT', fg='white', bg='#A93226', font=('arial', 13), command=exit)
exit_button.pack()
exit_button.place(x=250, y=320, width=120)





if __name__=="__main__":
    root.mainloop()
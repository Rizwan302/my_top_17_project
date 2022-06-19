from tkinter import*
from tkinter import Tk
import tkinter as tk
from PIL import Image, ImageTk



running = False
hours, minutes, seconds = 0, 0, 0
    
def start():
    global running
    if not running:
        update()
        running = True

# pause function
def pause():
    global running
    if running:
        # cancel updating of time using after_cancel()
        stopwatch_label.after_cancel(update_time)
        running = False

# reset function
def reset():
    global running
    if running:
        # cancel updating of time using after_cancel()
        stopwatch_label.after_cancel(update_time)
        running = False
    # set variables back to zero
    global hours, minutes, seconds
    hours, minutes, seconds = 0, 0, 0
    # set label back to zero
    stopwatch_label.config(text='00:00:00')

# update stopwatch function
def update():
    # update seconds with (addition) compound assignment operator
    global hours, minutes, seconds
    seconds += 1
    if seconds == 60:
        minutes += 1
        seconds = 0
    if minutes == 60:
        hours += 1
        minutes = 0
    # format time to include leading zeros
    hours_string = f'{hours}' if hours > 9 else f'0{hours}'
    minutes_string = f'{minutes}' if minutes > 9 else f'0{minutes}'
    seconds_string = f'{seconds}' if seconds > 9 else f'0{seconds}'
    # update timer label after 1000 ms (1 second)
    stopwatch_label.config(text=hours_string + ':' + minutes_string + ':' + seconds_string)
    # after each second (1000 milliseconds), call update function
    # use update_time variable to cancel or pause the time using after_cancel
    global update_time
    update_time = stopwatch_label.after(1000, update)
    
    

    
    
    
    
if __name__=="__main__":
    root = tk.Tk()
    root.geometry("700x600")
    # root.configure(bg='black', width=50) 
    # -----------AppName My_stop_watch------------
    back= Label(root, text="", width=50, height=100, bg="black").place(x=0, y=0)
    app_name = Label(root, text="My Stop Watch", fg='red', font=('italic', 30)).place(x=220, y=55)
    
    # cir_img = Image.open("C:/Users/DELL/Desktop/opp/images1.png")
    # test= ImageTk.PhotoImage(cir_img)
    # label1 = tkinter.Label(image=test, font=("Arial", 1))
    # label1.image = test
    # label1.place(x=8, y=10, width=130, height=100)
    # fram = Frame(root, width=450, height=250, highlightbackground='black', highlightcolor="black", highlightthickness=1, bd=3).place(x=80, y=170)

    

    
    fram = Frame(root, width=340, height=110, highlightbackground='black', highlightcolor="black", highlightthickness=1, bd=3)
    fram.place(x=180, y=210)
    hour = Label(root, text="Hour", fg="red", bg='black', font=('Arial', 22)).place(x=183, y=170)
    minute = Label(root, text="Minut", fg="red", bg='black', font=('Arial', 22)).place(x=280, y=170)
    minute = Label(root, text="es", fg="red", bg='white', font=('Arial', 22)).place(x=355, y=170)
    second = Label(root, text="Seconds", fg="red", bg='white', font=('Arial', 22)).place(x=400, y=170)
    
    
    stopwatch_label = tk.Label(fram, text='00:00:00', fg='green', font=('Arial', 60))
    stopwatch_label.pack()
    stopwatch_label.place(x=8, y=0)
    
    but_start=tk.Button(root, text='START', fg='white', bg='red', font=('Arial', 18), command=start).place(x=179, y=360)
    but_stop=tk.Button(root, text='STOP', fg='white', bg='red', font=('Arial', 18), command=pause).place(x=310, y=360)
    but_reset=tk.Button(root, text='RESET', fg='white', bg='red', font=('Arial', 18), command=reset).place(x=420, y=360)
    
    
    
    

    
    
    
    
        
    
    
    
    mainloop()
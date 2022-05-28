
from tkinter import *
from pytube import YouTube
import tkinter
from PIL import Image, ImageTk
import youtube_dl
import os
import pyperclip




if __name__=="__main__":
    root = Tk()
    root.geometry("600x300")
    # --------------first pats in name, img, etc---------------------.
    main_border=Label(root, width=88, text="", bg='red', height=2).place(x=0, y=0)
    My_app_name = Label(root, text="Video & Adiuo Downloader",bg='red', font=("Arial", 16)).place(x=170, y=6)
    app_img = Image.open("C:/Users/DELL/Desktop/opp/images1.png")
    test= ImageTk.PhotoImage(app_img)
    label1 = tkinter.Label(image=test, font=("Arial", 1))
    label1.image = test
    label1.place(x=20, y=0, width=60, height=35)
    
    def updata():
        global url_bar
        url_bar.insert(END,pyperclip.paste())
    
    # sec parts ha in border and search bar, labe, button
    def Download_Video():
        # global res
        url = YouTube(str(link.get()))
        video = url.streams.filter(only_video=True).first()
        video.download()
        
        # video_sterem = video.streams.filter(file_extension = 'mp4').get_by_itag(res)
        # video_sterem.download(filename="Untitled", output_path = "Video_path")
        message = Label(fram, text="Enter the Video & Audio url", font=("Arial", 10), fg='black')
        message.place(x=170, y=8)
           
      
    def Download_Audio():
        PATH_SAVE = "C:/Users/DELL/Downloads"
        yt = YouTube(str(link.get()))
        video = yt.streams.filter(only_audio=True).first()
        out_file = video.download(PATH_SAVE)
        base, ext = os.path.splitext(out_file)
        new_file = base + '.mp3'
        os.rename(yt, new_file)
        
        
    
        
        
    link = StringVar() 
    fram = Frame(root, width=202, height=110, highlightbackground='black', highlightcolor="black", highlightthickness=1, bd=3)
    url_bar = Entry(fram, borderwidth=0, relief="flat",textvariable=link, highlightcolor="white")
    url_bar.place(width=430, height=30, x=10, y=50)
    past_button = Button(fram,command=updata, text='Past', background="green",fg='white', highlightbackground='black', highlightcolor='black', highlightthickness=1)
    past_button.place(x=460, y=50, width=100, height=30)
    fram.place(x=10, y=70, width=580)
    # !------video filter------------
    # Label(root, text='Video Filter', font=("Arial", 11), fg='red').place(x=38, y=185)
    # Checkbutton(text='360p',onvalue=18, offvalue=0, variable=res1).place(x=8, y=210)
    # Checkbutton(text='720p',onvalue=22, offvalue=0, variable=res2).place(x=58, y=210)
    # Checkbutton(text='1080p',onvalue=37, offvalue=0, variable=res3) .place(x=110, y=210)
    # # --------------Audio filter--------------
    # Label(root, text='Audio Filter', font=("Arial", 11), fg='red').place(x=465, y=185)
    # Checkbutton(text='360p',onvalue=18, offvalue=0).place(x=428, y=210)
    # Checkbutton(text='720p',onvalue=22, offvalue=0).place(x=478, y=210)
    # Checkbutton(text='1080p',onvalue=37, offvalue=0) .place(x=530, y=210) 
    # root.mainloop()
    
    # ------------three parts border Adiuo and video button--------------
    # link = StringVar()
    last_fram = Frame(root, width=202, height=50, highlightbackground='black',highlightcolor='black', highlightthickness=1)
    video_button = Button(last_fram, text='Video Download', fg='white', bg='red', font=("Arial", 12), command=Download_Video)
    video_button.place(x=10, y=9)
    adiuo_button = Button(last_fram, text='Adiuo Download', fg='white', bg='red', font=("Arial", 12), command=Download_Audio)
    adiuo_button.place(x=435, y=9)
    last_fram.place(x=10, y=240, width=580)
    mainloop()


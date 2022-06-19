import os
from tkinter import *
from tkinter import filedialog
import pygame
from pygame import mixer


root = Tk()
# Musicplayer(root)

root.title("Music Player")
root.geometry("800x600+120+120")
root.filename=""
root.playlist = []
root.pauseFlag = False
root.songAdded = False
root.i = 0

def upload():
    path = filedialog.askdirectory()
    if path:
        os.chdir(path)
        songs = os.listdir(path)
        for song in songs:
            if song.endswith(".mp3"):
                mylist.insert(END,song)
    


def playsong():
    if mylist:
        mixer.init()
        mixer.music.load(mylist.get(ACTIVE))
        mixer.music.play()
    
    
def stopsong():
    mixer.music.stop()


def pause_music():
    mixer.music.pause()
    
def volum(val):
    volums = float(val) / 100
    mixer.music.set_volume(volums)
    
    

    
def next_music():
    pygame.mixer.music.play(-1)
    
    


mylist = Listbox(root, bg='#566573')
mylist.pack(side=RIGHT)
mylist.place(y=40)
mylist.place(x=580, y=50, width=200, height=500)
mybutton = Button(root, text='Upload', fg='white', bg='green', font=('arial', 10), command=upload)
mybutton.place(width=197, x=580, y=22)
ssb = Scrollbar(mylist)
ssb.pack(side=RIGHT, fill=Y)

img_label = PhotoImage(file='Music.gif')
img_label_back = Label(root, image=img_label)
img_label_back.place(x=0, y=0, width=580)




# play_btn = Button(root, text='play', fg='white', bg='red', command=playsong)
# play_btn.place(y=180, x=150, anchor="center")

next_btn = Button(root, text='NEXT', fg='white', bg='red', command=next_music)
next_btn.place(y=210, x=200)

# preves_btn = Button(root, text='pause', fg='white', bg='red', command=pause_music)
# preves_btn.place(y=210, x=100)

fram_button = Frame(root, bg='#5A647A')
fram_button.place(x=0, y=410, width=560, height=110)

play_btn = PhotoImage(file='images/play.png')
play_btnn = Button(root, image=play_btn, command=playsong)
play_btnn.place(x=200, y=450, width=40, height=40)

pause_btn = PhotoImage(file='images/pause.png')
pause_btnn = Button(root, image=pause_btn, command=pause_music)
pause_btnn.place(x=120, y=450, width=40, height=40)

stops_btn = PhotoImage(file='images/stops.png')
stops_btnn = Button(root, image=stops_btn, command=stopsong)
stops_btnn.place(x=280, y=450, width=40, height=40)

volum_btn = PhotoImage(file='images/speaker.png')
volum_btnn = Label(root, image=volum_btn)
volum_btnn.place(x=370, y=450, width=40, height=40)

music_volum = Scale(root, from_=0, to=100, orient='horizontal', command=volum)
music_volum.place(x=420, y=443)


    





        
        
if __name__=="__main__":
    mainloop()
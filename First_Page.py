from tkinter import *
from PIL import Image, ImageTk
import os

root=Tk();
root.geometry("500x400")
root.configure(bg='Powder blue',width=1000,height=1000);

image = Image.open("AI image1.jpg")
image = image.resize((500,400))
photo = ImageTk.PhotoImage(image)

s_label = Label(image=photo)
s_label.pack()

def ReservationMaster():
    os.system('AI_Run.py')

btnReservationmaster=Button(root,text=" Open AI assistance " ,bd=10,relief=RAISED,command=ReservationMaster);
btnReservationmaster.pack();
btnReservationmaster.place(x=50,y=280)

root.mainloop();
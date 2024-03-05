from tkinter import * 
from tkinter.colorchooser import askcolor
from tkinter import ttk
import tkinter as tk
from tkinter import filedialog
import os
from PIL import Image,ImageTk


root=Tk()
root.title("Paint")
root.geometry("1050x570+150+50")
root.config(bg="#f2f3f4")
root.resizable(False,False)


image_icon=PhotoImage(file="Logo.png")
root.iconphoto(False,image_icon)


colour_box=PhotoImage(file="Color section.png")
Label(root,image=colour_box,bg="#f2f3f4").place(x=10,y=20)

eraser=PhotoImage(file="eraser.png")
Button(root,image=eraser,bg="#f2f3f4").place(x=30,y=400)

import_image=PhotoImage(file="addimage.png")
Button(root,image=import_image,bg="#f2f3f4").place(x=30,y=450)



colors=Canvas(root,bg="#f2f3f4",width=37,height=300,bd=0)
colors.place(x=30,y=60)

def display_pallete():
    id=colors.create_rectangle((10,10,30,30),fill="black")
    colors.tag_bind(id,"<Button-1>",lambda x:show_color("black"))
    id=colors.create_rectangle((10,40,30,60),fill="black")
    colors.tag_bind(id,"<Button-1>",lambda x:show_color("black"))
    id=colors.create_rectangle((10,70,30,90),fill="black")
    colors.tag_bind(id,"<Button-1>",lambda x:show_color("black"))   
    id=colors.create_rectangle((10,100,30,120),fill="black")
    colors.tag_bind(id,"<Button-1>",lambda x:show_color("black"))   
    id=colors.create_rectangle((10,130,30,150),fill="black")
    colors.tag_bind(id,"<Button-1>",lambda x:show_color("black"))   
    id=colors.create_rectangle((10,160,30,180),fill="black")
    colors.tag_bind(id,"<Button-1>",lambda x:show_color("black"))   
    id=colors.create_rectangle((10,190,30,210),fill="black")
    colors.tag_bind(id,"<Button-1>",lambda x:show_color("black"))   






canvas=Canvas(root,width=930,height=500,background="white",cursor="hand2")
canvas.place(x=100,y=10)




root.mainloop()
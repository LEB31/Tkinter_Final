# Lily Bain 4/26
# Credit to Parvat Computer Technology
from tkinter import *
from tkinter.colorchooser import askcolor
from tkinter import ttk 
import tkinter as tk 

# Create Window
root = Tk()
def Board():
    win = Toplevel()
    win.title('Whiteboard')
    win.geometry("1050x570+150+50")
    win.configure(bg='#f2f3f5')
    win.resizable(False,False)

    # Variables
    current_x = 0
    current_y = 0
    color = 'black'

    def locate_xy(work):
        global current_x, current_y
        current_x = work.x
        current_y = work.y

    def addLine(work):
        global current_x, current_y
        canvas.create_line((current_x,current_y,work.x,work.y),width=get_current_value(),fill=color, capstyle=ROUND,smooth=TRUE)
        current_x, current_y = work.x, work.y

    def show_color(new_color):
        global color
        color = new_color

    def new_canvas():
        canvas.delete('all')
        choice()

    # icon 
    image_icon = PhotoImage(file='pen-solid.png')
    win.iconphoto(False,image_icon)

    # Colors
    color_box = PhotoImage(file="color_section.png")
    Label(win,image=color_box,bg="#f2f3f5").place(x=10,y=20)

    colors=Canvas(win,bg="#ffffff",width=37,height=300,bd=0)
    colors.place(x=30,y=60)

    def choice():
        id = colors.create_rectangle((10,10,30,30),fill="black")
        colors.tag_bind(id, '<Button-1>',lambda x: show_color('black'))

        id = colors.create_rectangle((10,40,30,60),fill="gray")
        colors.tag_bind(id, '<Button-1>',lambda x: show_color('gray'))

        id = colors.create_rectangle((10,70,30,90),fill="#A0522D")
        colors.tag_bind(id, '<Button-1>',lambda x: show_color('#A0522D'))

        id = colors.create_rectangle((10,100,30,120),fill="#CD5C5C")
        colors.tag_bind(id, '<Button-1>',lambda x: show_color('#CD5C5C'))

        id = colors.create_rectangle((10,130,30,150),fill="#FF7F50")
        colors.tag_bind(id, '<Button-1>',lambda x: show_color('#FF7F50'))

        id = colors.create_rectangle((10,160,30,180),fill="#EEF588")
        colors.tag_bind(id, '<Button-1>',lambda x: show_color('#EEF588'))

        id = colors.create_rectangle((10,190,30,210),fill="#98FB98")
        colors.tag_bind(id, '<Button-1>',lambda x: show_color('#98FB98'))

        id = colors.create_rectangle((10,220,30,240),fill="#87CEEB")
        colors.tag_bind(id, '<Button-1>',lambda x: show_color('#87CEEB'))

        id = colors.create_rectangle((10,250,30,270),fill="#9370DB")
        colors.tag_bind(id, '<Button-1>',lambda x: show_color('#9370DB'))
    choice()

    # Eraser 
    eraser=PhotoImage(file="eraser.png")
    Button(win, image=eraser,bg="#f2f3f5",command=new_canvas).place(x=30,y=400)

    # Board  
    canvas=Canvas(win,width=930,height=500,background="white",cursor="tcross")
    canvas.place(x=100,y=10)
    canvas.bind('<Button-1>', locate_xy)
    canvas.bind('<B1-Motion>', addLine)

    # Slider 
    current_value = tk.DoubleVar()

    def get_current_value():
        return '{: .2f}'.format(current_value.get())

    def slider_changed(event):
        value_label.configure(text=get_current_value())

    slider = ttk.Scale(win,from_=0,to=100,orient='horizontal',command=slider_changed, variable=current_value)
    slider.place(x=30,y=530)

    # Value Label
    value_label = ttk.Label(win,text=get_current_value())
    value_label.place(x=27,y=550)

root.geometry('500x500')
root.title('Welcome!')
root.configure(bg='#6BA06A')
btn = Button(root, text= "Whiteboard", command=Board).place(x=135,y=250)
root.mainloop()
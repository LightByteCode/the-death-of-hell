import tkinter as tk
import sys
import time,random,threading
from PIL import Image,ImageTk

##start program##
#global varibles
width=800
height=600
#main window init
root=tk.Tk()#main window
root.title("地府之亡")
root.geometry(f"{width}x{height}")
root.resizable(False,False)#cannot resize

bg_img=Image.open("bg1.png")#open the background image
bg_img=ImageTk.PhotoImage(bg_img)#cast to TK image
#back ground canvas init
bg_cv=tk.Canvas(root,width=width,height=height,relief=tk.FLAT)#the canvas to show backgound image
bg_cv.place(x=0,y=0)
#put the background image onto the backgrond canvas
bg_cv.create_image(0,0,image=bg_img,anchor="nw")
#update
root.update()

time.sleep(2)

##main GUI##
root.update()

bg_img=Image.open("bg2.png")#open the background image
bg_img=ImageTk.PhotoImage(bg_img)#cast to TK image
bg_cv.create_image(0,0,image=bg_img,anchor="nw")

#about window
def show_about_window():
    about_win=tk.Toplevel(root,width=400,height=550)
    about_win.title("关于")
    text=tk.Text(about_win,font=("楷体",20))
    text.place(x=0,y=0,width=400,height=550)

    text.insert("0.0","游戏开发者：张高毅\n制作者：刘清硕\n")

#def open_about_window():

#about
button_about=tk.Button(bg_cv,bg="black",fg="red",font=("隶书",30),text="关于我们",relief="flat",cursor="hand2",
                        command=show_about_window,activebackground="black",activeforeground="red")
button_about.place(x=300,y=200,width=200,height=100)

#mainloop
root.mainloop()
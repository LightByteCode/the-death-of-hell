import tkinter as tk
import sys
import time,random,threading
from PIL import Image,ImageTk
'''
root_window
|__frame0(main GUI):start&main GUI
    |__bg_img
        |__button_about
        |__button_play
        |__button_settings
|__frame1(game):main game
|__about_window
'''
#--------------------------------------
##start program##
#global varibles
width=800
height=600
#main window init
root=tk.Tk()#main window
root.title("地府之亡")
root.geometry(f"{width}x{height}")
root.resizable(False,False)#cannot resize

bg_img=Image.open("logo.png")#open the background image
bg_img=ImageTk.PhotoImage(bg_img)#cast to TK image
#frames
frame0=tk.Frame(root,width=width,height=height,relief="flat",bg="white")
frame1=tk.Frame(root,width=width,height=height,relief="flat",bg="white")
frame0.place(x=0,y=0)
#back ground canvas init
bg_cv=tk.Canvas(frame0,width=width,height=height,relief="flat")#the canvas to show backgound image
bg_cv.place(x=0,y=0)
#put the background image onto the backgrond canvas
bg_cv.create_image(0,0,image=bg_img,anchor="nw")
#update
root.update()
#--------------------------------------
time.sleep(2)
#--------------------------------------
##main GUI##
root.update()

bg_img=Image.open("bg.png")#open the background image
bg_img=ImageTk.PhotoImage(bg_img)#cast to TK image
bg_cv.create_image(0,0,image=bg_img,anchor="nw")

#about window
def show_about_window():
    about_win=tk.Toplevel(root,width=400,height=550)
    about_win.title("关于")
    about_win.resizable(False,False)

    text=tk.Text(about_win,font=("楷体",20))
    text.place(x=0,y=0,width=400,height=550)

    text.insert("0.0","游戏开发者：张高毅\n制作者：刘清硕\n版权所有：拜阎王会")
    text.window_create("1.0")

    text.config(state="disabled")

#about
button_about=tk.Button(bg_cv,bg="black",fg="red",font=("隶书",30),text="关于我们",relief="flat",cursor="hand2",
                        command=show_about_window,activebackground="black",activeforeground="red")
button_about.place(x=300,y=200,width=200,height=70)
#start main game
#---------class Card---------
class Card:
    def __init__(self,num,color,pos=(0,0)):
        global frame1
        self.num=num
        self.color=color
        self.x,self.y=pos
        if self.color=="black":
            text_color="white"
        else:
            text_color="black"
        self.body=tk.Button(frame1,relief="flat",bg=self.color,fg=text_color)
        
#------------Card------------
def start_main_game():
    pass
#start play
button_play=tk.Button(bg_cv,bg="black",fg="red",font=("隶书",30),text="开始游戏",relief="flat",cursor="hand2",
                        command=None,activebackground="black",activeforeground="red")
button_play.place(x=300,y=300,width=200,height=70)
#--------------------------------------
#mainloop
root.mainloop()

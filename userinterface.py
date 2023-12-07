import tkinter
from tkinter import *
root= Tk()

root.geometry("500x250")
# Describes the body of the graphical user interface


l= Label(root, text= "High score=0").pack()

from tkinter import messagebox

e= Entry(root, width=50)
e.pack()

def myClick():
    mylabel= Label(root, text=e.get())
    mylabel.pack()

def good_box():
    messagebox.showinfo("HomeWoof","Good job!")
tkinter.Button(root,text="Behaves",command=good_box).pack()

def bad_box():
   messagebox.showinfo("HomeWoof","Bad dog!")
tkinter.Button(root,text="Misbehaves",command=bad_box).pack()

def improvement_box():
    messagebox.showinfo("HomeWoof","You're getting there!")
tkinter.Button(root,text="Needs Improvement",command=improvement_box).pack()


myButton=Button(root,text="Add User: ", command=myClick)
myButton.pack()

root.mainloop()

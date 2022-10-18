from cProfile import label
import tkinter
from tkinter import *
from tkinter.font import BOLD

root=Tk()
root.title("Basic Calculator")
root.geometry("600x600")
root.resizable(False, False)
root.configure(bg="red")

equation=""

#Function for 'Numbers and Oparators' button
def show(value):
    global equation
    equation+=value
    label_result.config(text=equation)

#Function for 'Clear' button
def clear():
    global equation
    equation=""
    label_result.config(text=equation)

#Function for 'Equal to' button
def calculate():
    global equation
    result=""
    if equation!="":
        try:
            result=eval(equation)
        except:
            result="error"
            equation=""
    label_result.config(text=result)

#The result box
label_result=Label(root, width=35, height=4, text="", font=("arial",20))
label_result.pack()

#The buttonts of first row
Button(root,text="C",width=11,height=1,font=("arial",30,"bold"),fg="black",bg="yellow", command=lambda:clear()).place(x=17, y=140) 
Button(root,text="/",width=5,height=1,font=("arial",30,"bold"),fg="black",bg="cyan",command=lambda: show("/")).place(x=310, y=140) 
Button(root,text="*",width=5,height=1,font=("arial",30,"bold"),fg="black",bg="cyan",command=lambda: show("*")).place(x=455, y=140) 

#The buttonts of second row
Button(root,text="7",width=5,height=1,font=("arial",30,"bold"),fg="black",bg="cyan",command=lambda: show("7")).place(x=17, y=230)
Button(root,text="8",width=5,height=1,font=("arial",30,"bold"),fg="black",bg="cyan",command=lambda: show("8")).place(x=165, y=230) 
Button(root,text="9",width=5,height=1,font=("arial",30,"bold"),fg="black",bg="cyan",command=lambda: show("9")).place(x=310, y=230) 
Button(root,text="-",width=5,height=1,font=("arial",30,"bold"),fg="black",bg="cyan",command=lambda: show("-")).place(x=455, y=230)

#The buttonts of third row
Button(root,text="4",width=5,height=1,font=("arial",30,"bold"),fg="black",bg="cyan",command=lambda: show("4")).place(x=17, y=320)
Button(root,text="5",width=5,height=1,font=("arial",30,"bold"),fg="black",bg="cyan",command=lambda: show("5")).place(x=165, y=320) 
Button(root,text="6",width=5,height=1,font=("arial",30,"bold"),fg="black",bg="cyan",command=lambda: show("6")).place(x=310, y=320) 
Button(root,text="+",width=5,height=1,font=("arial",30,"bold"),fg="black",bg="cyan",command=lambda: show("+")).place(x=455, y=320)

#The buttonts of fourth row
Button(root,text="1",width=5,height=1,font=("arial",30,"bold"),fg="black",bg="cyan",command=lambda: show("1")).place(x=17, y=410)
Button(root,text="2",width=5,height=1,font=("arial",30,"bold"),fg="black",bg="cyan",command=lambda: show("2")).place(x=165, y=410) 
Button(root,text="3",width=5,height=1,font=("arial",30,"bold"),fg="black",bg="cyan",command=lambda: show("3")).place(x=310, y=410)
Button(root,text="=",width=5,height=3,font=("arial",30,"bold"),fg="black",bg="orange",command=lambda: calculate()).place(x=455, y=410)

#The buttonts of fifth row
Button(root,text="0",width=11,height=1,font=("arial",30,"bold"),fg="black",bg="cyan",command=lambda: show("0")).place(x=17, y=500)
Button(root,text=".",width=5,height=1,font=("arial",30,"bold"),fg="black",bg="cyan",command=lambda: show(".")).place(x=310, y=500)

root.mainloop()


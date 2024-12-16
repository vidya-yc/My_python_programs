
from tkinter import *
from tkinter.tix import Control, Tk, ComboBox
from tkinter import messagebox
top = Tk()
def info():
    messagebox.showinfo("info","Submitted the selected animal")

lb = Label(top,text="Animals in pair").pack()
ct = Control(top,label="Number: ",integer="True",max=12,min=2,value=2,step=2).pack()
cb = ComboBox(top,label="type",editable="True")
for animals in("Cat","Dog","snake"):
    cb.insert(END,animals)
cb.pack()
b1= Button(top,text="SUBMIT",command=info).pack()
b2 = Button(top,text="QUIT",command=top.destroy).pack()
top.mainloop()
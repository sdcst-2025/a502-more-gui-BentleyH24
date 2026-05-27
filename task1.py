import tkinter as tk 
from tkinter import *
from tkinter import ttk

#width,height

window = tk.Tk()
window.title = ("Tk")
window.geometry("400x100")
window.attributes("-topmost",True)

label1 = tk.Label(window, text = "Principal")
label2 = tk.Label(window, text = "Interest Rate")
label3= tk.Label(window, text = "Years")
label4 = tk.Label(window, text = "Amount")

entry1 = tk.Entry(window,text= "", borderwidth=3, relief=SUNKEN)
entry2 =tk.Entry(window)
entry3 = tk.Entry(window)
entry4 = tk.Entry(window)

combo = ttk.Combobox(window,values=["1","2","3","4"])

entry2.place(x=10,y=30)
entry3.place(x=130,y=30)
entry4.place(x=130, y=80)

label1.place(x=50,y=10)
label2.place(x=160,y=10)
label3.place(x=300,y=10)
label4.place(x=70,y=80)

combo.place(x=250,y=30, width=150)

window.mainloop()
#!python3
import tkinter as tk 
from tkinter import *
#importing ttk is required to use the tkinter.place() method
from tkinter import ttk

window = tk.Tk()
window.title = ("Tk")
window.geometry("650x650")
window.attributes("-topmost",True)

mainPhoto = PhotoImage(file="main.png")
miniMapPhoto = PhotoImage(file="minimap.png")
nintendoLogo = PhotoImage(file="logo.png")

label1 = tk.Label(window, image = mainPhoto)
label2 = tk.Label(window, image=miniMapPhoto)
label3 = tk.Label(window, image=nintendoLogo)

pokemonAdventure = tk.Label(window,text="POKEMON ADVENTURE")
miniMap = tk.Label(window,text="MINI MAP")

mapButton = tk.Button(window,text="MAP",width=13,height=2)
inventoryButton = tk.Button(window,text="INVENTORY",width=13,height=2)
pokedexButton = tk.Button(window,text="POKEDEX",width=13,height=2)
rosterButton = tk.Button(window,text="ROSTER",width=13,height=2)
journalButton = tk.Button(window,text="JOURNAL",width=13,height=2)
helpButton = tk.Button(window,text="HELP",width=13,height=2)
shopButton = tk.Button(window,text="SHOP",width=13,height=2)

northButton = tk.Button(window,text="N",width=3,height=1)
northEButton = tk.Button(window,text="NE",width=3,height=1)
eastButton = tk.Button(window,text="E",width=3,height=1)
southEButton = tk.Button(window,text="SE",width=3,height=1)
southButton = tk.Button(window,text="S",width=3,height=1)
southWButton = tk.Button(window,text="SW",width=3,height=1)
westButton = tk.Button(window,text="W",width=3,height=1)
northWButton = tk.Button(window,text="NW",width=3,height=1)

#============================================================

label1.place(x=10,y=50)
label2.place(x=520,y=100)
label3.place(x=200,y=500)

pokemonAdventure.place(x=200,y=20)
miniMap.place(x=535,y= 80)

mapButton.place(x=522,y=200)
inventoryButton.place(x=522,y=240)
pokedexButton.place(x=522,y=280)
rosterButton.place(x=522,y=320)
journalButton.place(x=522,y=360)
helpButton.place(x=522,y=400)
shopButton.place(x=522,y=440)

northButton.place(x=50,y=500)
northEButton.place(x=80,y=500)
eastButton.place(x=80,y=530)
southEButton.place(x=80,y=560)
southButton.place(x=50,y=560)
southWButton.place(x=20,y=560)
westButton.place(x=20,y=530)
northWButton.place(x=20,y=500)

window.mainloop()
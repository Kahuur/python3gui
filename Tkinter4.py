from tkinter import *

#akna seaded
aken = Tk()
aken.title('Käibemaksukalkulaator')
aken.configure()
#aken.iconbitmap('faviii.ico')
aken.geometry("300x194")
aken.resizable(0, 0)

#funktsioonid
def arvuta ():
    hind = float(sisestus.get())
    kmaks = var.get()
    
    km = hind*kmaks
    raha.config(text=f"{km:.2f}€")
    hkm = hind+km
    raha2.config(text=f"{hkm:.2f}€")
    

#nupud
nupp1 = Button(aken, font = "Tahoma 12", text="Ok", width=4, command=arvuta)
nupp1.grid(row=7, column=1, sticky = "e", padx = 2, pady = 2)

silt = Label(aken, font = "Tahoma 12", text="Hind käibemaksuta:")
silt.grid(row=1, sticky="w")
sisestus = Entry(aken)
sisestus.grid(row=1, column=1)


#valikukast
var = DoubleVar()
silt1 = Label(aken, font = "Tahoma 12", text="Käibemaksumäär:")
silt1.grid(row=2, sticky="w")
valikukast = Radiobutton(aken, font = "Tahoma 12",text="9%", variable=var, value=0.09)
valikukast.grid(row=2, column=1)
valikukast = Radiobutton(aken, font = "Tahoma 12",text="20%", variable=var, value=0.2)
valikukast.grid(row=3, column=1)
joon = Label(aken, font = "Tahoma 10", text="__________________________________________")
joon.grid(row=4, column=0, columnspan=2)
silt2 = Label(aken, font = "Tahoma 12", text="Käibemaks:")
silt2.grid(row=5, sticky="w")
silt3 = Label(aken, font = "Tahoma 12", text="Hind käibemaksuga:")
silt3.grid(row=6, sticky="w")
raha = Label(aken, font = "Tahoma 12", text="0.00€")
raha.grid(row=5, column=1)
raha2 = Label(aken, font = "Tahoma 12", text="0.00€")
raha2.grid(row=6, column=1)

aken.mainloop()
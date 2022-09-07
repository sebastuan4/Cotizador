from tkinter import *
from tokenize import String
import info
import coseg
#Global variables
price_global="d"
class cotizador():
    def search(plate,id,flag_coseg,price,flag_cl):
        if price=="":
            global price_global
            price=info.info.crautos(plate,flag_cl)
            print(f"El valor del auto es de: {price}")
        if flag_coseg=="1":
            coseg.coseg.coseg(plate,id,price)
        else:
            pass
    
    def UI(self):
        root=Tk()
        global price_global
        txt_id=Entry(root)
        txt_plate=Entry(root)
        txt_price=Entry(root)
        flag_coseg=StringVar()
        flag_cl=StringVar()
        price=StringVar()
        chk_coseg=Checkbutton(root,text="Coseg",variable=flag_coseg, onvalue=1,offvalue=0)
        chk_cl=Checkbutton(root,text="CL",variable=flag_cl, onvalue=1,offvalue=0)
        flag_coseg.set(0)
        flag_cl.set(0)
        btn_buscar=Button(root,text="Cotizar",command=lambda:cotizador.search(txt_plate.get(),txt_id.get(),flag_coseg.get(),txt_price.get(),flag_cl.get()))
       
        #Mostrando
        Label(root,text="Cedula").pack()
        txt_id.pack()
        Label(root,text="Placa").pack()
        txt_plate.pack()
        Label(root,text="Precio").pack()
        txt_price.pack()
        chk_coseg.pack()
        chk_cl.pack()
        btn_buscar.pack()
        root.mainloop()
cotizador().UI()
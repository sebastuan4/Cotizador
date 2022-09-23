from tkinter import *
import info
import coseg
import manual
#Global variables
price_global="d"
class cotizador():
    def search(plate,id,flag_coseg,price,flag_cl,flag_c,flag_rapido,flag_comercial):
        flag_registro=0
        if price=="":
            global price_global
            lista=info.info.crautos(plate,flag_cl,flag_c,flag_rapido)
            price=lista[10]
            flag_registro=1
        if flag_coseg=="1":
            coseg.coseg.coseg(plate,id,price)
        else:
            if flag_registro==0:
                lista = info.info.registro(plate,flag_cl,flag_c,flag_rapido)
            manual.paralelo.iniciar(id,flag_cl,flag_c,price,lista,plate,flag_comercial)
            pass
    
    def UI(self):
        root=Tk()
        global price_global
        txt_id=Entry(root)
        txt_plate=Entry(root)
        txt_price=Entry(root)
        flag_coseg=StringVar()
        flag_cl=StringVar()
        flag_c=StringVar()
        flag_rapido=StringVar()
        flag_comercial=StringVar()
        chk_rapido=Checkbutton(root,text="M.Rapido",variable=flag_rapido, onvalue=1,offvalue=0)
        chk_coseg=Checkbutton(root,text="Coseg",variable=flag_coseg, onvalue=1,offvalue=0)
        chk_cl=Checkbutton(root,text="CL",variable=flag_cl, onvalue=1,offvalue=0)
        chk_c=Checkbutton(root,text="C",variable=flag_c, onvalue=1,offvalue=0)
        chk_comercial=Checkbutton(root,text="Comercial",variable=flag_c, onvalue=1,offvalue=0)
        flag_rapido.set(0)
        flag_coseg.set(0)
        flag_c.set(0)
        flag_cl.set(0)
        flag_comercial.set(0)
        btn_buscar=Button(root,text="Cotizar",command=lambda:cotizador.search(txt_plate.get(),txt_id.get(),flag_coseg.get(),txt_price.get(),flag_cl.get(),flag_c.get(),flag_rapido.get(),flag_rapido.get()))
       
        #Mostrando
        Label(root,text="Cedula").pack()
        txt_id.pack()
        Label(root,text="Placa").pack()
        txt_plate.pack()
        Label(root,text="Precio").pack()
        txt_price.pack()
        chk_coseg.pack()
        chk_cl.pack()
        chk_c.pack()
        chk_comercial.pack()
        chk_rapido.pack()
        btn_buscar.pack()
        root.mainloop()
cotizador().UI()
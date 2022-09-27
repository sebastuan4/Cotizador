from tkinter import *
from tkinter import ttk
import info
import coseg
import manual

#Global variables
price_global="d"
class cotizador():
    def search(plate,id,flag_coseg,price,flag_cl,flag_c,flag_comercial,tipo_cedula):
        flag_registro=0
        if price=="":
            global price_global
            lista=info.info.crautos(plate,flag_cl,flag_c)
            price=lista[10]
            flag_registro=1
        if flag_coseg=="1":
            coseg.coseg.coseg(plate,id,price)
        else:
            if flag_registro==0:
                lista = info.info.registro(plate,flag_cl,flag_c)
            manual.paralelo.cotizar(id,flag_cl,flag_c,price,lista,plate,flag_comercial,tipo_cedula)
    
    def UI(self):
        root=Tk()
        global price_global
        #Visuales
        root.title("Cotizador")
        root.geometry("250x360")


        flag_coseg=StringVar()
        flag_cl=StringVar()
        flag_c=StringVar()
        flag_comercial=StringVar()
        tipo_cedula=StringVar()
        vlist = ["Carné diplomático", "Cédula de residencia", "Cédula física",
          "Cédula juridíca", "Dimex","Empresa extranjera","Nite","Pasaporte","Cédula Jurídica Gobierno Central","Cédula Institución Autónoma"]

        txt_id=Entry(root)
        txt_plate=Entry(root)
        txt_price=Entry(root)
        chk_coseg=Checkbutton(root,text="Coseg",variable=flag_coseg, onvalue=1,offvalue=0)
        chk_cl=Checkbutton(root,text="CL",variable=flag_cl, onvalue=1,offvalue=0)
        chk_c=Checkbutton(root,text="C",variable=flag_c, onvalue=1,offvalue=0)
        chk_comercial=Checkbutton(root,text="Comercial",variable=flag_comercial, onvalue=1,offvalue=0)
        Combo = ttk.Combobox(root, textvariable=tipo_cedula)
        Combo["values"]=vlist
        btn_buscar=Button(root,text="Cotizar",command=lambda:cotizador.search(txt_plate.get(),txt_id.get(),flag_coseg.get(),txt_price.get(),flag_cl.get(),flag_c.get(),flag_comercial.get(),tipo_cedula.get()))

        flag_comercial.set(0)
        flag_coseg.set(0)
        flag_c.set(0)
        flag_cl.set(0)
        tipo_cedula.set('Cédula física')
       
        #Mostrando
        Label(root,text="Cedula").pack()
        txt_id.pack()
        Label(root,text="Placa").pack()
        txt_plate.pack()
        Label(root,text="Precio").pack()
        txt_price.pack()
        Label(root,text="Manual o coseg").pack()
        chk_coseg.pack()
        Label(root,text="Tipo de placa").pack()
        chk_cl.pack()
        chk_c.pack()
        Label(root,text="Tipo de uso").pack()
        chk_comercial.pack()
        Label(root,text="Cedula del cliente").pack()
        Combo.pack()
        btn_buscar.pack()

        root.mainloop()    
cotizador().UI()
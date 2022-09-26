import lxml.html
import lxml.html.clean
import re
from colorama import Fore
class cleaning():
    def string_to_num(string=""):
        doc = lxml.html.fromstring(string)
        cleaner = lxml.html.clean.Cleaner(style=True)
        doc = cleaner.clean_html(doc)
        text = doc.text_content()
        string=str(text)
        string=string.replace('¢', '')
        string=string.replace(',', '')
        print(Fore.YELLOW+f"El valor es: {string}")
        return int(string)

    def listregex(lista):
            lista=list(lista)
            lista[2]=re.sub("C.C","",lista[2])
            lista[4]=re.sub("PUERTAS|[0-9]","",lista[4])
            lista[4]+=lista[7]
            lista[8]=re.sub(" kgrms.","",lista[8])
            lista[9]=re.sub(" personas","",lista[9])
            print(Fore.RED+f"Los datos son: {lista}")
            return lista

    def listhtml(lista):
        lista_lista=[]
        for string in lista:
            doc = lxml.html.fromstring(string)
            cleaner = lxml.html.clean.Cleaner(style=True)
            doc = cleaner.clean_html(doc)
            text = doc.text_content()
            string=str(text)
            lista_lista.append(string)
        print(Fore.RED+f"Los datos son: {lista_lista}")
        print(Fore.GREEN+f"El dueño es: {lista_lista[6]}")
        print("")
        return cleaning.listregex(lista_lista)

    def tseformato(cliente):
            cliente=list(cliente)
            clienteDatos=[]
            name = str(cliente[0]).split()
            nacimiento=cliente[1]
            clienteDatos.append(nacimiento)
            for palabras in name:
                clienteDatos.append(palabras)
            print(Fore.RED+f"Los datos son: {clienteDatos}")
            return clienteDatos

    def tsehtml(cliente):
        cliente_listo=[]
        for string in cliente:
            doc = lxml.html.fromstring(string)
            cleaner = lxml.html.clean.Cleaner(style=True)
            doc = cleaner.clean_html(doc)
            text = doc.text_content()
            string=str(text)
            cliente_listo.append(string)
        print(Fore.GREEN+f"Los datos son: {cliente_listo}")
        return cleaning.tseformato(cliente_listo)
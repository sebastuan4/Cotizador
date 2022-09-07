import lxml.html
import lxml.html.clean
import re
class cleaning():
    def string_to_num(string):
        doc = lxml.html.fromstring(string)
        cleaner = lxml.html.clean.Cleaner(style=True)
        doc = cleaner.clean_html(doc)
        text = doc.text_content()
        string=str(text)
        string=string.replace('¢', '')
        string=string.replace(',', '')
        return int(string)

    def listhtml(lista):
        lista_lista=[]
        for string in lista:
            doc = lxml.html.fromstring(string)
            cleaner = lxml.html.clean.Cleaner(style=True)
            doc = cleaner.clean_html(doc)
            text = doc.text_content()
            string=str(text)
            lista_lista.append(string)
        lista_lista.append(re.sub("[^0-9]", "", lista[4]))
        print(f"Los datos son: {lista_lista}")
        print(f"El dueño es: {lista_lista[6]}")
        return lista_lista
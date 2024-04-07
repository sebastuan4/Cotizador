from selenium import webdriver #Crear navegador
from selenium.webdriver.edge.service import Service #Aplicar el navegador
from webdriver_manager.microsoft import EdgeChromiumDriverManager #Navegador
from selenium.webdriver.common.by import By #Buscado
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import pyautogui
import cleaning
import time
import os


def descargas():
    if os.name == 'nt':
        import winreg
        sub_key = r'SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\Shell Folders'
        downloads_guid = '{374DE290-123F-4565-9164-39C4925E467B}'
        with winreg.OpenKey(winreg.HKEY_CURRENT_USER, sub_key) as key:
            location = winreg.QueryValueEx(key, downloads_guid)[0]
        return location

class info():
    def crautos(plate,flag_cl,flag_c):
            caracteristicas=info.registro(plate,flag_cl,flag_c)
            url_crautos="https://crautos.com/bluebook/"
            driver=webdriver.Edge(service=Service(EdgeChromiumDriverManager().install()))
            driver.get(url_crautos)
            driver.maximize_window()
            time.sleep(2)
            #Marca
            driver.find_element(by=By.XPATH,value='//select[@id="brand"]').click()
            driver.find_element(by=By.XPATH,value='//select[@id="brand"]').send_keys(caracteristicas[0])
            driver.find_element(by=By.XPATH,value='//select[@id="brand"]').click()
            #Modelo
            driver.find_element(by=By.XPATH,value='//input[@name="modelstr"]').send_keys(caracteristicas[1])
            #Cilindraje
            driver.find_element(by=By.XPATH,value='//input[@onkeyup="stringFilter(motorfrom)"]').clear()
            driver.find_element(by=By.XPATH,value='//input[@onkeyup="stringFilter(motorfrom)"]').send_keys(caracteristicas[2])
            #Estilo
            driver.find_element(by=By.XPATH,value='//select[@id="style"]').click()
            driver.find_element(by=By.XPATH,value='//select[@id="style"]').send_keys(caracteristicas[4])
            driver.find_element(by=By.XPATH,value='//select[@id="style"]').click()
            #Combustible
            driver.find_element(by=By.XPATH,value='//select[@name="fuel"]').click()
            driver.find_element(by=By.XPATH,value='//select[@name="fuel"]').send_keys(caracteristicas[3])
            driver.find_element(by=By.XPATH,value='//select[@name="fuel"]').click()
            #Año
            driver.find_element(by=By.XPATH,value='//select[@name="yearfrom"]').click()
            driver.find_element(by=By.XPATH,value='//select[@name="yearfrom"]').send_keys(caracteristicas[5])
            driver.find_element(by=By.XPATH,value='//select[@name="yearfrom"]').click()
            #Esperando a que salga la trabla de precios
            WebDriverWait(driver, 2000).until(EC.presence_of_element_located((By.XPATH, '(//td[@align="left"])[13]')))
            price = driver.find_element(by=By.XPATH,value='(//td[@align="left"])[13]').get_attribute("innerHTML")
            price = cleaning.cleaning.string_to_num(price)
            caracteristicas.append(price)
            time.sleep(1)
            pyautogui.hotkey('ctrl','p')
            time.sleep(2)
            pyautogui.hotkey('enter')
            time.sleep(1)
            pyautogui.typewrite(f"{descargas()}\{plate}_CrAutos.pdf")
            time.sleep(1)
            pyautogui.hotkey('enter')
            time.sleep(3)
            return caracteristicas


    def registro(plate,flag_cl,flag_c):
            url_registro="https://www.rnpdigital.com/shopping/login.jspx"
            driver=webdriver.Edge(service=Service(EdgeChromiumDriverManager().install()))
            driver.get(url_registro)
            driver.maximize_window()
            time.sleep(2)
            driver.find_element(by=By.XPATH,value='(//input[@class="inputbox"])[1]').send_keys("")
            driver.find_element(by=By.XPATH,value='(//input[@class="inputbox"])[2]').send_keys("")
            time.sleep(1)
            driver.find_element(by=By.XPATH,value='//input[@value="Ingresar"]').click()
            time.sleep(2)
            driver.find_element(by=By.XPATH,value='//a[@title="Consultas Gratuitas"]').click()
            time.sleep(1.2)
            driver.find_element(by=By.XPATH,value='//*[contains(text(),"Consulta de Vehículo")]').click()
            time.sleep(1.2)
            #if para seleccionar carga pesada o carga liviana
            if flag_cl=="1":
                driver.find_element(by=By.XPATH,value='//select[@id="class"]').click()
                time.sleep(1)
                driver.find_element(by=By.XPATH,value='//select[@id="class"]').send_keys("cl")
                time.sleep(1)
                driver.find_element(by=By.XPATH,value='//select[@id="class"]').click()
                time.sleep(1)
            if flag_c=="1":
                driver.find_element(by=By.XPATH,value='//select[@id="class"]').click()
                time.sleep(1)
                driver.find_element(by=By.XPATH,value='//select[@id="class"]').send_keys("c")
                time.sleep(0.3)
                driver.find_element(by=By.XPATH,value='//select[@id="class"]').send_keys("c")
                time.sleep(1)
                driver.find_element(by=By.XPATH,value='//select[@id="class"]').click()
                time.sleep(1.5)
            #Digitando los datos del vehiculo
            driver.find_element(by=By.XPATH,value='//input[@id="carNumber"]').send_keys(plate)
            time.sleep(1.2)
            driver.find_element(by=By.XPATH,value='(//a[@onclick])[26]').click()
            WebDriverWait(driver, 2000).until(EC.presence_of_element_located((By.XPATH, '(//td)[79]')))
            #Adquiriendo los datos de la tabla del registro
            caracteristicas=[]
            caracteristicas.append(driver.find_element(by=By.XPATH,value='(//td)[16]').get_attribute("innerHTML"))#marca
            caracteristicas.append(driver.find_element(by=By.XPATH,value='(//td)[18]').get_attribute("innerHTML"))#Modelo
            caracteristicas.append(driver.find_element(by=By.XPATH,value='(//td)[79]').get_attribute("innerHTML"))#cilindraje
            caracteristicas.append(driver.find_element(by=By.XPATH,value='(//td)[85]').get_attribute("innerHTML"))#Combustible
            caracteristicas.append(driver.find_element(by=By.XPATH,value='(//td)[28]').get_attribute("innerHTML"))#Carroceria
            caracteristicas.append(driver.find_element(by=By.XPATH,value='(//td)[40]').get_attribute("innerHTML"))#Año
            caracteristicas.append(driver.find_element(by=By.XPATH,value='(//div)[103]').get_attribute("innerHTML"))#dueño
            caracteristicas.append(driver.find_element(by=By.XPATH,value='(//td)[32]').get_attribute("innerHTML"))#traccion
            caracteristicas.append(driver.find_element(by=By.XPATH,value='(//td)[34]').get_attribute("innerHTML"))#Peso
            caracteristicas.append(driver.find_element(by=By.XPATH,value='(//td)[22]').get_attribute("innerHTML"))#Personas
            pyautogui.hotkey('ctrl','p')
            time.sleep(2)
            pyautogui.hotkey('enter')
            time.sleep(1)
            pyautogui.typewrite(f"{descargas()}\{plate}_Registro.pdf")
            time.sleep(1)
            pyautogui.hotkey('enter')
            time.sleep(3)
            return cleaning.cleaning.listhtml(caracteristicas)

    def tse(cedula):
            url_registro="https://servicioselectorales.tse.go.cr/chc/consulta_cedula.aspx"
            driver=webdriver.Edge(service=Service(EdgeChromiumDriverManager().install()))
            driver.get(url_registro)
            driver.maximize_window()
            #Llenado de cedula
            driver.find_element(by=By.XPATH,value='//input[@id="txtcedula"]').click()
            driver.find_element(by=By.XPATH,value='//input[@id="txtcedula"]').send_keys(cedula)
            time.sleep(1)
            driver.find_element(by=By.XPATH,value='//input[@id="btnConsultaCedula"]').click()
            time.sleep(2)
            cliente = []
            cliente.append(driver.find_element(by=By.XPATH,value='//span[@id="lblnombrecompleto"]').get_attribute("innerHTML"))
            cliente.append(driver.find_element(by=By.XPATH,value='//span[@id="lblfechaNacimiento"]').get_attribute("innerHTML"))
            return cleaning.cleaning.tsehtml(cliente)

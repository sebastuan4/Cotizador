from tkinter import *
from selenium import webdriver #Crear navegador
from selenium.webdriver.edge.service import Service #Aplicar el navegador
from webdriver_manager.microsoft import EdgeChromiumDriverManager #Navegador
from selenium.webdriver.common.by import By #Buscado
from selenium.webdriver.common.action_chains import ActionChains
import time
class coseg():
    def coseg(plate,id,price):
        url_coseg="http://coseg.net/"
        driver=webdriver.Edge(service=Service(EdgeChromiumDriverManager().install()))
        a=ActionChains(driver)
        driver.get(url_coseg)
        driver.maximize_window()
        time.sleep(4)
        #Login page
        driver.find_element(by=By.XPATH,value='//input[@id="Usuario"]').send_keys("aalvarado")
        driver.find_element(by=By.XPATH,value='//input[@id="Password"]').send_keys("P@ssword44440")
        driver.find_element(by=By.XPATH,value='//button[@type="submit"]').click()
        time.sleep(1)
        #Seleccion de tipo de seguro
        dropdown=driver.find_element(by=By.XPATH,value='//a[@class="nav-link dropdown-toggle"]')
        a.move_to_element(dropdown).perform()
        driver.find_element(by=By.XPATH,value='//a[@href="/AutoSimple/Cotizar"]').click()
        time.sleep(1)
        #Llenadod e informacion cedula y placa
        driver.find_element(by=By.XPATH,value='(//input[@id="txtCedula"])[2]').send_keys(id)
        driver.find_element(by=By.XPATH,value='//input[@id="txtPlaca"]').send_keys(plate)
        driver.find_element(by=By.XPATH,value='//button[@id="BuscarPlaca"]').click()
        time.sleep(2)
        #Precio del automovil
        driver.find_element(by=By.XPATH,value='(//input[@inputmode="numeric"])[2]').click()
        driver.find_element(by=By.XPATH,value='(//input[@inputmode="numeric"])[2]').send_keys(price)
        driver.find_element(by=By.XPATH,value='(//button[@name="btn_Cot"])[2]').click()
        #Esperando a que termine el comparativo
        time.sleep(20)
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        driver.find_element(by=By.XPATH,value=r"""//button[@ng-click="Open('#CoberLAFISEModal')"]""").click()
        time.sleep(1)
        driver.find_element(by=By.XPATH,value='//button[@ng-click="UrlCotizacion(3)"]').click()
        driver.switch_to.window(driver.window_handles[0])
        driver.find_element(by=By.XPATH,value='(//button[@class="close"])[9]').click()
        #Descargar comparativo
        driver.find_element(by=By.XPATH,value='//span[@ng-click="CardClick(1)"]').click()
        time.sleep(0.2)
        driver.find_element(by=By.XPATH,value='//span[@ng-click="CardClick(2)"]').click()
        time.sleep(0.2)
        driver.find_element(by=By.XPATH,value='//span[@ng-click="CardClick(3)"]').click()
        time.sleep(0.2)
        driver.find_element(by=By.XPATH,value='//span[@ng-click="CardClick(4)"]').click()
        time.sleep(0.2)
        driver.find_element(by=By.XPATH,value='//button[@class="ripple"]').click()
        time.sleep(20000)
from tkinter import *
from selenium import webdriver #Crear navegador
from selenium.webdriver.edge.service import Service #Aplicar el navegador
from webdriver_manager.microsoft import EdgeChromiumDriverManager #Navegador
from selenium.webdriver.common.by import By #Buscado
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import cleaning
import time
class ins():
    def cotizar(id):
        url_ins="https://cotiza.ins-cr.com/frmLogin.aspx"
        driver=webdriver.Edge(service=Service(EdgeChromiumDriverManager().install()))
        driver.get(url_ins)
        driver.maximize_window()
        a=ActionChains(driver)
        time.sleep(1)
        #Logueo
        driver.find_element(by=By.XPATH,value='//input[@id="txtUsuario"]').send_keys("110650128")
        driver.find_element(by=By.XPATH,value='//input[@id="txtPassword"]').send_keys("Ivaalo3004")
        driver.find_element(by=By.XPATH,value='//button[@id="INSContent_btnIngresar"]').click()
        time.sleep(5)
        #Dropdown
        driver.find_element(by=By.XPATH,value='(//span[@class="pulse collapsed"])[1]').click()
        time.sleep(1)
        #Seleccion del seguro
        autos=driver.find_element(by=By.XPATH,value='//input[@id="INSContent_btnCotizar330"]')
        a.move_to_element(autos).perform()
        autos.click()
        time.sleep(4)
        #Llenado de cedula
        driver.find_element(by=By.XPATH,value='//input[@name="ctl00$INSContent$ctrDinamico$IDENTCLI$ctl04"]').send_keys(id)
        driver.find_element(by=By.XPATH,value='//a[@id="lnkIDENTCLI"]').click()
        time.sleep(1)
        driver.find_element(by=By.XPATH,value='//input[@id="INSContent_ctrDinamico_btnAvanzar"]').click()
        #plate,id,flag_coseg,price
        time.sleep(2000)
ins.cotizar(118260556)
        

        

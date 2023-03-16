import multiprocessing
from multiprocessing.dummy import freeze_support
from tkinter import *
from selenium import webdriver #Crear navegador
from selenium.webdriver.edge.service import Service #Aplicar el navegador
from webdriver_manager.microsoft import EdgeChromiumDriverManager #Navegador
from selenium.webdriver.common.by import By #Buscado
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import WebDriverException
import pyautogui
from joblib import Parallel, delayed
import multiprocessing
import info
import time

class ins():
    def cotizar(id,flag_cl,flag_c,price,tabla,plate,flag_comercial,tipo_cedula):
        url_ins="https://cotiza.ins-cr.com/frmLogin.aspx"
        driver=webdriver.Edge(service=Service(EdgeChromiumDriverManager().install()))
        driver.get(url_ins)
        driver.maximize_window()
        a=ActionChains(driver)
        time.sleep(1)
        #Logueo
        driver.find_element(by=By.XPATH,value='//input[@id="txtUsuario"]').send_keys("")
        driver.find_element(by=By.XPATH,value='//input[@id="txtPassword"]').send_keys("")
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
        #Tipo de cedula
        if tipo_cedula=="Dimex":
            tipo_cedula="Documento Migratorio"
        if tipo_cedula=="Carné diplomático":
            tipo_cedula="d"
        if tipo_cedula=="Cédula juridíca":
            tipo_cedula="Cédula Persona Juridíca"
        driver.find_element(by=By.XPATH,value='//select[@id="TIPOIDCLI"]').click()
        driver.find_element(by=By.XPATH,value='//select[@id="TIPOIDCLI"]').send_keys(tipo_cedula)
        driver.find_element(by=By.XPATH,value='//select[@id="TIPOIDCLI"]').send_keys(Keys.ENTER)
        #Llenado de cedula
        driver.find_element(by=By.XPATH,value='//input[@name="ctl00$INSContent$ctrDinamico$IDENTCLI$ctl04"]').send_keys(id)
        driver.find_element(by=By.XPATH,value='//a[@id="lnkIDENTCLI"]').click()
        
        #driver.find_element(by=By.XPATH,value='//input[@id="INSContent_ctrDinamico_btnAvanzar"]').click()

        #Esperando que salga la parte de cotizar
        WebDriverWait(driver, 2000).until(EC.presence_of_element_located((By.XPATH, '//select[@id="CLASEPLACARSGO"]')))
        #LLenando tipo de placa
        if flag_cl=="1":
            driver.find_element(by=By.XPATH,value='//select[@id="CLASEPLACARSGO"]').click()
            driver.find_element(by=By.XPATH,value='//select[@id="CLASEPLACARSGO"]').send_keys("c")
        if flag_c=="1":
            driver.find_element(by=By.XPATH,value='//select[@id="CLASEPLACARSGO"]').click()
            driver.find_element(by=By.XPATH,value='//select[@id="CLASEPLACARSGO"]').send_keys("cc")
        #Segundo tipo de placa
        driver.find_element(by=By.XPATH,value='//select[@id="CLASEPLACA2RSGO"]').click()
        driver.find_element(by=By.XPATH,value='//select[@id="CLASEPLACA2RSGO"]').send_keys("p")
        #Tipo de combustible
        driver.find_element(by=By.XPATH,value='//select[@id="TIPOCOMBUSTRSGO"]').click()
        driver.find_element(by=By.XPATH,value='//select[@id="TIPOCOMBUSTRSGO"]').send_keys(tabla[3])
        #Año
        driver.find_element(by=By.XPATH,value='//input[@id="ANIORSGO"]').clear()
        driver.find_element(by=By.XPATH,value='//input[@id="ANIORSGO"]').send_keys(tabla[5])
        #Valor asegurado
        driver.find_element(by=By.XPATH,value='//input[@id="VALDECRSGO"]').send_keys(price)
        #Capacidad
        driver.find_element(by=By.XPATH,value='//input[@id="CAPACIDADRSGO"]').clear()
        driver.find_element(by=By.XPATH,value='//input[@id="CAPACIDADRSGO"]').send_keys(tabla[9])
        #Peso
        driver.find_element(by=By.XPATH,value='//input[@id="PESORSGO"]').send_keys(tabla[8])
        #Placa
        driver.find_element(by=By.XPATH,value='//input[@name="ctl00$INSContent$ctrDinamico$NUMPLACARSGO$ctl04"]').send_keys(plate)
        #Coberturas C Y DFH
        driver.find_element(by=By.XPATH,value='//select[@id="DUMMYDEDDFH"]').click()
        driver.find_element(by=By.XPATH,value='//select[@id="DUMMYDEDDFH"]').send_keys('f')
        driver.find_element(by=By.XPATH,value='//select[@id="DUMMYDEDC"]').click()
        driver.find_element(by=By.XPATH,value='//select[@id="DUMMYDEDC"]').send_keys('f')
        #Seleccion de las coberturas
        coberturas=driver.find_element(by=By.XPATH,value='(//a[@class="btn btn-default"])[3]')
        a.move_to_element(coberturas).perform()
        driver.find_element(by=By.XPATH,value='(//a[@class="btn btn-default"])[1]').click()
        driver.find_element(by=By.XPATH,value='//select[@id="LIMITEMINIMOA"]').click()
        driver.find_element(by=By.XPATH,value='//select[@id="LIMITEMINIMOA"]').send_keys("25")
        driver.find_element(by=By.XPATH,value='(//a[@class="btn btn-default"])[3]').click()
        driver.find_element(by=By.XPATH,value='//select[@id="LIMITEMINIMOC"]').click()
        driver.find_element(by=By.XPATH,value='//select[@id="LIMITEMINIMOC"]').send_keys("100")
        while True:
            try:
                driver.get_window_size()
                time.sleep(0.2)
            except WebDriverException:
                break

class lafise():
    def cotizar(id,flag_cl,flag_c,price,tabla,plate,flag_comercial,tipo_cedula):
        url_lafise="https://appscr.seguroslafise.com/cotizador_de_seguros/automovil"
        driver=webdriver.Edge(service=Service(EdgeChromiumDriverManager().install()))
        driver.get(url_lafise)
        driver.maximize_window()
        a=ActionChains(driver)
        #Plan        
        driver.find_element(by=By.XPATH,value='//input[@id="Plan-selectized"]').click()
        driver.find_element(by=By.XPATH,value='//input[@id="Plan-selectized"]').send_keys("seguro")
        driver.find_element(by=By.XPATH,value='//div[@data-value="335"]').click()
        #Cuotas
        driver.find_element(by=By.XPATH,value='//input[@id="Cuotas-selectized"]').send_keys("seme")
        driver.find_element(by=By.XPATH,value='(//div[@data-value="2"])[1]').click()
        #Productor
        driver.find_element(by=By.XPATH,value='//input[@id="Productor-selectized"]').send_keys("confi")
        driver.find_element(by=By.XPATH,value='//div[@data-value="122"]').click()
        #Sub Agente
        driver.find_element(by=By.XPATH,value='//input[@id="subAgente-selectized"]').send_keys("alonso")
        driver.find_element(by=By.XPATH,value='//div[@data-value="156949"]').click()
        #Siguiente
        driver.find_element(by=By.XPATH,value='(//button[@class="waves-effect waves-dark btn blue next-step"])[1]').click()
        #Marca
        time.sleep(1)
        driver.find_element(by=By.XPATH,value='//input[@id="cmarca-selectized"]').click()
        driver.find_element(by=By.XPATH,value='//input[@id="cmarca-selectized"]').send_keys(tabla[0])
        driver.find_element(by=By.XPATH,value='//input[@id="cmarca-selectized"]').send_keys(Keys.ENTER)
        #Modelo
        driver.find_element(by=By.XPATH,value='//input[@id="cmodelo-selectized"]').send_keys(tabla[1])
        driver.find_element(by=By.XPATH,value='//input[@id="cmodelo-selectized"]').send_keys(Keys.ENTER)
        #Año
        driver.find_element(by=By.XPATH,value='//input[@id="auAnio-selectized"]').send_keys(tabla[5])
        driver.find_element(by=By.XPATH,value='//input[@id="auAnio-selectized"]').send_keys(Keys.ENTER)
        
        #Valor
        driver.find_element(by=By.XPATH,value='//input[@id="auValorNuevo"]').send_keys(str(price)+"00")
        driver.find_element(by=By.XPATH,value='//input[@id="auValorNuevo"]').send_keys(Keys.ENTER)

        #Deducible
        driver.find_element(by=By.XPATH,value='//input[@id="ideducible-selectized"]').click()
        driver.find_element(by=By.XPATH,value='//input[@id="ideducible-selectized"]').send_keys(300)
        driver.find_element(by=By.XPATH,value='//input[@id="ideducible-selectized"]').send_keys(Keys.ENTER)
        
        #Uso 
        campo_precio = driver.find_element(by=By.XPATH,value='//input[@id="auValorNuevo"]')
        a.move_to_element(campo_precio).move_by_offset(-350, 0).click().perform()
        pyautogui.hotkey('backspace')
        
        driver.find_element(by=By.XPATH,value='//input[@id="auUso-selectized"]').click()
        #Condicional Carga
        if flag_c=="1":
            driver.find_element(by=By.XPATH,value='//input[@id="auUso-selectized"]').send_keys("carga pesada")
        #Condicional Carga liviana
        if flag_cl=="1" and flag_comercial!="1":
            driver.find_element(by=By.XPATH,value='//input[@id="auUso-selectized"]').send_keys("carga liviana uso pe")
        elif flag_cl=="1" and flag_comercial=="1":
            driver.find_element(by=By.XPATH,value='//input[@id="auUso-selectized"]').send_keys("liviana uso com")
        #Condicional Particular
        if flag_c!="1" and flag_cl!="1" and flag_comercial!="1":
            driver.find_element(by=By.XPATH,value='//input[@id="auUso-selectized"]').send_keys("particular uso per")
        elif flag_c!="1" and flag_cl!="1" and flag_comercial=="1":
            driver.find_element(by=By.XPATH,value='//input[@id="auUso-selectized"]').send_keys("particular uso com")
        driver.find_element(by=By.XPATH,value='//input[@id="auUso-selectized"]').send_keys(Keys.ENTER)
        #Coberturas
        driver.find_element(by=By.XPATH,value='(//td[@class="ckbox"])[1]').click()
        driver.find_element(by=By.XPATH,value='(//td[@class="ckbox"])[2]').click()
        driver.find_element(by=By.XPATH,value='(//td[@class="ckbox"])[3]').click()
        driver.find_element(by=By.XPATH,value='(//td[@class="ckbox"])[7]').click()
        driver.find_element(by=By.XPATH,value='(//td[@class="ckbox"])[8]').click()
        driver.find_element(by=By.XPATH,value='(//td[@class="ckbox"])[11]').click()
        #Modificando cobertura B
        driver.find_element(by=By.XPATH,value='//a[@id="CobSA62"]').click()
        driver.find_element(by=By.XPATH,value='//select[@class="form-control input-sm"]').click()
        driver.find_element(by=By.XPATH,value='//option[@value="50000000"]').click()
        #Decuento
        driver.find_element(by=By.XPATH,value='//div[@class="spin-icon"]').click()
        time.sleep(0.5)
        driver.find_element(by=By.XPATH,value='//a[@title="Click para agregar descuento"]').click()
        driver.find_element(by=By.XPATH,value='(//label[@class="form-check-label"])[15]').click()
        driver.find_element(by=By.XPATH,value='//a[@data-name="desc2"]').click()
        driver.find_element(by=By.XPATH,value='//input[@class="form-control input-sm"]').clear()
        driver.find_element(by=By.XPATH,value='//input[@class="form-control input-sm"]').send_keys(35)
        driver.find_element(by=By.XPATH,value='//input[@class="form-control input-sm"]').send_keys(Keys.ENTER)
        driver.find_element(by=By.XPATH,value='(//button[@class="btn btn-primary btn-mg-4 waves-effect waves-light"])[1]').click()
        while True:
            try:
                driver.get_window_size()
                time.sleep(0.2)
            except WebDriverException:
                break

class qualitas():
    def cotizar(id,flag_cl,flag_c,price,tabla,plate,flag_comercial,tipo_cedula):
        url_qualitas="https://www.qualitas.co.cr/web/qcr/acceso-agentes"
        driver=webdriver.Edge(service=Service(EdgeChromiumDriverManager().install()))
        driver.get(url_qualitas)
        driver.maximize_window()
        a=ActionChains(driver)
        time.sleep(1)
        #Login
        driver.find_element(by=By.XPATH,value='//input[@name="_58_clave"]').click()
        driver.find_element(by=By.XPATH,value='//input[@name="_58_clave"]').send_keys()
        driver.find_element(by=By.XPATH,value='//input[@name="_58_loginn"]').click()
        driver.find_element(by=By.XPATH,value='//input[@name="_58_loginn"]').send_keys('')
        driver.find_element(by=By.XPATH,value='//input[@name="_58_password"]').click()
        driver.find_element(by=By.XPATH,value='//input[@name="_58_password"]').send_keys('CONFIA')
        driver.find_element(by=By.XPATH,value='//button[@class="btn btn-modificado btn-modificado_2"]').click()
        #Entrando al cotizador
        driver.find_element(by=By.XPATH,value='//a[@href="https://www.qualitas.co.cr/group/qcr/cotizador"]').click()
        #Marca
        driver.find_element(by=By.XPATH,value='//select[@id="marca"]').click()
        driver.find_element(by=By.XPATH,value='//select[@id="marca"]').send_keys(tabla[0])
        driver.find_element(by=By.XPATH,value='//select[@id="marca"]').send_keys(Keys.ENTER)
        #Tipo
        driver.find_element(by=By.XPATH,value='//select[@id="tipo"]').click()
        driver.find_element(by=By.XPATH,value='//select[@id="tipo"]').send_keys(tabla[1])
        driver.find_element(by=By.XPATH,value='//select[@id="tipo"]').send_keys(Keys.ENTER)
        #Modelo/año 
        driver.find_element(by=By.XPATH,value='//select[@id="modelo"]').click()
        driver.find_element(by=By.XPATH,value='//select[@id="modelo"]').send_keys(tabla[5])
        driver.find_element(by=By.XPATH,value='//select[@id="modelo"]').send_keys(Keys.ENTER)
        #Monto asegurado
        time.sleep(2.5)
        driver.find_element(by=By.XPATH,value='//input[@id="sumaAsegurada"]').click()
        driver.find_element(by=By.XPATH,value='//input[@id="sumaAsegurada"]').clear()
        driver.find_element(by=By.XPATH,value='//input[@id="sumaAsegurada"]').send_keys(price)
        while True:
            try:
                driver.get_window_size()
                time.sleep(0.2)
            except WebDriverException:
                break

class oceanica():
    def cotizar(id,flag_cl,flag_c,price,tabla,plate,flag_comercial,tipo_cedula):
        url_oceanica="http://portal.oceanica-cr.com/oceanicaweb/"
        driver=webdriver.Edge(service=Service(EdgeChromiumDriverManager().install()))
        driver.get(url_oceanica)
        driver.maximize_window()
        a=ActionChains(driver)
        #Login
        driver.find_element(by=By.XPATH,value='//input[@id="username"]').click()
        driver.find_element(by=By.XPATH,value='//input[@id="username"]').send_keys('')
        driver.find_element(by=By.XPATH,value='//input[@id="password"]').click()
        driver.find_element(by=By.XPATH,value='//input[@id="password"]').send_keys('')
        driver.find_element(by=By.XPATH,value='//button[@type="submit"]').click()
        #Seleccion de la poliza
        time.sleep(1)
        driver.find_element(by=By.XPATH,value='//i[@class="vial"]').click()
        #Saltando alerta
        time.sleep(1)
        alert = driver.switch_to.alert
        alert.accept()
        #Saltando pop up
        time.sleep(2)
        body=driver.find_element(by=By.XPATH,value='//img[@class="img-responsive"]')
        a.move_to_element(body).move_by_offset(600,0).click().perform()
        #Marca
        driver.find_element(by=By.XPATH,value='//select[@id="sMarca"]').click()
        driver.find_element(by=By.XPATH,value='//select[@id="sMarca"]').send_keys(tabla[0])
        driver.find_element(by=By.XPATH,value='//select[@id="sMarca"]').send_keys(Keys.ENTER)
        #Modelo
        driver.find_element(by=By.XPATH,value='//select[@id="sModelo"]').click()
        driver.find_element(by=By.XPATH,value='//select[@id="sModelo"]').send_keys(tabla[1])
        driver.find_element(by=By.XPATH,value='//select[@id="sModelo"]').send_keys(Keys.ENTER)
        #Año
        driver.find_element(by=By.XPATH,value='//input[@id="iAnio"]').click()
        driver.find_element(by=By.XPATH,value='//input[@id="iAnio"]').send_keys(tabla[5])
        #Monto
        driver.find_element(by=By.XPATH,value='//input[@id="iMontoFactura"]').click()
        driver.find_element(by=By.XPATH,value='//input[@id="iMontoFactura"]').send_keys(price)
        #Cedula
        driver.find_element(by=By.XPATH,value='//input[@id="solNumid"]').click()
        driver.find_element(by=By.XPATH,value='//input[@id="solNumid"]').send_keys(id)
        #Tipo de id
        driver.find_element(by=By.XPATH,value='//select[@id="solTipoid"]').click()
        driver.find_element(by=By.XPATH,value='//select[@id="solTipoid"]').send_keys(tipo_cedula)
        driver.find_element(by=By.XPATH,value='//select[@id="sUso"]').send_keys(Keys.ENTER)
        #Datos del cliente
        if tipo_cedula=="Cédula física":
            cliente=info.info.tse(id)
            #Fecha de nacimiento
            driver.find_element(by=By.XPATH,value='//input[@id="iFechaNacimiento"]').click()
            driver.find_element(by=By.XPATH,value='//input[@id="iFechaNacimiento"]').send_keys(cliente[0])
            #Apellido
            driver.find_element(by=By.XPATH,value='//input[@id="iApellido"]').click()
            driver.find_element(by=By.XPATH,value='//input[@id="iApellido"]').send_keys(cliente[-2]," ",cliente[-1])
            #Nombre
            nombre=""
            for i in range(1,len(cliente)-2,1):
                nombre+=str(cliente[i])+" "
            driver.find_element(by=By.XPATH,value='//input[@id="iNombre"]').click()
            driver.find_element(by=By.XPATH,value='//input[@id="iNombre"]').send_keys(nombre)
        #Uso
        driver.find_element(by=By.XPATH,value='//select[@id="sUso"]').click()
        if flag_comercial!="1": 
            driver.find_element(by=By.XPATH,value='//select[@id="sUso"]').send_keys("")
        else:
            driver.find_element(by=By.XPATH,value='//select[@id="sUso"]').send_keys("")
        driver.find_element(by=By.XPATH,value='//select[@id="sUso"]').send_keys(Keys.ENTER)
        WebDriverWait(driver, 20000).until(EC.presence_of_element_located((By.XPATH, '//select[@id="rango-500-009-COA3"]')))
        move=driver.find_element(by=By.XPATH,value='//select[@id="rango-500-009-COA3"]')
        a.move_to_element(move)
        try:
            driver.find_element(by=By.XPATH,value='//select[@id="rango-500-009-COA3"]').click()
            driver.find_element(by=By.XPATH,value='//select[@id="rango-500-009-COA3"]').send_keys(240)
            driver.find_element(by=By.XPATH,value='//select[@id="rango-500-043-COA3"]').click()
            driver.find_element(by=By.XPATH,value='//select[@id="rango-500-043-COA3"]').send_keys(240)
            driver.find_element(by=By.XPATH,value='//select[@id="rango-500-044-COA3"]').click()
            driver.find_element(by=By.XPATH,value='//select[@id="rango-500-044-COA3"]').send_keys(240)
            driver.find_element(by=By.XPATH,value='//select[@id="rango-500-044-COA3"]').click()
            driver.find_element(by=By.XPATH,value='//select[@id="rango-500-044-COA3"]').send_keys(240)
        except:
            pass
        try:
            driver.find_element(by=By.XPATH,value='//a[@id="gd-dedu-500-009"]').click()
            driver.find_element(by=By.XPATH,value='//a[@id="gd-dedu-500-043"]').click()
            driver.find_element(by=By.XPATH,value='//a[@id="gd-dedu-500-044""]').click()
            driver.find_element(by=By.XPATH,value='//a[@id="rango-500-009-COA3"]').click()
        except:
            pass

        while True:
            try:
                driver.get_window_size()
                time.sleep(0.2)
            except WebDriverException:
                break
        
class paralelo():
    def cotizar(id,flag_cl,flag_c,price,tabla,plate,flag_comercial,tipo_cedula):
        multiprocessing.freeze_support()
        try:
            clases = [ins,qualitas,oceanica,lafise]
            Parallel(n_jobs=-1,backend='threading')(delayed(i.cotizar)(id,flag_cl,flag_c,price,tabla,plate,flag_comercial,tipo_cedula)for i in clases)
        except WebDriverException:
            print("Webdriver")




from tkinter import *
from selenium import webdriver #Crear navegador
from selenium.webdriver.edge.service import Service #Aplicar el navegador
from webdriver_manager.microsoft import EdgeChromiumDriverManager #Navegador
from selenium.webdriver.common.by import By #Buscado
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from joblib import Parallel, delayed
import info
import time

class ins():
    def cotizar(id,flag_cl,flag_c,price,tabla,plate,flag_comercial):
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
        time.sleep(2000)

class lafise():
    def cotizar(id,flag_cl,flag_c,price,tabla,plate,flag_comercial):
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
        #Uso
        driver.find_element(by=By.XPATH,value='//input[@id="auUso-selectized"]').click()
        #Condicional Carga
        if flag_c=="1":
            driver.find_element(by=By.XPATH,value='//input[@id="auUso-selectized"]').send_keys("carga pesada")
        #Condicional Carga liviana
        if flag_c=="1" and flag_comercial!="1":
            driver.find_element(by=By.XPATH,value='//input[@id="auUso-selectized"]').send_keys("carga liviana uso pe")
        elif flag_c=="1" and flag_comercial=="1":
            driver.find_element(by=By.XPATH,value='//input[@id="auUso-selectized"]').send_keys("carga liviana uso com")
        #Condicional Particular
        if flag_c!="1" and flag_cl!="1" and flag_comercial!="1":
            driver.find_element(by=By.XPATH,value='//input[@id="auUso-selectized"]').send_keys("particular uso per")
        elif flag_c!="1" and flag_cl!="1" and flag_comercial=="1":
            driver.find_element(by=By.XPATH,value='//input[@id="auUso-selectized"]').send_keys("particular uso com")
        driver.find_element(by=By.XPATH,value='//input[@id="auUso-selectized"]').send_keys(Keys.ENTER)
        #Modelo
        driver.find_element(by=By.XPATH,value='//input[@id="cmodelo-selectized"]').send_keys(tabla[1])
        driver.find_element(by=By.XPATH,value='//input[@id="cmodelo-selectized"]').send_keys(Keys.ENTER)
        #Año
        driver.find_element(by=By.XPATH,value='//input[@id="auAnio-selectized"]').send_keys(tabla[5])
        driver.find_element(by=By.XPATH,value='//input[@id="auAnio-selectized"]').send_keys(Keys.ENTER)
        #Valor
        driver.find_element(by=By.XPATH,value='//input[@id="auValorNuevo"]').send_keys(price*100)
        driver.find_element(by=By.XPATH,value='//input[@id="auValorNuevo"]').send_keys(Keys.ENTER)
        #Deducible
        driver.find_element(by=By.XPATH,value='//input[@id="ideducible-selectized"]').click()
        driver.find_element(by=By.XPATH,value='//input[@id="ideducible-selectized"]').send_keys(300)
        driver.find_element(by=By.XPATH,value='//input[@id="ideducible-selectized"]').send_keys(Keys.ENTER)
        #Coberturaas
        driver.find_element(by=By.XPATH,value='(//td[@class="ckbox"])[1]').click()
        driver.find_element(by=By.XPATH,value='(//td[@class="ckbox"])[2]').click()
        driver.find_element(by=By.XPATH,value='(//td[@class="ckbox"])[3]').click()
        driver.find_element(by=By.XPATH,value='(//td[@class="ckbox"])[7]').click()
        driver.find_element(by=By.XPATH,value='(//td[@class="ckbox"])[8]').click()
        driver.find_element(by=By.XPATH,value='(//td[@class="ckbox"])[11]').click()
        time.sleep(2000)

class qualitas():
    def cotizar(id,flag_cl,flag_c,price,tabla,plate,flag_comercial):
        url_qualitas="https://www.qualitas.co.cr/web/qcr/acceso-agentes"
        driver=webdriver.Edge(service=Service(EdgeChromiumDriverManager().install()))
        driver.get(url_qualitas)
        driver.maximize_window()
        a=ActionChains(driver)
        time.sleep(1)
        #Login
        driver.find_element(by=By.XPATH,value='//input[@name="_58_clave"]').click()
        driver.find_element(by=By.XPATH,value='//input[@name="_58_clave"]').send_keys(2)
        driver.find_element(by=By.XPATH,value='//input[@name="_58_loginn"]').click()
        driver.find_element(by=By.XPATH,value='//input[@name="_58_loginn"]').send_keys('Comercial')
        driver.find_element(by=By.XPATH,value='//input[@name="_58_password"]').click()
        driver.find_element(by=By.XPATH,value='//input[@name="_58_password"]').send_keys('CONFIA')
        driver.find_element(by=By.XPATH,value='//button[@class="btn btn-modificado btn-modificado_2"]').click()
        time.sleep(2000)

class oceanica():
    def cotizar(id,flag_cl,flag_c,price,tabla,plate,flag_comercial):
        cliente=info.info.tse(id)
        url_oceanica="http://portal.oceanica-cr.com/oceanicaweb/"
        driver=webdriver.Edge(service=Service(EdgeChromiumDriverManager().install()))
        driver.get(url_oceanica)
        driver.maximize_window()
        a=ActionChains(driver)
        #Login
        driver.find_element(by=By.XPATH,value='//input[@id="username"]').click()
        driver.find_element(by=By.XPATH,value='//input[@id="username"]').send_keys('CO-000031')
        driver.find_element(by=By.XPATH,value='//input[@id="password"]').click()
        driver.find_element(by=By.XPATH,value='//input[@id="password"]').send_keys('SQJDrxPE')
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
        driver.find_element(by=By.XPATH,value='//select[id="sModelo"]').click()
        driver.find_element(by=By.XPATH,value='//select[id="sModelo"]').send_keys(tabla[1])
        driver.find_element(by=By.XPATH,value='//select[id="sModelo"]').send_keys(Keys.ENTER)
        #Año
        driver.find_element(by=By.XPATH,value='//input[@id="iAnio"]').click()
        driver.find_element(by=By.XPATH,value='//input[@id="iAnio"]').send_keys(tabla[5])
        time.sleep(2000)
        #Monto
        driver.find_element(by=By.XPATH,value='//input[id="iMontoFactura"]').click()
        driver.find_element(by=By.XPATH,value='//input[id="iMontoFactura"]').send_keys(tabla[5])
        
        
#[ins,lafise,qualitas]
class paralelo():
    def cotizar(id,flag_cl,flag_c,price,tabla,plate,flag_comercial):
        clases = [ins,qualitas,lafise,oceanica]
        Parallel(n_jobs=-1)(delayed(i.cotizar)(id,flag_cl,flag_c,price,tabla,plate,flag_comercial)for i in clases)

tabla = ['NISSAN', 'TIIDA', '1798 ', 'GASOLINA', 'SEDAN   HATCHBACK4X2', '2012', 'SENAJUUNO NUEVE CERO TRES SOCIEDAD ANONIMA ', '4X2', '1588', '5']
oceanica.cotizar("110650128","0",'0',4600000,tabla,"wtf003","0")





        

        

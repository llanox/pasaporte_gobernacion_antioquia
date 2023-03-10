import time

from selenium import webdriver
import schedule
import os
import sys

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

URL_REAL = 'https://sedeelectronica.antioquia.gov.co/pasaporte/user/pago/'
URL_TEST = 'file://' + os.getcwd() + '/test/payment_webhtml.html'
URL_REQUEST_PAYMENT_FORM = URL_TEST
PATH_SCREENSHOT_PAYMENT_PAGE = os.getcwd() + '/screenshots/payment_form.png'
PATH_SCREENSHOT_ERROR_PAGE = os.getcwd() + '/screenshots/payment_error.png'
PATH_PAYMENT_HTML = os.getcwd() + '/website/payment_webhtml.html'
EXECUTE_EVERY_N_SECS = 7

# Aquí van los datos del solicitante
REQUESTER_NAMES = 'Juan Manuel'
REQUESTER_LAST_NAME = 'Jaramillo Aristizabal'
REQUESTER_CC = '000000000'  # Número de cédula
REQUESTER_MOBILE = '3100000000'
REQUESTER_EMAIL = 'juan.manuel.jaramillo@yopmail.com'

job_running = True


# Solo funciona con MACOSX si se tiene configurado el speaker Mónica
def say(msg="Finish", voice="Mónica"):
    if sys.platform == 'darwin':
        os.system(f'say -v {voice} {msg}')
    else:
        print(msg)


# En caso de que falle, se almacena para saber si algo cambio en el form que pueda afectar la
# ejecución del script.
def save_payment_page(driver):
    driver.save_screenshot(PATH_SCREENSHOT_PAYMENT_PAGE)
    page_source = driver.page_source
    file = open(PATH_PAYMENT_HTML, "w")  # open file in binary mode
    print(page_source)
    file.writelines(page_source)
    file.close()


def fill_out_payment_form(driver):
    save_payment_page(driver)

    select_tipo_id = Select(driver.find_element(By.NAME, 'data[tipo_ide]'))
    select_tipo_id.select_by_value('CC')

    input_cedula = driver.find_element(By.ID, "num_ide")
    input_cedula.send_keys(REQUESTER_CC)

    confirm_input_cedula = driver.find_element(By.ID, "num_ide_confirm")
    confirm_input_cedula.send_keys(REQUESTER_CC)

    input_nombres = driver.find_element(By.ID, "nombre")
    input_nombres.send_keys(REQUESTER_NAMES)

    input_apellidos = driver.find_element(By.ID, "apellido")
    input_apellidos.send_keys(REQUESTER_LAST_NAME)

    input_mobile = driver.find_element(By.ID, "mobile")
    input_mobile.send_keys(REQUESTER_MOBILE)

    input_email = driver.find_element(By.ID, "email")
    input_email.send_keys(REQUESTER_EMAIL)

    confirm_input_email = driver.find_element(By.ID, "email_confirm")
    confirm_input_email.send_keys(REQUESTER_EMAIL)

    select_tipo_passport = Select(driver.find_element(By.NAME, 'data[opc]'))
    select_tipo_passport.select_by_value('5c5a446a15ab22a64d531d80704d4d88d5928a0a')

    checkbox_acepto = driver.find_element(By.ID, 'acepto')
    checkbox_acepto.click()

    input_submit_form = driver.find_element(By.ID, "form-pago")
    input_submit_form.click()


def check_page():
    driver = webdriver.Firefox()
    driver.get(URL_REQUEST_PAYMENT_FORM)
    is_payment_form = "Realice el pago de su pasaporte" in driver.page_source
    if is_payment_form:
        say("Página de Pago")
        fill_out_payment_form(driver)
        quit()
        global job_running
        job_running = False
        return schedule.CancelJob
    else:
        print("Mostrando notificación de no posibilidad de pago")
        # siempre que no muestre el formulario de pago, guarda un screenshot de la ventana actual
        driver.save_screenshot(PATH_SCREENSHOT_ERROR_PAGE)
        driver.close()


schedule.every(EXECUTE_EVERY_N_SECS).seconds.do(check_page)
while job_running:
    schedule.run_pending()
    time.sleep(1)

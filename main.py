from dotenv import load_dotenv
import os
# Error libs
from selenium.common.exceptions import WebDriverException
# selenium
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium import webdriver
# excel lib
import openpyxl

print("....Start....")

load_dotenv()

# op = Options 
# AttributeError: type object 'Options' has no attribute '_ignore_local_proxy'
#opitions.headless = True <- Hability to run in server"

# try:
# configure and define webdriver
service = Service(os.getenv("DRIVER_PATH"))
driver = webdriver.Chrome(service=service)
driver.get("https://buscacepinter.correios.com.br/app/endereco/index.php")
driver.maximize_window()
# except WebDriverException :
#     print("\n\n\n","ERROR: Verify you crhomedriver driver version and yor connection","\n\n\n")


# open excel
zip_code_without_address = openpyxl.load_workbook("excel\excel_desatualizado.xlsx")
# select page
planilha1 = zip_code_without_address["planilha 1"]
# storage zip codes in list
zip_code_list=[row[0].value for row in planilha1.iter_rows(min_row=2, max_row=11)]
# print("row", len(zip_code_list), zip_code_list)

import time
def send_zip_codes(driver,zip_code_list):
    for cep in zip_code_list:
        driver.find_element(By.ID, "endereco").send_keys(f"{cep}" + Keys.ENTER)
        print(type(cep))
        #mensagem-resultado 69912-655
        try:
            
        except:

        time.sleep(5)
        driver.find_element(By.ID, "btn_nbusca").click()

    return

send_zip_codes(driver, zip_code_list)

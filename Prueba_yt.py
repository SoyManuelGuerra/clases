from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


#instaciamos el driver de chrome
driver = webdriver.Chrome()

#navega por la url
driver.get("https://www.google.com")

#maximizar ventana
driver.maximize_window()

#buscar elemento  por su nombre
search_box = driver.find_element(By.NAME,"q")
search_box.click()
search_box.send_keys("Slipknot"+Keys.ENTER)
#hace clik 
search_video = driver.find_element(By.LINK_TEXT, "Videos").click()
play_video = driver.find_element(By.PARTIAL_LINK_TEXT, "Slipknot - Psychosocial")
play_video.click()

driver.minimize_window()
#se espera por mas tiempoo
time.sleep(120)

driver.quit()
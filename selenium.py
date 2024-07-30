from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time


options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)


driver = webdriver.Chrome(options=options, service=Service(ChromeDriverManager().install()))


html_file_path = "https://incredible-vacherin-7d6258.netlify.app/"


driver.get(html_file_path)


driver.maximize_window()


time.sleep(2)  


username_field = driver.find_element(By.ID, 'username')
time.sleep(2)
password_field = driver.find_element(By.ID, 'password')
time.sleep(2)


username_field.send_keys('user')
password_field.send_keys('password')


login_button = driver.find_element(By.CSS_SELECTOR, 'input[type="submit"]')
time.sleep(2)
login_button.click()


time.sleep(5)


dash_file_path = "file:///C:/Users/amith/OneDrive/Desktop/inventry%20managment/dash.html "
driver.get(dash_file_path)
time.sleep(2)  


driver.maximize_window()


driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(2) 


driver.execute_script("window.scrollTo(0, 0);")
time.sleep(2) 


def add_to_current_inventory(name, brand, quantity, price):
    driver.find_element(By.ID, 'current_order_product_name').send_keys(name)
    driver.find_element(By.ID, 'current_order_product_brand').send_keys(brand)
    driver.find_element(By.ID, 'current_order_product_quantity').send_keys(quantity)
    driver.find_element(By.ID, 'current_order_product_price').send_keys(price)
    driver.find_element(By.CSS_SELECTOR, 'button[onclick="addCurrentInventory()"]').click()
    time.sleep(2) 




def add_to_incoming_purchase(name, brand, quantity, price):
    driver.find_element(By.ID, 'profile-tab').click()
    time.sleep(2) 
    driver.find_element(By.ID, 'incoming_order_product_name').send_keys(name)
    driver.find_element(By.ID, 'incoming_order_product_brand').send_keys(brand)
    driver.find_element(By.ID, 'incoming_order_product_quantity').send_keys(quantity)
    driver.find_element(By.ID, 'incoming_order_product_price').send_keys(price)
    driver.find_element(By.CSS_SELECTOR, 'button[onclick="addIncomingOrder()"]').click()
    time.sleep(2)  


def add_to_outgoing_orders(name, brand, quantity, price):
    driver.find_element(By.ID, 'contact-tab').click()
    time.sleep(2)  
    driver.find_element(By.ID, 'outgoing_order_product_name').send_keys(name)
    driver.find_element(By.ID, 'outgoing_order_product_brand').send_keys(brand)
    driver.find_element(By.ID, 'outgoing_order_product_quantity').send_keys(quantity)
    driver.find_element(By.ID, 'outgoing_order_product_price').send_keys(price)
    driver.find_element(By.CSS_SELECTOR, 'button[onclick="addOutgoingOrder()"]').click()
    time.sleep(2)  




add_to_current_inventory('Product1', 'Brand1', '10', '100')
add_to_current_inventory('Product2', 'Brand2', '20', '200')


driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(5) 


add_to_incoming_purchase('Product3', 'Brand3', '30', '300')
add_to_incoming_purchase('Product4', 'Brand4', '40', '400')


driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(5)  


add_to_outgoing_orders('Product5', 'Brand5', '50', '500')
add_to_outgoing_orders('Product6', 'Brand6', '60', '600')
time.sleep(5)


driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(2)



time.sleep(5)


driver.quit()

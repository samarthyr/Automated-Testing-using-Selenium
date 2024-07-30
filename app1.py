from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

# Set up Chrome options
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

# Initialize WebDriver using webdriver_manager
driver = webdriver.Chrome(options=options, service=Service(ChromeDriverManager().install()))

# Replace this with the actual path to your HTML file
html_file_path = "https://incredible-vacherin-7d6258.netlify.app/"

# Open the HTML file
driver.get(html_file_path)

# Maximize the window to ensure full scrolling
driver.maximize_window()

# Wait for the page to load completely
time.sleep(2)  # Adjust this sleep time as necessary

# Locate the username and password fields
username_field = driver.find_element(By.ID, 'username')
time.sleep(2)
password_field = driver.find_element(By.ID, 'password')
time.sleep(2)

# Input the hardcoded username and password
username_field.send_keys('user')
password_field.send_keys('password')

# Locate and click the login button
login_button = driver.find_element(By.CSS_SELECTOR, 'input[type="submit"]')
time.sleep(2)
login_button.click()

# Wait for a few seconds to ensure the login is processed
time.sleep(5)

# Open the dashboard HTML file
dash_file_path = "file:///C:/Users/amith/OneDrive/Desktop/inventry%20managment/dash.html "
driver.get(dash_file_path)
time.sleep(2)  # Adjust this sleep time as necessary

# Maximize the window to ensure full scrolling
driver.maximize_window()

# Scroll down the page
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(2)  # Wait for a few seconds to observe the scroll down

# Scroll up the page
driver.execute_script("window.scrollTo(0, 0);")
time.sleep(2)  # Wait for a few seconds to observe the scroll up

# Function to add a product to the current inventory
def add_to_current_inventory(name, brand, quantity, price):
    driver.find_element(By.ID, 'current_order_product_name').send_keys(name)
    driver.find_element(By.ID, 'current_order_product_brand').send_keys(brand)
    driver.find_element(By.ID, 'current_order_product_quantity').send_keys(quantity)
    driver.find_element(By.ID, 'current_order_product_price').send_keys(price)
    driver.find_element(By.CSS_SELECTOR, 'button[onclick="addCurrentInventory()"]').click()
    time.sleep(2)  # Adjust this sleep time as necessary



# Function to add a product to the incoming purchase
def add_to_incoming_purchase(name, brand, quantity, price):
    driver.find_element(By.ID, 'profile-tab').click()
    time.sleep(2)  # Adjust this sleep time as necessary
    driver.find_element(By.ID, 'incoming_order_product_name').send_keys(name)
    driver.find_element(By.ID, 'incoming_order_product_brand').send_keys(brand)
    driver.find_element(By.ID, 'incoming_order_product_quantity').send_keys(quantity)
    driver.find_element(By.ID, 'incoming_order_product_price').send_keys(price)
    driver.find_element(By.CSS_SELECTOR, 'button[onclick="addIncomingOrder()"]').click()
    time.sleep(2)  # Adjust this sleep time as necessary

# Function to add a product to the outgoing orders
def add_to_outgoing_orders(name, brand, quantity, price):
    driver.find_element(By.ID, 'contact-tab').click()
    time.sleep(2)  # Adjust this sleep time as necessary
    driver.find_element(By.ID, 'outgoing_order_product_name').send_keys(name)
    driver.find_element(By.ID, 'outgoing_order_product_brand').send_keys(brand)
    driver.find_element(By.ID, 'outgoing_order_product_quantity').send_keys(quantity)
    driver.find_element(By.ID, 'outgoing_order_product_price').send_keys(price)
    driver.find_element(By.CSS_SELECTOR, 'button[onclick="addOutgoingOrder()"]').click()
    time.sleep(2)  # Adjust this sleep time as necessary



# Add products to the current inventory
add_to_current_inventory('Product1', 'Brand1', '10', '100')
add_to_current_inventory('Product2', 'Brand2', '20', '200')

# Scroll down the page
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(5)  # Wait for a few seconds to observe the scroll down

# Add products to the incoming purchase
add_to_incoming_purchase('Product3', 'Brand3', '30', '300')
add_to_incoming_purchase('Product4', 'Brand4', '40', '400')

# Scroll down the page
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(5)  # Wait for a few seconds to observe the scroll down

# Add products to the outgoing orders
add_to_outgoing_orders('Product5', 'Brand5', '50', '500')
add_to_outgoing_orders('Product6', 'Brand6', '60', '600')
time.sleep(5)

# Scroll down the page
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(2)  # Wait for a few seconds to observe the scroll down


# Wait for a few seconds to observe the result
time.sleep(5)

# Close the browser
driver.quit()

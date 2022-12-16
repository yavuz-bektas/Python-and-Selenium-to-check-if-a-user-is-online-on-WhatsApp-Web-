# Import the necessary libraries
from selenium import webdriver
from selenium.webdriver.common.by import By

# Set the path to the ChromeDriver executable
driver = webdriver.Chrome(executable_path='/path/to/chromedriver')

# Open WhatsApp Web in Chrome
driver.get('https://web.whatsapp.com/')

# Wait for the user to scan the QR code and log in
input("Press Enter after scanning the QR code and logging in")

# Find the user's chat window by their name or phone number
user = "John Doe"  # Change this to the name or phone number of the user
xpath = "//span[@title='{}']".format(user)
user_window = driver.find_element(By.XPATH, xpath)

# Check if the user is online by looking for the green dot next to their name
online_dot = user_window.find_elements(By.XPATH, ".//div[@title='online']")

# Print the result
if online_dot:
    print("User is online")
else:
    print("User is offline")

# Close the browser
driver.quit()

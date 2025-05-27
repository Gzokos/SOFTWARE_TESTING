from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


driver = webdriver.Chrome()

try:
  
    driver.get("file:///C:/Users/gzoko/essay/test2.html")  
    driver.maximize_window()


    driver.find_element(By.ID, "username").send_keys("testuser")
    driver.find_element(By.ID, "password").send_keys("Test@123")
    driver.find_element(By.ID, "login-button").click()
    time.sleep(4)


    driver.find_element(By.XPATH, "//div[text()='Inception']").click()
    time.sleep(4)
    driver.find_element(By.XPATH, "//button[text()='6:00 PM']").click()


    driver.find_element(By.ID, "seat-B4").click()


    driver.find_element(By.ID, "confirm-booking").click()


    confirmation = driver.find_element(By.ID, "confirmation-message").text
    assert "Booking confirmed" in confirmation
    print("Test passed: Booking confirmation displayed.")

except Exception as e:
    print(" Test failed:", e)

finally:
    time.sleep(4)
    driver.quit()

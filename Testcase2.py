from selenium import webdriver
from selenium.webdriver.common.by import By
import re
import time


def is_valid_password(password):
    if len(password) != 8:
        return False
    if not re.search(r"[A-Za-z]", password):
        return False
    if not re.search(r"\d", password):
        return False
    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        return False
    return True

username = "testuser"
password = "Abc@1234"  


if not is_valid_password(password):
    print(" Password validation failed (invalid format)")
else:
    print("Password format valid, continuing with Selenium login...")

 
    driver = webdriver.Chrome()
    try:
        driver.get("file:///C:/Users/gzoko/essay/test2.html")  
        driver.maximize_window()
        time.sleep(1)

        driver.find_element(By.ID, "username").send_keys(username)
        driver.find_element(By.ID, "password").send_keys(password)
        driver.find_element(By.ID, "login-button").click()
        time.sleep(2)

        driver.find_element(By.ID, "movie-inception").click()
        time.sleep(1)

        driver.find_element(By.XPATH, "//button[text()='6:00 PM']").click()
        time.sleep(1)

        driver.find_element(By.ID, "seat-B4").click()
        time.sleep(1)

        driver.find_element(By.ID, "confirm-booking").click()
        time.sleep(2)

        msg = driver.find_element(By.ID, "confirmation-message").text
        assert "Booking confirmed" in msg
        print("Booking flow passed.")

    except Exception as e:
        print("Test failed:", e)

    finally:
        driver.quit()

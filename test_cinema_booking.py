
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os
from datetime import datetime

os.makedirs("screenshots", exist_ok=True)

def take_screenshot(driver, label):
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"screenshots/{timestamp}_{label}.png"
    driver.save_screenshot(filename)

@pytest.fixture
def setup_browser():
    driver = webdriver.Chrome()
    driver.get("file:///C:/Users/gzoko/essay/test2.html")  
    driver.maximize_window()
    yield driver
    driver.quit()

def test_booking_with_screenshots(setup_browser):
    driver = setup_browser
    wait = WebDriverWait(driver, 10)


    driver.find_element(By.ID, "username").send_keys("testuser")
    driver.find_element(By.ID, "password").send_keys("Test@123")
    take_screenshot(driver, "step1_login_filled")
    driver.find_element(By.ID, "login-button").click()
    time.sleep(2)

  
    wait.until(EC.visibility_of_element_located((By.ID, "movie-inception"))).click()
    take_screenshot(driver, "step2_movie_selected")
    time.sleep(2)


    wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='6:00 PM']"))).click()
    take_screenshot(driver, "step3_showtime_selected")
    time.sleep(2)

    wait.until(EC.element_to_be_clickable((By.ID, "seat-B4"))).click()
    take_screenshot(driver, "step4_seat_selected")
    time.sleep(2)

    
    driver.find_element(By.ID, "confirm-booking").click()
    take_screenshot(driver, "step5_booking_confirmed")
    time.sleep(2)

  
    confirmation = driver.find_element(By.ID, "confirmation-message").text
    assert "Booking confirmed" in confirmation
    print(" Booking test passed.")

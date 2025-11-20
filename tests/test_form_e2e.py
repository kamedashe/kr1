from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import pytest

@pytest.fixture
def driver():
    opts = webdriver.ChromeOptions()
    opts.add_argument("--headless=new")
    driver = webdriver.Chrome(options=opts)
    yield driver
    driver.quit()

def submit_and_get_message(driver, url, value):
    driver.get(url)
    input_el = driver.find_element(By.NAME, "value")  # змінити під свій селектор
    input_el.clear()
    input_el.send_keys(value)
    submit = driver.find_element(By.ID, "submit")  # змінити під свій селектор
    submit.click()
    time.sleep(0.3)
    # припускаємо, що повідомлення з валідацією має class 'error' або 'success'
    try:
        return driver.find_element(By.CLASS_NAME, "error").text
    except:
        try:
            return driver.find_element(By.CLASS_NAME, "success").text
        except:
            return ""

def test_ec1_valid(driver):
    msg = submit_and_get_message(driver, "http://localhost:8000/form", "42")
    assert "Успішно" in msg or msg == ""

def test_ec2_too_small(driver):
    msg = submit_and_get_message(driver, "http://localhost:8000/form", "0")
    assert "Число має бути від 1 до 100" in msg

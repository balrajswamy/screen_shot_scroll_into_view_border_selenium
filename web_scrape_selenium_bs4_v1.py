from selenium import webdriver
from selenium.webdriver.common.by import By
import time



def open_browser():
    driver = webdriver.Chrome()

    driver.maximize_window()

    url = 'https://awesomeqa.com/practice.html'

    driver.get(url)
    time.sleep(3)
    driver.find_element(By.XPATH,"//input[@name='firstname']").send_keys("Balraj")
    time.sleep(1)
    driver.find_element(By.XPATH, "//input[@name='lastname']").send_keys("Ponnuswamy")
    time.sleep(3)
    driver.find_element(By.XPATH,"//input[@value='Male']").click()

    time.sleep(3)
    element = driver.find_element(By.XPATH,"//input[@value='Automation Tester']")
    element_screenshot_filename = "element_screenshot.png"
    element.click()
    time.sleep(3)
    element.screenshot(element_screenshot_filename)
    time.sleep(3)
    screen_fullpage_filename = "screenshot_fullpage.png"
    driver.save_screenshot(screen_fullpage_filename)

    time.sleep(6)
    #to scroll to view element
    button_element = driver.find_element(By.XPATH, "//button[@class='btn btn-info']")
    driver.execute_script("arguments[0].scrollIntoView(true);", button_element)

    driver.execute_script("arguments[0].style.border='1px solid red'", button_element)
    time.sleep(10)
    driver.quit()

if __name__ == "__main__":
    open_browser()
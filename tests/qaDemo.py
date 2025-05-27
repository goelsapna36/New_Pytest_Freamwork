import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from conftest import setup_browser

def test_qa_demo(setup_browser):
    driver = setup_browser
    driver.maximize_window()
    wait = WebDriverWait(driver, 10)

    driver.get("https://demoqa.com/")

    # Hide ad that can block elements
    driver.execute_script("document.getElementById('fixedban').style.display = 'none';")

    # Click on 'Elements' card
    elements_card = wait.until(EC.element_to_be_clickable((By.XPATH, "(//div[@class='card mt-4 top-card'])[1]")))
    driver.execute_script("arguments[0].scrollIntoView(true);", elements_card)
    time.sleep(1)
    elements_card.click()

    # Click on 'Text Box' in the sidebar
    text_box = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Text Box']")))
    text_box.click()

    # Fill in the form
    wait.until(EC.visibility_of_element_located((By.ID, "userName"))).send_keys("sapna singh")
    driver.find_element(By.ID, "userEmail").send_keys("abc23@gmail.com")
    driver.find_element(By.ID, "currentAddress").send_keys("rakesh marg")
    driver.find_element(By.ID, "permanentAddress").send_keys("new panchwati")

    # Submit the form
    submit = wait.until(EC.element_to_be_clickable((By.ID, "submit")))
    driver.execute_script("arguments[0].scrollIntoView(true);", submit)
    time.sleep(1)
    submit.click()

    # ✅ Go to Radio Button section
    radio_menu = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Radio Button']")))
    radio_menu.click()

    # Click the "Yes" radio button
    yes_radio = wait.until(EC.element_to_be_clickable((By.XPATH, "//label[@for='yesRadio']")))
    driver.execute_script("arguments[0].scrollIntoView(true);", yes_radio)
    time.sleep(1)
    yes_radio.click()

    # Verify result
    output = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "text-success")))
    assert output.text == "Yes", "Radio button selection failed"

    print("✅ Test Passed - You have selected 'Yes'")
    time.sleep(2)

    # ✅ Go to Web Tables section (corrected line)
    web_table = wait.until(EC.element_to_be_clickable((By.XPATH, "(//li[@id='item-3'])[1]")))
    web_table.click()

    time.sleep(4)

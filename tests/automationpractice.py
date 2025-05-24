import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from conftest import setup_browser



def test_something(setup_browser):
    driver = setup_browser
    driver.implicitly_wait(1)  # implicit wait added here

    driver.get("https://rahulshettyacademy.com/AutomationPractice/")

    checkbox1 = driver.find_element(By.XPATH, "//input[@id='checkBoxOption1']")
    checkbox1.click()

    checkbox2 = driver.find_element(By.XPATH, "//input[@id='checkBoxOption2']")
    checkbox2.click()
    driver.implicitly_wait(2)

    radio1 = driver.find_element(By.XPATH, "//input[@value='radio1']")
    radio1.click()
    driver.implicitly_wait(3)
    radio2 = driver.find_element(By.XPATH,"//input[@value='radio2']")
    radio2.click()
    time.sleep(3)
    driver.implicitly_wait(3)

    wait = WebDriverWait(driver, 10)
    input_box = wait.until(EC.visibility_of_element_located((By.ID, "autocomplete")))

    # Scroll to the input box
    driver.execute_script("arguments[0].scrollIntoView(true);", input_box)

    # Clear and enter text
    input_box.clear()
    input_box.send_keys("Ind")

    time.sleep(3)  # wait to see the suggestions

    suggestions = driver.find_elements(By.CSS_SELECTOR, "li.ui-menu-item div")

    # Step 3: Loop through suggestions and click "India"
    for suggestion in suggestions:
        if suggestion.text == "India":
            suggestion.click()
            break

    time.sleep(3)  #

    """openwindow =  driver.find_element(By.XPATH,"//button[@id='openwindow']")
    openwindow.click()
    time.sleep(3)"""

    # Step 1: Click the button
    openwindow = driver.find_element(By.XPATH, "//button[@id='openwindow']")
    openwindow.click()

    # Step 2: Get all window handles
    main_window = driver.current_window_handle
    all_windows = driver.window_handles

    # Step 3: Check that a new window opened
    assert len(all_windows) > 1, "Popup window did not open."

    # Step 4: Switch to the popup window
    for handle in all_windows:
        if handle != main_window:
            driver.switch_to.window(handle)
            break

    time.sleep(2)  # optional: allow page to load

    # Step 5: Assert the new window title is correct
    # Step 5: Assert the new window title is correct
    assert "QAClick Academy" in driver.title, "Popup window title is incorrect."

    print("Popup window title:", driver.title)

    # Step 6: Close popup and switch back
    driver.close()
    driver.switch_to.window(main_window)


    switchalert = driver.find_element(By.XPATH,"//input[@id='name']")
    switchalert.send_keys("sapna")
    time.sleep(4)
    driver.find_element(By.XPATH,"//input[@id='confirmbtn']").click()
    time.sleep(2)

    # Switch to alert and accept it
    alert = driver.switch_to.alert
    print("Alert text:", alert.text)  # Optional: print alert text
    alert.accept()

    driver.find_element(By.XPATH,"//a[@id='opentab']").click()
    time.sleep(3)
    # Get all window handles
    all_windows = driver.window_handles

    # Switch to the new window using a different loop variable
    for win_handle in all_windows:
        if win_handle != main_window:
            driver.switch_to.window(win_handle)
            break

    # Optional: Do something in the new window
    print("New window title:", driver.title)

    # Close the new window if needed
    driver.close()

    # Switch back to the main window
    driver.switch_to.window(main_window)
    print("Back to main window:", driver.title)
    time.sleep(3)




    hover_element = driver.find_element(By.XPATH, "//button[@id='mousehover']")
    actions = ActionChains(driver)#Perform Mouse Hover

    actions.move_to_element(hover_element).perform()
    top_option = driver.find_element(By.LINK_TEXT, "Top")
    top_option.click()
    time.sleep(6)

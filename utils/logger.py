# store resusable helper functions like webdriver setup and custom logs
from selenium import webdriver

def get_driver(browser="chrome"):
    if browser == "chrome":
        options = webdriver.ChromeOptions()
        options.add_argument("--start-maximized")
        return webdriver.Chrome(options=options)
    else:
        raise ValueError("Browser not supported")
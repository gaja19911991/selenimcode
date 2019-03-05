from selenium import webdriver
import os
from selenium.webdriver.common.by import By
import time


class RadioButtonsAndCheckboxes():
    def test(self):
        driverLocation = r'C:\Users\Admin\eclipse-workspace\chromedriver.exe'
        os.environ["webdriver.chrome.driver"] = driverLocation
        driver = webdriver.Chrome(driverLocation)
        driver.get("https://learn.letskodeit.com/p/practice")
        driver.maximize_window()
        driver.implicitly_wait(10)

        bmwRadioButton = driver.find_element_by_id("bmwradio")
        bmwRadioButton.click()

        time.sleep(3)
        benzRadioButton = driver.find_element_by_id("benzradio")
        benzRadioButton.click()

        time.sleep(3)
        bmwCheckbox = driver.find_element_by_id("bmwcheck")
        bmwCheckbox.click()

        time.sleep(3)
        benzCheckbox = driver.find_element_by_id("benzcheck")
        benzCheckbox.click()
        time.sleep(3)

        print("BMW radio button is selected? " + str(bmwRadioButton.is_selected()))
        print("Benz radio button is selected? " + str(benzRadioButton.is_selected()))

        print("BMW checkbox is selected? " + str(bmwCheckbox.is_selected()))
        print("Benz checkbox is selected? " + str(benzCheckbox.is_selected()))


ff = RadioButtonsAndCheckboxes()
ff.test()
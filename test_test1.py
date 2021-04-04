# Generated by Selenium IDE
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class TestTest1():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def wait_for_window(self, timeout = 2):
    time.sleep(round(timeout / 1000))
    wh_now = self.driver.window_handles
    wh_then = self.vars["window_handles"]
    if len(wh_now) > len(wh_then):
      return set(wh_now).difference(set(wh_then)).pop()
  
  def test_test1(self):
    self.driver.get("https://www.flipkart.com/")
    self.driver.set_window_size(1200, 741)
    self.driver.find_element(By.CSS_SELECTOR, ".\\_3umUoc:nth-child(1)").send_keys("agarwal.divyansh123@gmail.com")
    self.driver.find_element(By.CSS_SELECTOR, ".\\_3mctLh").send_keys("9958256111")
    self.driver.find_element(By.CSS_SELECTOR, ".\\_3AWRsL").click()
    self.driver.find_element(By.CSS_SELECTOR, ".\\_2doB4z").click()
    self.driver.find_element(By.NAME, "q").click()
    self.driver.find_element(By.NAME, "q").send_keys("design of eve")
    self.driver.find_element(By.CSS_SELECTOR, ".Y5N33s:nth-child(1) .lrtEPN").click()
    element = self.driver.find_element(By.CSS_SELECTOR, ".Y5N33s:nth-child(1) .lrtEPN")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    element = self.driver.find_element(By.CSS_SELECTOR, ".\\_1AtVbE:nth-child(2) > .\\_13oc-S > div:nth-child(1) .\\_396cs4")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    self.vars["window_handles"] = self.driver.window_handles
    self.driver.find_element(By.CSS_SELECTOR, ".\\_1AtVbE:nth-child(2) > .\\_13oc-S > div:nth-child(1) .\\_396cs4").click()
    self.vars["win5"] = self.wait_for_window(2000)
    self.vars["root"] = self.driver.current_window_handle
    self.driver.switch_to.window(self.vars["win5"])
    self.driver.close()
    self.driver.switch_to.window(self.vars["root"])
    self.driver.close()
    self.vars["root"] = self.driver.current_window_handle
    self.driver.switch_to.window(self.vars["win5"])
    self.driver.switch_to.window(self.vars["root"])
    element = self.driver.find_element(By.CSS_SELECTOR, "body")
    actions = ActionChains(self.driver)
    actions.move_to_element(element, 0, 0).perform()
  
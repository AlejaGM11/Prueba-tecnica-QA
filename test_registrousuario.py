import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestRegistrousuario:
    def setup_method(self, method):
        self.driver = webdriver.Remote(command_executor='http://localhost:4444/wd/hub', desired_capabilities=DesiredCapabilities.CHROME)
        self.driver.implicitly_wait(10)
        self.vars = {}

    def teardown_method(self, method):
        self.driver.quit()

    def test_registrousuario(self):
        self.driver.get("https://test-qa.inlaze.com/auth/sign-in")
        self.driver.set_window_size(1354, 714)
        self.driver.find_element(By.LINK_TEXT, "Sign up").click()
        
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, "full-name"))).send_keys("MARIA GOMEZ")
        self.driver.find_element(By.ID, "email").send_keys("MGOMEZ@GMAIL.COM")
        self.driver.find_element(By.CSS_SELECTOR, ".w-full > #password").send_keys("Pass123#")
        self.driver.find_element(By.CSS_SELECTOR, ".w-full > #confirm-password").send_keys("Pass123#")
        self.driver.find_element(By.CSS_SELECTOR, ".btn:nth-child(5)").click()

        WebDriverWait(self.driver, 10).until(EC.url_contains("dashboard"))
        assert "dashboard" in self.driver.current_url

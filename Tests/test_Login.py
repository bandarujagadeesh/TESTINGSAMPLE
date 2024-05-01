from datetime import datetime
import time
import pytest
from selenium.webdriver.common.by import By


#adding to git this samples
@pytest.mark.usefixtures("setup_and_teardown")
class TestLogin:
    def test_login_with_invalidemail_validpassword(self):
        self.driver.implicitly_wait(3)
        self.driver.find_element(By.XPATH,"//span[text()='My Account']").click()
        time.sleep(2)
        self.driver.find_element(By.LINK_TEXT,'Login').click()
        time.sleep(2)
        username = self.driver.find_element(By.ID,'input-email')
        username.send_keys(self.generate_email_with_timestamp())
        time.sleep(2)
        password = self.driver.find_element(By.ID,'input-password')
        password.send_keys("srisai@143")
        time.sleep(2)
        self.driver.find_element(By.XPATH,"//input[@value='Login']").click()
        expected_message = "Warning: No match for E-Mail Address and/or Password."
        assert self.driver.find_element(By.XPATH,"//div[@id='account-login']/div[1]").text.__contains__(expected_message)

    def test_login_with_valid_credentials(self):
        self.driver.implicitly_wait(3)
        self.driver.find_element(By.XPATH,"//span[text()='My Account']").click()
        time.sleep(2)
        self.driver.find_element(By.LINK_TEXT,'Login').click()
        time.sleep(2)
        username = self.driver.find_element(By.ID,'input-email')
        username.send_keys("bandarujagadeesh.mca@gmail.com")
        time.sleep(2)
        password = self.driver.find_element(By.ID,'input-password')
        password.send_keys("srisai@143")
        time.sleep(2)
        self.driver.find_element(By.XPATH,"//input[@value='Login']").click()
        assert self.driver.find_element(By.LINK_TEXT,"Edit your account information").is_displayed()

    def test_login_with_validemail_invalidpassword(self):
        self.driver.implicitly_wait(5)
        self.driver.find_element(By.XPATH,"//span[text()='My Account']").click()
        time.sleep(2)
        self.driver.find_element(By.LINK_TEXT,'Login').click()
        time.sleep(2)
        username = self.driver.find_element(By.ID,'input-email')
        username.send_keys("bandarujagadeesh.mca@gmail.com")
        time.sleep(2)
        password = self.driver.find_element(By.ID,'input-password')
        password.send_keys("12345")
        time.sleep(2)
        self.driver.find_element(By.XPATH,"//input[@value='Login']").click()
        expected_message = "Warning: No match for E-Mail Address and/or Password."
        assert self.driver.find_element(By.XPATH,"//div[@id='account-login']/div[1]").text.__contains__(expected_message)

    def generate_email_with_timestamp(self):
        datetimestamp = datetime.now().strftime("%Y-%m-%d%H:%M:%S")
        return "bandarujagadeesh.mca"+datetimestamp+"@gmail.com"
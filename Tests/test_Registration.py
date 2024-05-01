from datetime import datetime
import pytest
from selenium.webdriver.common.by import By
import time

@pytest.mark.usefixtures("setup_and_teardown")
class TestRegistration:
    def test_register_with_mandatory_fields(self):
        self.driver.implicitly_wait(5)
        self.driver.find_element(By.XPATH,"//span[text()='My Account']").click()
        self.driver.find_element(By.LINK_TEXT,"Register").click()
        time.sleep(2)
        self.driver.find_element(By.ID,"input-firstname").send_keys("Jaggu")
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//input[@placeholder='Last Name']").send_keys('kum')
        time.sleep(2)
        emailid = self.driver.find_element(By.ID,"input-email")
        emailid.send_keys(self.generate_email_with_datetimestamp())
        time.sleep(2)
        telephone = self.driver.find_element(By.ID,"input-telephone")
        telephone.send_keys("1234567890")
        time.sleep(2)
        password = self.driver.find_element(By.ID,"input-password")
        password.send_keys("passwordtest")
        time.sleep(2)
        confirmpassword = self.driver.find_element(By.ID,"input-confirm")
        confirmpassword.send_keys("passwordtest")
        time.sleep(2)
        self.driver.find_element(By.NAME,"agree").click()
        time.sleep(2)
        self.driver.find_element(By.XPATH,"//input[@value='Continue']").click()
        time.sleep(2)
        expected_text_message = "Your Account Has Been Created!"
        assert self.driver.find_element(By.XPATH,"//div[@id='content']/h1").text.__eq__(expected_text_message)

    def test_register_with_all_fields(self):
        self.driver.implicitly_wait(5)
        self.driver.find_element(By.XPATH,"//span[text()='My Account']").click()
        self.driver.find_element(By.LINK_TEXT,"Register").click()
        time.sleep(2)
        self.driver.find_element(By.ID,"input-firstname").send_keys("Jaggu")
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//input[@placeholder='Last Name']").send_keys('kum')
        time.sleep(2)
        emailid = self.driver.find_element(By.ID,"input-email")
        emailid.send_keys(self.generate_email_with_datetimestamp())
        time.sleep(2)
        telephone = self.driver.find_element(By.ID,"input-telephone")
        telephone.send_keys("1234567890")
        time.sleep(2)
        password = self.driver.find_element(By.ID,"input-password")
        password.send_keys("passwordtest")
        time.sleep(2)
        confirmpassword = self.driver.find_element(By.ID,"input-confirm")
        confirmpassword.send_keys("passwordtest")
        time.sleep(2)
        self.driver.find_element(By.XPATH,'//input[@name="newsletter"][@value="1"]').click()
        self.driver.find_element(By.NAME,"agree").click()
        time.sleep(2)
        self.driver.find_element(By.XPATH,"//input[@value='Continue']").click()
        time.sleep(2)
        expected_text_message = "Your Account Has Been Created!"
        assert self.driver.find_element(By.XPATH,"//div[@id='content']/h1").text.__eq__(expected_text_message)

    def test_register_with_already_existing_email_duplicate(self):
        self.driver.implicitly_wait(5)
        self.driver.find_element(By.XPATH, "//span[text()='My Account']").click()
        self.driver.find_element(By.LINK_TEXT, "Register").click()
        time.sleep(2)
        self.driver.find_element(By.ID,"input-firstname").send_keys("Jaggu")
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//input[@placeholder='Last Name']").send_keys('kum')
        time.sleep(2)
        emailid = self.driver.find_element(By.ID, "input-email")
        emailid.send_keys("bandarujagadeesh.mca@gmail.com")
        time.sleep(2)
        telephone = self.driver.find_element(By.ID, "input-telephone")
        telephone.send_keys("1234567890")
        time.sleep(2)
        password = self.driver.find_element(By.ID, "input-password")
        password.send_keys("passwordtest")
        time.sleep(2)
        confirmpassword = self.driver.find_element(By.ID, "input-confirm")
        confirmpassword.send_keys("passwordtest")
        time.sleep(2)
        self.driver.find_element(By.XPATH, '//input[@name="newsletter"][@value="1"]').click()
        time.sleep(2)
        self.driver.find_element(By.NAME, "agree").click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//input[@value='Continue']").click()
        time.sleep(2)
        expected_warning_message = "Warning: E-Mail Address is already registered!"
        assert self.driver.find_element(By.XPATH, '//div[@id="account-register"]/div[1]').text.__contains__(expected_warning_message)

    def test_without_entering_anyfields(self):
        self.driver.implicitly_wait(5)
        self.driver.find_element(By.XPATH, "//span[text()='My Account']").click()
        self.driver.find_element(By.LINK_TEXT, "Register").click()
        time.sleep(2)
        self.driver.find_element(By.ID,"input-firstname").send_keys("")
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//input[@placeholder='Last Name']").send_keys('')
        time.sleep(2)
        emailid = self.driver.find_element(By.ID, "input-email")
        emailid.send_keys("")
        time.sleep(2)
        telephone = self.driver.find_element(By.ID, "input-telephone")
        telephone.send_keys("")
        time.sleep(2)
        password = self.driver.find_element(By.ID, "input-password")
        password.send_keys("")
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//input[@value='Continue']").click()
        time.sleep(2)
        expected_warning_nodetails_message = "Warning: You must agree to the Privacy Policy!"
        assert self.driver.find_element(By.XPATH, '//div[@id="account-register"]/div[1]').text.__contains__(expected_warning_nodetails_message)
        expected_firstname_message = "First Name must be between 1 and 32 characters!"
        assert self.driver.find_element(By.XPATH,'//input[@id="input-firstname"]/following-sibling::div').text.__contains__(expected_firstname_message)
        expected_lastname_message = "Last Name must be between 1 and 32 characters!"
        assert self.driver.find_element(By.XPATH,'//input[@id="input-lastname"]/following-sibling::div').text.__contains__(expected_lastname_message)
        expected_email_message = "E-Mail Address does not appear to be valid!"
        assert self.driver.find_element(By.XPATH,'//input[@id="input-email"]/following-sibling::div').text.__contains__(expected_email_message)
        expected_telephone_message = "Telephone must be between 3 and 32 characters!"
        assert self.driver.find_element(By.XPATH,'//input[@id="input-telephone"]/following-sibling::div').text.__contains__(expected_telephone_message)
        expected_password_message = "Password must be between 4 and 20 characters!"
        assert self.driver.find_element(By.XPATH,'//input[@id="input-password"]/following-sibling::div').text.__contains__(expected_password_message)

    def generate_email_with_datetimestamp(self):
        datetimestamp = datetime.now().strftime("%Y-%m-%d%H-%M-%S")
        return "testmail"+datetimestamp+"@gmail.com"




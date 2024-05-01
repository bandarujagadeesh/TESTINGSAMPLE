import time

import pytest
from selenium.webdriver.common.by import By

@pytest.mark.usefixtures("setup_and_teardown")
class TestSearch:
    def test_search_for_an_invalid_product(self):
        time.sleep(2)
        searchoption = self.driver.find_element(By.NAME,'search')
        searchoption.send_keys("Honda")
        time.sleep(2)
        self.driver.find_element(By.XPATH,"//button[@class='btn btn-default btn-lg']").click()
        time.sleep(2)
        expected_text = "There is no product that matches the search criteria."
        assert self.driver.find_element(By.XPATH,"//input[@id='button-search']/following-sibling::p").text.__eq__(expected_text)

    def test_search_for_a_valid_product(self):
        time.sleep(2)
        searchoption = self.driver.find_element(By.NAME,'search')
        searchoption.send_keys("HP")
        time.sleep(2)
        self.driver.find_element(By.XPATH,"//button[@class='btn btn-default btn-lg']").click()
        time.sleep(2)
        assert self.driver.find_element(By.LINK_TEXT,"HP LP3065").is_displayed()

    def test_search_without_entering_any_product(self):
        time.sleep(2)
        searchoption = self.driver.find_element(By.NAME,'search')
        searchoption.send_keys("")
        time.sleep(2)
        self.driver.find_element(By.XPATH,"//button[@class='btn btn-default btn-lg']").click()
        time.sleep(2)
        expected_text = "There is no product that matches the search criteria."
        assert self.driver.find_element(By.XPATH,"//input[@id='button-search']/following-sibling::p").text.__eq__(expected_text)
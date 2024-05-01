import pytest
from selenium import webdriver
from selenium.webdriver import chrome
from selenium.webdriver.chrome.service import Service
from Utilities import ReadConfigurations
# from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture()
def setup_and_teardown(request):
    browser = ReadConfigurations.read_configurations("basic info", "browser")
    driver = None
    if browser.__eq__("chrome"):
        options = webdriver.ChromeOptions()
        options.add_experimental_option("detach", True)
        driver = webdriver.Chrome(options=options, service=Service())
    elif browser.__eq__("firefox"):
        driver = webdriver.Firefox()
    elif browser.__eq__("edge"):
        driver = webdriver.Edge()
    else:
        print("Provide a valid browser")
    app_url = ReadConfigurations.read_configurations("basic info", "url")
    driver.get(app_url)
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.quit()

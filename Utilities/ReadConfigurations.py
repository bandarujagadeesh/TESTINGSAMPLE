from configparser import ConfigParser

def read_configurations(category, key):
    config = ConfigParser()
    config.read("C:/Users/Jagadeesh Bandaru/PycharmProjects/SeleniumPythonHybridframework/Configuratons/config.ini")
    return config.get(category, key)


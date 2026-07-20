import configparser


class ConfigReader:

    config = configparser.ConfigParser()
    config.read("config/config.ini")

    @staticmethod
    def get_browser():
        return ConfigReader.config.get("DEFAULT", "browser")

    @staticmethod
    def get_headless():
        return ConfigReader.config.getboolean("DEFAULT", "headless")

    @staticmethod
    def get_slow_mo():
        return ConfigReader.config.getint("DEFAULT", "slow_mo")

    @staticmethod
    def get_url(environment):
        return ConfigReader.config.get(environment, "url")
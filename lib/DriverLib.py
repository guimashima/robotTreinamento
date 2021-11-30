from robot.api.deco import library
from selenium import webdriver
from msedge.selenium_tools import EdgeOptions
from SeleniumLibrary.base import keyword
import os

@library
class DriverLib():
    ROBOT_LIBRARY_SCOPE = 'GLOBAL'

    @keyword
    def create_chrome_options(self):
        """Return an instance of chromeOptions with users preferences to be set on Chrome browser

            To implement user preferences with RobotFramework, please see the ./resources/drivers.robot file

            To add more preferences, prease look for the correct option and the correct way to set
            that option on the internet or chromeOptions documentation
            @Param
            self: instance of DriverLib class;
            """
        options = webdriver.ChromeOptions()
        prefs = {"download.default_directory":os.getcwd() + "\\resources\\download"}
        options.add_experimental_option("prefs", prefs)
        return options
    
    @keyword
    def create_edge_options(self):
        """Return an instance of edgeOptions with users preferences to be set on Edge browser

            To implement user preferences with RobotFramework, please see the ./resources/drivers.robot file

            To add more preferences, prease look for the correct option and the correct way to set
            that option on the internet or edgeOptions documentation
            @Param
            self: instance of DriverLib class;
            """
        options = EdgeOptions()
        options.use_chromium = True
        prefs = {"download.default_directory":os.getcwd() + "\\resources\\download"}
        #options.add_argument("-inprivate")
        options.add_experimental_option("prefs", prefs)
        return options.to_capabilities()

    @keyword
    def create_firefox_profile(self):
        """Return a path of firefocProfile with users preferences to be set on Firefox browser

            To implement user preferences with RobotFramework, please see the ./resources/drivers.robot file

            To add more preferences, prease look for the correct option and the correct way to set
            that option on the internet or firefoxOptions documentation
            @Param
            self: instance of DriverLib class;
            """
        ff = webdriver.FirefoxProfile()
        ff.set_preference("browser.download.folderList",2)
        ff.set_preference("browser.download.manager.showWhenStarting",False)
        ff.set_preference("browser.download.dir", os.getcwd() + "\\resources\\download")
        ff.set_preference("browser.helperApps.neverAsk.saveToDisk", "text/csv,application/java-archive, application/x-msexcel,application/excel,application/vnd.openxmlformats-officedocument.wordprocessingml.document,application/x-excel,application/vnd.ms-excel,image/png,image/jpeg,text/html,text/plain,application/msword,application/xml,application/vnd.microsoft.portable-executable")
        ff.update_preferences()
        return ff.path
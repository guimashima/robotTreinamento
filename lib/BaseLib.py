from robot.libraries.BuiltIn import BuiltIn
from SeleniumLibrary.base import keyword
from SeleniumLibrary import SeleniumLibrary
from random import randint
from robot.api.deco import library
from typing import Any, TypeVar, Union
from selenium.webdriver.remote.webelement import WebElement
import time
import base64
import urllib.parse
import re

@library
class BaseLib():
    ROBOT_LIBRARY_SCOPE = 'GLOBAL'
    seleniumLib = BuiltIn().get_library_instance('SeleniumLibrary')
    T = TypeVar('T')

    @keyword
    def encode_into_base64(self, text: str) -> str:
        """Return an encoded string into base64
            @Param
            self: instance of BaseLib class;
            text: str;"""
        textByte = str(text).encode("ascii")
        return base64.b64encode(textByte)
    
    @keyword
    def encode_into_url(self, text: str) -> str:
        """Return an encoded string into url.
            @Safe characters:
            -> "'" (single Quote);
            -> "(" and ")" (parentehsis);

            @Param
            self: instance of BaseLib class;
            text: str;"""
        print(text)
        urlEncoded = urllib.parse.quote_plus(str(text), "'" "(" ")" )
        return urlEncoded
            
    @keyword
    def select_from_selection_random(self, select: str) -> None:
        """By passing a unique selector, it'll select a random option from a Selection element.
            
            @Param
            self: instance of BaseLib class;
            select: str;"""
        i = 0
        selectValueList = self.seleniumLib.get_list_items(select)
        while len(selectValueList) <= 1:
            time.sleep(0.5)
            selectValueList = self.seleniumLib.get_list_items(select)
            if i == 5:
                self.seleniumLib.failure_occurred()
                break
            i = i + 1
        index = randint(1, len(selectValueList) - 1)
        self.seleniumLib.select_from_list_by_index(select, str(index))

    @keyword
    def return_child_element_from_parent(self, parent: WebElement, query: str) -> WebElement:
        """This function returns a Child element from a Parent element 
            using Query parameter as a cssSelector.
            
            @Param
            self: instance of BaseLib class;
            parent: Parent WebElement;
            query: string containing a cssSelector;"""
        if(str(query).__contains__("css:")):
            query = str(query).replace("css:", "")
        return parent.find_element_by_css_selector(query)

    @keyword
    def wait_until_element_loses_attribute(self, locator: Any, attribute: str) -> None:
        """This function will wait until element located by Locator loses Attribute. Max of 3 sec.
            
            @Param
            self: instance of BaseLib class;
            locator: any WebElement locator in robotframework (e.g. css:*** or id:***) or a webelement;
            attribute: string containing a attribute name;"""
        i = 0
        while str(self.seleniumLib.get_element_attribute(locator, attribute)).__eq__("true"):
            time.sleep(0.5)
            if i == 5:
                self.seleniumLib.click_button()
                break
            i = i + 1
    
    @keyword
    def return_random_element_with_selector_from_list(self, selector: str) -> WebElement:
        """This function will wait until list of element located by selector be more than 1. Max of 3 sec.
            After that, will return an element based on randint() with list length
            
            @Param
            self: instance of BaseLib class;
            selector: any WebElement locator in robotframework (e.g. css:*** or id:***);"""
        i = 0
        elementList = self.seleniumLib.get_webelements(selector)
        while len(elementList) <= 1:
            time.sleep(0.5)
            elementList = self.seleniumLib.get_webelements(selector)
            if i == 5:
                self.seleniumLib.failure_occurred()
                break
            i = i + 1
        index = randint(0, len(elementList) - 1)
        return elementList[index]
    
    @keyword
    def return_element_with_selector_from_list_by_index(self, selector: str, index: str) -> WebElement:
        """This function will wait until list of element located by selector be more than 1. Max of 3 sec.
            After that, will return an element based on sended index. 
            
            @Param
            self: instance of BaseLib class;
            selector: any WebElement locator in robotframework (e.g. css:*** or id:***);
            index: string of a number;"""
        i = 0
        elementList = self.seleniumLib.get_webelements(selector)
        while len(elementList) <= 1:
            time.sleep(0.5)
            elementList = self.seleniumLib.get_webelements(selector)
            if i == 5:
                self.seleniumLib.failure_occurred()
                break
            i = i + 1
        return elementList[int(index)]
    
    @keyword
    def element_list_should_be_equals_or_higher_than_length(self, selector: str, length: str) -> None:
        """This function will create a list based on the sended Selector. After that, 
            validated if length of elementList is equals or higher than sended length
            
            @Param
            self: instance of BaseLib class;
            selector: any WebElement locator in robotframework (e.g. css:*** or id:***);
            length: string of a number;"""
        elementList = self.seleniumLib.get_webelements(selector)
        if(len(elementList) >= int(length)):
            print("validation passed: list length equals or higher then sended length")
        else:
            self.seleniumLib.failure_occurred()

    @keyword
    def return_parent_element_from_child(self, selector: str) -> WebElement:
        """This function will wait the element located by selector to be visible and return a parent WebElement from sended Selector
            
            @Param
            self: instance of BaseLib class;
            selector: any WebElement locator in robotframework (e.g. css:*** or id:***);"""
        self.seleniumLib.wait_until_page_contains_element(selector)
        return self.seleniumLib.get_webelement(selector).find_element_by_xpath('parent::*')
        
    @keyword
    def one_from_list_should_contain(self, listValues: list[str], param: str) -> None:
        """This function validate that sended List Values contains sended Parameter.
            
            @Param
            self: instance of BaseLib class;
            listValues: a list of strings;
            param: a value (string) to be validated in listValues;"""
        if not(listValues.__contains__(param)):
            print(param, " not inside of ", listValues)
            self.seleniumLib.click_button()
    
    @keyword
    def all_from_list_should_contain(self, listValues: list[str], param: str) -> None:
        """This function validate that sended List Values contains sended Parameter.
            
            @Param
            self: instance of BaseLib class;
            listValues: a list of strings;
            param: a value (string) to be validated in listValues;"""
        for value in listValues:
            if not(value.__contains__(param)):
                print(param, " not inside of ", value, " from ", listValues)
                self.seleniumLib.click_button()
    
    @keyword
    def return_all_values_from_select(self, locator: Any) -> list[str]:
        """This function will return all values from a selection element located by Locator
            
            @Param
            self: instance of BaseLib class;
            locator: any WebElement locator in robotframework (e.g. css:*** or id:***) or an webelement;"""
        element = self.seleniumLib.get_webelement(locator)
        listValues = []
        listOptions = element.find_elements_by_css_selector("option")
        for value in listOptions:
            listValues.append(str(self.seleniumLib.get_element_attribute(value, "value")))
        return listValues
    
    @keyword
    def return_random_element_with_list_from_list(self, sendedList: list[T]) -> T:
        """This function will return a random value from sended list
            
            @Param
            self: instance of BaseLib class;
            sendedList: list of values;"""
        index = randint(0, (len(sendedList) - 1))
        return sendedList[index]
    
    @keyword
    def return_child_element_list_from_parent(self, parent: WebElement, childSelector: str) -> list[WebElement]:
        """This function will return an element list from a Parent element.
            
            @Param
            self: instance of BaseLib class;
            parent: WebElement;
            childSelector: str of cssSelector;"""
        i = 0
        query = str(childSelector).replace("css:", "")
        print(query)
        while len(parent.find_elements_by_css_selector(query)) < 1:
            time.sleep(0.5)
            i = i + 1
            if i == 5:
                self.seleniumLib.failure_occurred()
                break
        resultsList = parent.find_elements_by_css_selector(query)
        return resultsList
        
    @keyword
    def Wait_until_element_contains_attribute(self, locator: Any, attribute: str) -> None:
        """This function will wait until element located by Locator gains Attribute. Max of 3 sec.
            
            @Param
            self: instance of BaseLib class;
            locator: any WebElement locator in robotframework (e.g. css:*** or id:***) or a webelement;
            attribute: string containing a attribute name;"""
        i = 0
        while i <= 5:
            att = self.seleniumLib.get_element_attribute(locator, attribute)
            if str(att).__contains__("true"):
                return
            i = i + 1
            time.sleep(0.5)
        self.seleniumLib.click_button()
    
    @keyword
    def generate_random_num_by_list_length(self, lista: list[T]) -> str:
        """This function will return a random number in string by sended list length
            
            @Param
            self: instance of BaseLib class;
            lista: any list;"""
        num = 0
        num = randint(0, len(lista) - 1)
        return str(num)
    
    @keyword
    def remove_field_from_body(self, body: str, field: str) -> str:
        """This function will remove Field from sended Body string.

            
            It's set to remove:

            @-> "key": {"how": "many", "parameters": "you", "want": "values too"}, (if exists comma in the end)
            @-> "key": ["how": "many", "parameters": "you", "want": "values too"], (if exists comma in the end)
            @-> "key": "value", (if exists comma in the end)
            
            @Param
            self: instance of BaseLib class;
            body: a string of an object;
            field: name of the key to remove"""
        regexObj = r"\"\b(" + field + r")\":\s*{\"[\w\sáàâãéèêíïóôõöúçñÁÀÂÃÉÈÊÍÏÓÒÖÚÇÑ!,.?¿:\"[\]]*\"*},*"
        regexArray = r"\"\b(" + field + r")\":\s*\[\"*[\w\sáàâãéèêíïóôõöúçñÁÀÂÃÉÈÊÍÏÓÒÖÚÇÑ!,.?{[\]¿}\":]*\"*,*],*"
        regexString = r"\"\b(" + field + r")\":\s*\"*[\w\sáàâãéèêíïóôõöúçñÁÀÂÃÉÈÊÍÏÓÒÖÚÇÑ!,.?¿]*\"*,*"
        unitedRegex = regexObj + "|" + regexArray + "|" + regexString
        removedBody = re.sub(unitedRegex,"", body, 1)
        regexComma = r",\s*}"
        return re.sub(regexComma, "}", removedBody)

    @keyword
    def return_value_list_from_response_list(self, listaBody: list, key: str) -> list[str]:
        """This function will return a list os values from a list of bodies by the given key
            
            @Param
            self: instance of BaseLib class;
            listaBody: a list of response bodies, containing the given key
            key: a name of a paremeter inside each body sended in listaBody;"""
        arrayList = []
        for body in listaBody:
            print(body[key])
            arrayList.append(body[key])
        return arrayList

    @keyword
    def return_value_list_from_response_list_by_count(self, listaBody: list[dict], key: str, count: str) -> list[str]:
        """This function will return a list os values from a list of bodies by the given key
            
            @Param
            self: instance of BaseLib class;
            listaBody: a list of response bodies, containing the given key
            key: a name of a paremeter inside each body sended in listaBody;"""
        arrayList = []
        i = 0
        while i < int(count):
            index = int(self.generate_random_num_by_list_length(listaBody))
            arrayList.append(listaBody[index][key])
            listaBody.pop(index)
            i = i + 1
        return arrayList

    @keyword
    def select_random_int(self, firstValue: int, secondValue:int) -> str:
        """Return a number in format string
            @Param
            self: instance of BaseLib class
            firstValue: number that start the gap
            secondValue: number that end the gap
            """
        number = randint(firstValue, secondValue)
        return number

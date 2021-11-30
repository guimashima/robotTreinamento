from robot.libraries.BuiltIn import BuiltIn
from SeleniumLibrary.base import keyword
from SeleniumLibrary import SeleniumLibrary
from random import randint
from robot.api.deco import library
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from BaseLib import BaseLib
from typing import Union
import time
import re

@library
class PublisherLib():
    ROBOT_LIBRARY_SCOPE = 'GLOBAL'
    seleniumLib = BuiltIn().get_library_instance('SeleniumLibrary')

    @keyword
    def search_component_in_component_list_by_title_name(self, name: str) -> Union[WebElement, None]:
        """On all component page, where shows all created components (Carousels or Pages), this function will look for an
            specific component.
            First this function will wait until appears the component list on screen and after that it'll look on that list
            with the given name.
            If there is a match, will return the first match as a WebElement. 
            If doesn't find any match, will generate button error (to fail the test case)
            @Param
            self: instance of PublisherLib class;
            text: str;"""
        i = 0
        componentList = self.seleniumLib.get_webelements("css:#list-table tbody tr")
        while len(componentList) < 1:
            time.sleep(0.5)
            componentList = self.seleniumLib.get_webelements("css:#list-table tbody tr")
            if i == 5:
                print("Components didn't show on screen after 3 seconds")
                self.seleniumLib.click_button()
                break
            else:
                i = i + 1
        for element in componentList:
            if (len(element.find_elements_by_css_selector("p.text")) > 0):
                if (self.seleniumLib.get_text(element.find_element_by_css_selector("p.text")) == name):
                    return element
        print("Couldn't find any match")
        self.seleniumLib.click_button()
    
    @keyword
    def input_filter_description(self) -> None:
        """On Carousel creation page, when selecting the type of filter to be applied on an automatic filter, it's necessary
            to input a decription. Depending on the type, it can be an input element or a dropdown element.
            This function will input "Filter Description" for input element OR select a random option in dropdown element.
            For filter type "Start Time", where request an date, it'll be inputed "2021-05-03T10:00:00" on input element
            @Param
            self: instance of PublisherLib class;"""
        time.sleep(0.5)
        cond = "input"
        while len(self.seleniumLib.get_webelements("css:input[name='chose-opt']")) == 0:
            if len(self.seleniumLib.get_webelements("css:select[name='chose-opt']")) > 0:
                cond = "select"
                break
            time.sleep(0.5)
            
        if (cond.__eq__("input")):
            print("input")
            parent = BaseLib.return_parent_element_from_child(BaseLib, "css:select[name='filtro']")
            BaseLib.return_parent_element_from_child(BaseLib, "css:select[name='filtro']")
            text = self.seleniumLib.get_text(BaseLib.return_child_element_from_parent(BaseLib, parent,"css:.btn span b"))
            if str(text).__contains__("Start Time"):
                self.seleniumLib.press_keys('css:.make-filter input[name="chose-opt"]', "2021-05-03T10:00:00")
            else:
                self.seleniumLib.input_text('css:.make-filter input[name="chose-opt"]', "Filter description")
        else:
            print("select")
            parent = BaseLib.return_parent_element_from_child(BaseLib, "css:select[name='chose-opt']")
            btn = BaseLib.return_child_element_from_parent(BaseLib, parent, "css:.btn")
            self.seleniumLib.click_element(btn)
            options = BaseLib.return_child_element_list_from_parent(BaseLib, parent, "label.checkbox")
            print("cheguei aq")
            self.select_multiple_option_by_click(options, "1")
    
    @keyword
    def return_highlight_carousel_from_page_creation_page_by_count_and_status(self, count: str, status: str) -> Union[list[WebElement], WebElement]:
        """On Page creation page, when selecting carousels to be attached to a page, just one highlight carousel can be
            attached to it. This function will return the first highlight carousel on carousel list.
            The carousel list it's made of all carousels that shows in Page creation page.
            If carousels list don't show in 3 seconds, will be forced an fail by click_button method from seleniumLib
            @Param
            self: instance of PublisherLib class;"""
        i = 0
        while len(self.seleniumLib.get_webelements("css:#source-carousel tr")) < 1:
            time.sleep(0.5)
            if i == 5:
                print("carousel list didn't show after 3 seconds")
                self.seleniumLib.click_button()
                break
            i = i + 1
        carouselsList = self.seleniumLib.get_webelements("css:#source-carousel tr")
        heroList = []
        i = 1
        for carousel in carouselsList:
            if(self.seleniumLib.get_text(carousel.find_element_by_css_selector("span.type")).__contains__("Hero") and
                carousel.get_attribute("data-state").__contains__(status)):
                heroList.append(carousel)
                if (int(count) == 1): return carousel
                if (int(count) == i): return heroList
                i = 1 + i
        print("Highlight carousel Not found")
        return heroList
    
    @keyword
    def drag_comom_carousel_into_phone_viewer(self, carouselCont: str) -> None:
        """On Page creation page, when selecting carousels to be attached to a page, it's necessary to drag and drop 
            carousels element into the phone viewer. This function will select a random carousel from carousel list 
            in Page creation page and drag and drop that carousel element into phone viewer. 
            This function will repeat as many times as sended carouselCont
            If carousels list don't show in 3 seconds, will be forced an fail by click_button method from seleniumLib
            @Param
            self: instance of PublisherLib class;
            carouselCont: string of an int number"""
        i = 0
        while len(self.seleniumLib.get_webelements("css:#source-carousel tr")) < 0:
            time.sleep(0.5)
            if i == 5:
                print("carousel list didn't show after 3 seconds")
                self.seleniumLib.click_button()
                break
            i = i + 1
        carouselsList = self.seleniumLib.get_webelements("css:#source-carousel tr")
        for carousel in carouselsList:
            if(self.seleniumLib.get_text(carousel.find_element_by_css_selector("span.type")).__contains__("Hero")):
                carouselsList.remove(carousel)
        i = 0
        while i < int(carouselCont):
            index = randint(0, len(carouselsList) - 1)
            self.seleniumLib.drag_and_drop(carouselsList[index], "css:tfoot .area-new-carrossel")
            carouselsList.remove(carouselsList[index])
            i = i + 1
            time.sleep(0.2)
    
    @keyword
    def add_comom_carousel_into_phone_viewer_by_options(self, carouselCont: str) -> None:
        """On Page creation page, when selecting carousels to be attached to a page, it's necessary to drag and drop 
            carousels element into the phone viewer. This function will select a random carousel from carousel list 
            in Page creation page and add to phone viewer by carousel options in the right side of carousel element. 
            This function will repeat as many times as sended carouselCont
            If carousels list don't show in 3 seconds, will be forced an fail by click_button method from seleniumLib
            @Param
            self: instance of PublisherLib class;
            carouselCont: string of an int number"""
        i = 0
        while len(self.seleniumLib.get_webelements("css:#source-carousel tr")) < 0:
            time.sleep(0.5)
            if i == 5:
                print("carousel list didn't show after 3 seconds")
                self.seleniumLib.click_button()
                break
            i = i + 1
        carouselsList = self.seleniumLib.get_webelements("css:#source-carousel tr")
        for carousel in carouselsList:
            if(self.seleniumLib.get_text(carousel.find_element_by_css_selector("span.type")).__contains__("Hero")):
                carouselsList.remove(carousel)
        i = 0
        while i < int(carouselCont):
            index = randint(0, len(carouselsList) - 1)
            self.seleniumLib.click_element(BaseLib.return_child_element_from_parent(BaseLib, carouselsList[index], ".options"))
            self.seleniumLib.scroll_element_into_view(BaseLib.return_child_element_from_parent(BaseLib, carouselsList[index], ".assign-this"))
            self.seleniumLib.click_element(BaseLib.return_child_element_from_parent(BaseLib, carouselsList[index], ".assign-this"))
            carouselsList.remove(carouselsList[index])
            i = i + 1
            time.sleep(0.2)
    
    @keyword
    def select_content_by_number(self, contentCont: str) -> None:
        """On Catalog page it's possible to select content from content list and create a carousel
            with those selected content as a manual content.
            This function will repeat the content selection as many times as sended contentCont and proceed with 
            carousel creation flow.
            If content list don't show in 3 seconds, will be forced an fail by click_button method from seleniumLib
            @Param
            self: instance of PublisherLib class;
            contentCont: string of an int number"""
        i = 1
        lim = 0
        contentList = self.seleniumLib.get_webelements("css:.filme-item .ck-mark")
        while len(self.seleniumLib.get_webelements("css:.filme-item .ck-mark")) <= 1:
            time.sleep(0.5)
            lim = lim + 1
            if lim == 5:
                print("content list didn't show after 3 seconds")
                self.seleniumLib.click_button()
                break
        contentList = self.seleniumLib.get_webelements("css:.filme-item .ck-mark")
        for content in contentList:
            self.seleniumLib.click_element(content)
            if(int(contentCont) == i):
                break
            else:
                i = i + 1
                
    @keyword
    def select_multiple_option_by_click(self, options: list[WebElement], cont: str) -> None:
        """For any dropdown in CMS Publisher. 
            Most of dropdown in Publisher it's a hidden select. So this function will select a random option from
            dropdown by clicking on the option.
            For this function to work correctly, it's necessaruy to pass a list of options element. And, to pass it correctly,
            it's necessary to click on the dropdown and create a list of options elements that shows on screen.
            There are examples of this method implemented in ./keywords/publisher/carousels.robot file. 
            See there for more details
            @Param
            self: instance of PublisherLib class;
            options: list of dropdown options element;
            cont: str of an int number. How many times you want to repeat the selection"""
        i = 1
        while i <= int(cont):
            index = randint(0, len(options) - 1)
            if str(self.seleniumLib.get_element_attribute(options[index], "title")).__contains__("Select"):
                options.remove(options[index])
                continue
            self.seleniumLib.scroll_element_into_view(options[index])
            self.seleniumLib.click_element(options[index])
            i = i + 1
            if int(cont) == 1:
                return self.seleniumLib.get_element_attribute(options[index], "title")
            options.remove(options[index])

    @keyword
    def return_content_in_catalog_by_title(self, title: str) -> Union[WebElement, None]:
        """For Catalog page. This function search the given title in all visible content in catalog page.
            First it'll wait until length of a list of content be more than one and after that will search the title of 
            each content in the content list.
            If there is a match, it'll return that match as a WebElement
            If the isn't any match, will return None
            @Param
            self: instance of PublisherLib class;
            title: str. title of desired content"""
        i = 0
        while len(self.seleniumLib.get_webelements("css:.filme-item")) < 1:
            time.sleep(0.5)
            i = i + 1
            if i == 5:
                print("content list didn't show after 3 seconds")
                self.seleniumLib.click_button()
                break
        contentList =  self.seleniumLib.get_webelements("css:.filme-item")
        for content in contentList:
            contentTitle = self.seleniumLib.get_text(content.find_element_by_css_selector("h4"))
            if title.__eq__(contentTitle):
                return content

    @keyword
    def return_carousel_type_from_settings_page(self, element: WebElement) -> str:
        """For Settings page. This function returns a carousel type as a string, retrieving from given element from 
            Settings Page. 
            Fisrt it'll extract the text from element and split it by ";" and will return the second element from splitted array
            @Param
            self: instance of PublisherLib class;
            element: WebElement, containing carousel type as a text"""
        text = self.seleniumLib.get_text(element)
        textList = str(text).split(str(";"))
        carouselType = textList[1].strip()
        return carouselType

    @keyword
    def logs_page_should_contain_title(self, title: str) -> None:
        """For Logs page. This function will validate if there is a give title on logs list.
        First it'll wait until there is at least one log component and after that will create a list of logs and validate if
        exists the given title inside created log list 
        @Param
        self: instance of PublisherLib class;
        title: str. a title from a content from catalog"""
        i = 0
        cont = 0
        while(len(self.seleniumLib.get_webelements("css:#list-table tbody tr")) < 1):
            time.sleep(0.5)
            i = i + 1
            if i == 5:
                print("Log list didn't show after 3 seconds")
                self.seleniumLib.click_button()
        pageLogs = self.seleniumLib.get_webelements("css:#list-table tbody tr")
        for pageLog in pageLogs:
            logTitle = self.seleniumLib.get_text(pageLog.find_element_by_css_selector("p.text"))
            if (str(logTitle).__contains__(title)):
                break

    @keyword
    def all_from_resbody_list_should_contains(self, contentList: list[dict], key: str, value: str) -> None:
        """ This function will validate if the sended resbody from a request response body contains the given 
            key and value.
            If even one of resbody list doesn't contain the given key value pair, than this function fill return a 
            failed validation
            @Param
            self: instance of PublisherLib class;
            contentList: content array (json) of response body from v1/search GET request/
            key: str. used to retrieve value from one content;
            value: str. used to validate if retrieved value equals sended value;"""
        cond = True
        for content in contentList:
            cond= False
            if (not(str(content[key]).__contains__(value.upper())) and 
                not(str(content[key]).__contains__(value.lower())) and 
                not(str(content[key]).__contains__(value.title())) and
                not(str(content[key]).__contains__(value))):
                print("Error on validation. {} not found in {}".format(value, key))
                # using click button to generate error in robot and log all info os the test in report
                self.seleniumLib.click_button()
                break
            print(content[key])
        if (cond):
            print("No content found in Resbody")
            self.seleniumLib.click_button()
    
    @keyword
    def at_least_one_resbody_in_resbody_list_should_contain(self, carousels: list[dict], key: str, value: str) -> None:
        """ This function will validate if the sended resbody from a request response body contains the given 
            key and value.
            If at least one of resbody list contains the given key value pair, than this function fill return a 
            successfull validation
            @Param
            self: instance of PublisherLib class;
            carouselList: carousel array (json) of response body from cms request/
            key: str. used to retrieve value from one content;
            value: str. used to validate if retrieved value equals sended value;"""
        cond = True
        for carousel in carousels:
            if (str(carousel[key]).__contains__(value.upper()) or 
                str(carousel[key]).__contains__(value.lower()) or 
                str(carousel[key]).__contains__(value.title()) or
                str(carousel[key]).__contains__(value)):
                cond = False
                break
            print(carousel[key])
            print(value)
        if cond:
            print("Error on validation. {} not found in {}".format(value, key))
            # using click button to generate error in robot and log all info os the test in report
            self.seleniumLib.click_button()
            
    @keyword
    def content_list_should_contain_cast_name(self, contentList: list[dict], value: str) -> None:
        """For Catalog_API scenarios. When requesting on v1/search, all results are content from one of the sources.
            This function will validated if the sended contentlist from a v1/search response body contains the given 
            cast name inside cast of each content.
            If even one of contents doesn't contain the given cast name, than this function fill return a 
            failed validation
            @Param
            self: instance of PublisherLib class;
            contentList: content array (json) of response body from v1/search GET request/
            value: cast name as str. used to validate if retrieved value equals sended value;"""
        actorFound = False
        for content in contentList:
            actorFound = False
            actors = content["cast"]
            for actor in actors:
                if (str(actor["person"]["firstName"]).__contains__(value.upper()) or
                    str(actor["person"]["firstName"]).__contains__(value.lower()) or
                    str(actor["person"]["firstName"]).__contains__(value.title()) or
                    str(actor["person"]["lastName"]).__contains__(value.lower()) or
                    str(actor["person"]["lastName"]).__contains__(value.title()) or
                    str(actor["person"]["lastName"]).__contains__(value.upper())):
                    actorFound = True
                    break
            if not(actorFound):
                break
        if not(actorFound):
            print("actor not found in content")
            # using click button to generate error in robot and log all info os the test in report
            self.seleniumLib.click_button()

    @keyword    
    def content_list_should_be_equals_or_future_date(self, contentList: list[dict], date: str) -> None:
        """For Catalog_API scenarios. When requesting on v1/search, all results are content from one of the sources.
            This function will validated if the sended contentlist licenseStartDate from a v1/search response body 
            is equals or future date than sended date.
            If even one of contents isn't equals or future date, then the validation will fail
            failed validation
            @Param
            self: instance of PublisherLib class;
            contentList: content array (json) of response body from v1/search GET request/
            value: Date as str. used to validate if retrieved licenseStartDate is equals or future than sended date;"""
        cond = True
        for content in contentList:
            cond = False
            contentDate = content["licenseStartDate"]
            contentDate = str(contentDate).replace("Z", "")
            date = date.replace(".000", "")
            contentTime = time.strptime(contentDate, '%Y-%m-%dT%H:%M:%S')
            contentTime2 = time.strptime(date, '%Y-%m-%dT%H:%M:%S')
            if not(contentTime >=  contentTime2):
                print("content start date past than sended date")
                # using click button to generate error in robot and log all info os the test in report
                self.seleniumLib.click_button()
        if (cond):
            print("No content found in Resbody")
            self.seleniumLib.click_button()
                
            
    @keyword    
    def content_list_should_be_equals_or_past_date(self, contentList, date):
        """For Catalog_API scenarios. When requesting on v1/search, all results are content from one of the sources.
            This function will validated if the sended contentlist licenseStartDate from a v1/search response body 
            is equals or past date than sended date.
            If even one of contents isn't equals or future date, then the validation will fail
            failed validation
            @Param
            self: instance of PublisherLib class;
            contentList: content array (json) of response body from v1/search GET request/
            value: Date as str. used to validate if retrieved licenseStartDate is equals or past than sended date;"""
        cond = True
        for content in contentList:
            cond = False
            contentDate = content["licenseEndDate"]
            contentDate = str(contentDate).replace("Z", "")
            date = date.replace(".000", "")
            contentTime = time.strptime(contentDate, '%Y-%m-%dT%H:%M:%S')
            contentTime2 = time.strptime(date, '%Y-%m-%dT%H:%M:%S')
            if not(contentTime <=  contentTime2):
                print("content start date past than sended date")
                # using click button to generate error in robot and log all info os the test in report
                self.seleniumLib.click_button()
        if (cond):
            print("No content found in Resbody")
            self.seleniumLib.click_button()

    @keyword
    def remove_field_in_carousel_creation_body_field(self, body: str, field: str) -> str:
        """This function remove a given field and special characters from a CMS request body BEFORE 
            it was encoded in URL and return the body as a string
            @Param
            self: instance of PublisherLib class;
            body: a body as a str to be used to POST in CMS API
            field: a field as a string to be removed from body, together with special character: { } / : , """
        regexString = r"\\\"\b{}\\\":\\\"\w*\\\",".format(field)
        return re.sub(regexString,"", body, 1)
    
    @keyword
    def replace_field_in_carousel_creation_body_field(self, body: str, field: str, value:str) -> str:
        """This function remove a given field and special characters from a CMS request body BEFORE 
            it was encoded in URL and return the body as a string
            @Param
            self: instance of PublisherLib class;
            body: a body as a str to be used to POST in CMS API
            field: a field as a string to be removed from body, together with special character: { } / : , """
        regexString1 = r"\\\"\b{}\\\":\w*".format(field)
        regexString2 = r"\\\"\b{}\\\":\\\"\w*\\\"".format(field)
        body = re.sub(regexString1,"\\\"{}\\\":{}".format(field, value), body, 1)
        return re.sub(regexString2,"\\\"{}\\\":\\\"{}\\\"".format(field, value), body, 1)

    @keyword
    def change_TAID_switch_by_status(self, status: str) -> None:
        """This function changes TAID switch to sended status. 
            If true, then switch should be on.
            If false, then switch should be off 
            @param
            self: instance of PublisherLib. class
            status: a string, either true or false"""
        if(str(self.seleniumLib.get_webelement('css:input[name="ta-id"]').is_displayed()).lower() != status.lower()):
            button = BaseLib.return_parent_element_from_child(BaseLib, 'css:input[name="is-ta"]')
            self.seleniumLib.click_element(button)
    
    @keyword
    def change_VOD_EPG_switch_by_status(self, status: str) -> None:
        """This function changes VOD/EPG switch to sended status. 
            If true, then switch should be EPG.
            If false, then switch should be VOD 
            @param
            self: instance of PublisherLib. class
            status: a string, either true or false"""
        i = 0
        while i < 5:
            if(len(self.seleniumLib.get_webelements('css:#opt-channels')) == 1):
                break
            time.sleep(0.5)
            i = i + 1
            if i == 5:
                return
        parent = BaseLib.return_parent_element_from_child(BaseLib, 'css:#opt-channels')
        if(str(parent.is_displayed()).lower() != status.lower()):
            button = BaseLib.return_parent_element_from_child(BaseLib, 'css:input[name="vod-epg"]')
            self.seleniumLib.click_element(button)
    
    @keyword
    def build_filter_body_from_epg_content_response(self, content:dict) -> str:
        """This method build the filter part of a carousel creation body. Passing the EPG content/asset requested from catalog, it'll build the content
            in the same way that it's done in publisher carousel creation form.
            @param
            self: instance of PublisherLib
            content: a dict of an EPG content/asset, requested in catalog"""
        programs = list(content["programs"])
        index = int(BaseLib.generate_random_num_by_list_length(BaseLib, programs))
        while (programs[index]["id"].__contains__("EPG00000000001")):
            programs.pop(index)
            index = int(BaseLib.generate_random_num_by_list_length(BaseLib, programs))
        channelTitle = str(content["title"]) if str(content["title"]) else ''
        channelLogo = str(content["logo"]) if str(content["logo"]) else ''
        channelId = str(content["id"]) if str(content["id"]) else ''
        programAirtime = str(programs[index]["airTime"]) if str(programs[index]["airTime"]) else ''
        programEndtime = str(programs[index]["endTime"]) if str(programs[index]["endTime"]) else ''
        programDuration = str(programs[index]["duration"]) if str(programs[index]["duration"]) else ''
        programHashkey = str(programs[index]["hashKey"]) if str(programs[index]["hashKey"]) else ''
        programTitle = str(programs[index]["title"]) if str(programs[index]["title"]) else ''
        programImgUrl = str(programs[index]["images"][0]["url"]) if len(programs[index]["images"]) > 0 else ''
        programType = str(programs[index]["programType"]) if str(programs[index]["programType"]) else ''
        filterBody1 = r"\"('channelTitle':'" + channelTitle + r"','logoChannel':'" + channelLogo + r"',"
        filterBody2 = r"'channelId':'" + channelId + r"','airTime':'" + programAirtime + r"','endTime':'"
        filterBody3 = programEndtime + r"','duration':" + programDuration + r",'hashKey':'"
        filterBody4 = programHashkey + r"','programTitle':'" + programTitle + r"','image':'"
        filterBody5 = programImgUrl + r"','programType':'" + programType + r"')\""
        filterBody = filterBody1 + filterBody2 + filterBody3 + filterBody4 + filterBody5
        return filterBody

    @keyword
    def return_channelId_by_channelId_count(self, channelList: list[dict], count: str) -> str:
        """This method returns channelIds to be used in a catalog api search. By a list of channels that was requested
            in search (search?programType=LIVE), it'll form a string containing the channel ids separated by , (comma).
            The quantity of channel ids is determinated by the total of count sended as parameter of this function
            @param
            self: instance of PublisherLib
            channeList: list of channels requested in catalog (in search?programType=LIVE)
            count: quantity of channelIds desired"""
        i = 0
        index = 0
        channels = ''
        while i < int(count):
            index = int(BaseLib.generate_random_num_by_list_length(BaseLib, channelList))
            channels = str(channelList[index]["channelId"]) if channels == '' else str(channels) + "," + str(channelList[index]["channelId"])
            channelList.pop(index)
            i = i + 1
        print(channels)
        return channels
    
    @keyword
    def return_content_id_from_content_list_by_count(self, contentList: list[dict], count: str) -> str:
        """This method returns contentId to be used in a carousel editorial content body. By a list of content that was requested
            in search (i.e. search?programType=MOVIE), it'll form a string containing the content ids separated by | (vertical bar).
            The quantity of conetnt ids is determinated by the total of count sended as parameter of this function
            @param
            self: instance of PublisherLib
            contentList: list of content requested in catalog (i.e. in search?programType=MOVIE)
            count: quantity of contentIds desired"""
        ids = ''
        i = 0
        index = 0
        while i < int(count):
            index = int(BaseLib.generate_random_num_by_list_length(BaseLib, contentList))
            print(contentList[index])
            ids = str(contentList[index]["id"]) if ids == '' else str(ids) + "|" + str(contentList[index]["id"])
            contentList.pop(index)
            i = i + 1
        return ids
    
    @keyword
    def add_banner_into_banner_collection(self, count: str) -> WebElement:
        i = 0
        while(len(self.seleniumLib.get_webelements("css:#list-table tbody tr")) < int(count)):
            time.sleep(0.5)
            i = i + 1
            if (i == 5):
                print("it wasn't possible to locale enough banner from list")
                self.seleniumLib.click_button()
        i = 0
        bannerList = self.seleniumLib.get_webelements("css:#list-table tbody tr")
        while(i < int(count)):
            banner = BaseLib.return_random_element_With_list_from_list(BaseLib, bannerList)
            banner.find_element_by_css_selector(".add-icons").click()
            bannerList.remove(banner)
            i = i + 1
        return banner


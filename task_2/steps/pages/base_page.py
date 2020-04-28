from selenium.common.exceptions import *
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait


class BasePage:
    locators_dictionary = {}

    def __init__(self, browser, timeout=10):
        self.browser = browser
        self.timeout = timeout

    def find_element(self, *locator: str):
        """
        The method looks for an element with the corresponding locator in the DOM-model and returns WebElement
        instance. Returns None if the corresponding element doesn't exist.
        :param locator: key of locators_dictionary or pair of By and locator according to value of
                        locators_dictionary
        :return: WebElement or None
        """
        if len(locator) == 1:
            locator_name = locator[0]
            if locator_name not in self.locators_dictionary:
                raise ValueError(f"There's no locator named '{locator_name}' "
                                 f"in the {self}'s locators_dictionary.")
            locator_tuple = self.locators_dictionary[locator_name]
        elif len(locator) == 2:
            locator_tuple = locator
        else:
            raise ValueError("The method can't receive less than one and more than two parameters.")

        try:
            return self.browser.find_element(*locator_tuple)
        except NoSuchElementException:
            return None

    def get_element(self, element_name: str):
        """
        The method returns WebElement object according to its name in variable locators_dictionary.
        Expecting that the WebElement exists in the Dom model and visible. Expecting that the element_name is a one
        of locators_dictionary keys.
        If the wanted element doesn't exists or invisible NoSuchElement exception rises.
        :param element_name: str, locator name
        :return: WebElement object
        """
        if element_name in self.locators_dictionary.keys():
            try:
                WebDriverWait(self.browser, self.timeout).until(
                    ec.presence_of_element_located(self.locators_dictionary[element_name])
                )
            except(TimeoutException, StaleElementReferenceException):
                raise NoSuchElementException(f"There's no element '{element_name}' in the {self} DOM model.")
            try:
                WebDriverWait(self.browser, self.timeout).until(
                    ec.visibility_of_element_located(self.locators_dictionary[element_name])
                )
            except(TimeoutException, StaleElementReferenceException):
                raise ElementNotVisibleException(
                    f"The element '{element_name}' isn't visible in the {self}."
                )
            return self.find_element(element_name)
        else:
            raise Exception(f"There's no '{element_name}' element in the locators dictionary!")

    def click_on_element(self, element):
        """
        Just straightaway realization of clicking on element
        :param element: WebElement
        :return: None
        """
        self.get_element(element).click()

    def enter_text(self, element, text):
        """
        Just straightaway realization of entering text into the element
        :param element: WebElement
        :param text: str
        :return: None
        """
        self.get_element(element).send_keys(text)

import pytest

from pytest_bdd import parsers, given, when, then
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, ElementNotVisibleException
from .pages import PAGE_OBJECTS


MIRO_URL = 'https://miro.com'


@pytest.fixture(autouse=True)
def browser():
    browser = webdriver.Chrome()
    browser.implicitly_wait(10)
    yield browser
    browser.quit()


@pytest.fixture(autouse=True)
def context():
    class Context(object):
        pass

    return Context()


@given(parsers.parse('the "{endpoint}" endpoint is opened'))
def get_url(endpoint):
    context.url = f'{MIRO_URL}{endpoint}'
    browser.get(context.url)


@then(parsers.parse('the "{page_name}" page is displayed'))
@when(parsers.parse('the "{page_name}" page is displayed'))
def the_page_is_displayed(page_name):
    if page_name in PAGE_OBJECTS.keys():
        context.page = PAGE_OBJECTS[page_name](browser)
        context.page_name = page_name
    else:
        raise AttributeError(f"The page '{page_name}' doesn't exist")


@then(parsers.parse('the item "{item_name}" is visible'))
def the_item_is_displayed(item_name):
    try:
        context.page.get_element(item_name)
    except (NoSuchElementException, ElementNotVisibleException):
        raise AssertionError(f"The item '{item_name}' isn't displayed on the {context.page}.")


@then(parsers.parse('the current url is "{url}"'))
def check_url(url):
    assert browser.current_url == url, f"Wrong URL, expected {url}, instead of {browser.current_url}"


@when(parsers.parse('press the element "{element_name}"'))
def press_the_element(element_name):
    context.page.click_on_element(element_name)


@when(parsers.parse('enter the text "{text}" to the "{element_name}"'))
def enter_the_text_to_the_element(text, element_name):
    context.page.enter_text(element_name, text)

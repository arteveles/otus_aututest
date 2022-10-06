import time
from lesson_5.data_storage import HP_SEARCH_INPUT, HP_SEARCH_BUTTON, IPHONE, SEARCH_CARD, ASSERTION_VALUE_IPHONE
from lesson_5.data_storage import HP_FOOTER_INFO, HP_FOOTER_TEXT_ASSERTION
from selenium.webdriver.common.by import By


def test_home_page_positive(driver):
    driver.get(url=driver.base_url)
    assert driver.title == "Your Store"


def test_home_page_negative(driver):
    driver.get(url=driver.base_url)
    # driver.save_screenshot("test_home_page_firefox_negative.png")
    assert driver.title == "YourStore"


def test_home_page_menu(driver):
    driver.get(url=driver.base_url)
    time.sleep(3)
    menu_items = driver.find_elements(By.XPATH, HP_MENU_ITEMS)
    assert len(menu_items) == 8


def test_home_page_search(driver):
    driver.get(url=driver.base_url)
    search_input = driver.find_element(By.XPATH, HP_SEARCH_INPUT)
    search_input.click()
    search_input.clear()
    search_input.send_keys(IPHONE)
    time.sleep(1)
    search_button = driver.find_element(By.XPATH, HP_SEARCH_BUTTON)
    search_button.click()
    assertion_card = driver.find_element(By.XPATH, SEARCH_CARD)
    assert assertion_card.text == ASSERTION_VALUE_IPHONE


def test_home_page_footer(driver):
    driver.get(url=driver.base_url)
    footer = driver.find_element(By.XPATH, HP_FOOTER_INFO)
    footer.location_once_scrolled_into_view
    assert footer.text == HP_FOOTER_TEXT_ASSERTION

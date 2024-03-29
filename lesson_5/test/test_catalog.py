import time
from selenium.webdriver.common.by import By
from lesson_5.data_storage import URL_MONITOR_CATALOG
from lesson_5.data_storage import URL_OPENCART_CATALOG, HP_MENU_ITEMS, CATALOG_SEE_ALL, CATALOG_HEADER, \
    CATALOG_HEADER_TEXT
from lesson_5.data_storage import CATALOG_BUTTON_LIST, CATALOG_BTN_ADD_TO_FVT, CTG_ALERT_LGN, CTG_ASSERT_LGN
from lesson_5.data_storage import CTG_COMPARE_BTN, CTG_HEADER_COMPARE, CTG_HEADER_CMP_ASSERT
from lesson_5.data_storage import CTG_MENU_CMPS, CTG_COMPARE_ITEMS, CTG_CNT_ITEMS
from lesson_5.data_storage import CTG_SORT_TEXT, CTG_ASSERTED_SORT_TEXT


def test_visit_catalog_from_menu(driver):
    driver.get(url=URL_OPENCART_CATALOG)

    menu_desktop = driver.find_element(By.XPATH, HP_MENU_ITEMS)
    menu_desktop.click()

    all_desktops = driver.find_element(By.XPATH, CATALOG_SEE_ALL)
    all_desktops.click()

    time.sleep(3)

    desktop_header = driver.find_element(By.XPATH, CATALOG_HEADER)
    assert desktop_header.text == CATALOG_HEADER_TEXT


def test_catalog_add_to_favourite(driver):
    driver.get(url=URL_OPENCART_CATALOG)

    time.sleep(3)
    print("sleep 3 sec")

    button_list = driver.find_element(By.XPATH, CATALOG_BUTTON_LIST)
    button_list.click()

    add_to_fvt = driver.find_element(By.XPATH, CATALOG_BTN_ADD_TO_FVT)
    add_to_fvt.click()

    assertion_text = driver.find_element(By.XPATH, CTG_ALERT_LGN)
    assert assertion_text.text == CTG_ASSERT_LGN


def test_catalog_compare(driver):
    driver.get(url=URL_OPENCART_CATALOG)

    time.sleep(1)

    click_btn_compare = driver.find_element(By.XPATH, CTG_COMPARE_BTN)
    click_btn_compare.click()

    time.sleep(2)

    assertion_header = driver.find_element(By.XPATH, CTG_HEADER_COMPARE)
    assert assertion_header.text == CTG_HEADER_CMP_ASSERT


def test_compare_count_prod(driver):
    driver.get(url=URL_OPENCART_CATALOG)

    click_menu = driver.find_element(By.XPATH, CTG_MENU_CMPS)
    click_menu.click()

    time.sleep(2)

    remember_menu_items = driver.find_element(By.XPATH, CTG_COMPARE_ITEMS)
    count_of_menu_items = remember_menu_items.text[10]
    remember_menu_items.click()

    time.sleep(2)

    count_items_in_page = driver.find_elements(By.XPATH, CTG_CNT_ITEMS)
    assert str(len(count_items_in_page)) == count_of_menu_items


def test_sort(driver):
    driver.get(url=URL_MONITOR_CATALOG)

    sort_text = driver.find_element(By.XPATH, CTG_SORT_TEXT).text
    assert sort_text == CTG_ASSERTED_SORT_TEXT

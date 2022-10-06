from selenium.webdriver.common.by import By

from lesson_5.data_storage import URL_PRODUCT_CARD
from lesson_5.data_storage import EL1_PRODUCT_CARD, EL2_ADD_BTN, EL3_FAVOURITE_BTN
from lesson_5.data_storage import EL4_COMPARE_BTN, EL5_CARD_IMAGE, EL2_ASSERTION_TEXT


def test_product_card_fixture(driver):
    driver.get(url=URL_PRODUCT_CARD)

    product_card = driver.find_element(By.XPATH, EL1_PRODUCT_CARD)
    assert product_card

    add_btn = driver.find_element(By.XPATH, EL2_ADD_BTN)
    assert add_btn.text.lower() == EL2_ASSERTION_TEXT.lower()

    favourite_btn = driver.find_element(By.XPATH, EL3_FAVOURITE_BTN)
    assert favourite_btn

    compare_btn = driver.find_element(By.XPATH, EL4_COMPARE_BTN)
    assert compare_btn

    card_image = driver.find_element(By.XPATH, EL5_CARD_IMAGE)
    assert card_image

from lesson_5.data_storage import URL_OPENCART


def test_home_page_positive(driver):
    driver.get(url=driver.base_url)
    assert driver.title == "Your Store"


def test_home_page_negative(driver):
    driver.get(url=driver.base_url)
    # driver.save_screenshot("test_home_page_firefox_negative.png")
    assert driver.title == "YourStore"


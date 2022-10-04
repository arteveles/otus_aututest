from lesson_5.data_storage import URL_OPENCART


def test_home_page_firefox_positive(driver):
    driver.get(url=URL_OPENCART)
    assert driver.title == "Your Store"


def test_home_page_firefox_negative(driver):
    driver.get(url=URL_OPENCART)
    # driver.save_screenshot("test_home_page_firefox_negative.png")
    assert driver.title == "YourStore"

# def test_home_page_chrome():
#     chrome = webdriver.Chrome(executable_path=os.path.expanduser(CHROMEDRIVER_PATH))
#     chrome.get(url=URL_OPENCART)

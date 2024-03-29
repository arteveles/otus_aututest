URL_OPENCART = "http://10.0.2.15:8081/"
URL_OPENCART_CATALOG = "http://10.0.2.15:8081/desktops"
URL_MONITOR_CATALOG = "http://10.0.2.15:8081/component/monitor"

# selectors home page
HP_MENU_ITEMS = "//div[@class='collapse navbar-collapse navbar-ex1-collapse']/ul/li"
HP_SEARCH_INPUT = "//div[@id='search']/input"
HP_SEARCH_BUTTON = "//div/span/button[@class='btn btn-default btn-lg']"
IPHONE = "iphone"
SEARCH_CARD = "//div[@class='caption']/h4/a[text()='iPhone']"
ASSERTION_VALUE_IPHONE = "iPhone"
HP_FOOTER_INFO = "//div[@class='row']/div[@class='col-sm-3']/h5"
HP_FOOTER_TEXT_ASSERTION = "Information"

# selectors catalog page
CATALOG_SEE_ALL = "//div[@class='dropdown-menu']/a[text() = 'Show All Desktops']"
CATALOG_HEADER = "//div[@class='col-sm-9']/h2"
CATALOG_HEADER_TEXT = "Desktops"
CATALOG_BUTTON_LIST = "//div[@class='btn-group btn-group-sm']/button[@id='list-view']"
CATALOG_BTN_ADD_TO_FVT = "//div[@class='button-group']/button[2]"
CTG_ALERT_LGN = "//div[@class='alert alert-success alert-dismissible']/child::a[@href='http://10.0.2.15:8081/index.php?route=account/login']"
CTG_ASSERT_LGN = "login"

CTG_COMPARE_BTN = "//div[@class='form-group']"
CTG_HEADER_COMPARE = "//h1[text()='Product Comparison']"
CTG_HEADER_CMP_ASSERT = "Product Comparison"

CTG_MENU_CMPS = "//ul[@class='nav navbar-nav']/child::li[3]"
CTG_COMPARE_ITEMS = "//ul[@class='nav navbar-nav']/child::li[3]//child::li[2]/a"
CTG_CNT_ITEMS = "//div[@class='row'][3]/child::div"
CTG_SORT_TEXT = "//div/label[@class='input-group-addon' and @for='input-sort']"
CTG_ASSERTED_SORT_TEXT = "Sort By:"

# product card
URL_PRODUCT_CARD = "http://10.0.2.15:8081/component/monitor"
EL1_PRODUCT_CARD = "//div[@class='product-thumb']"
EL2_ADD_BTN = "//div[@class='button-group']/button[1]"
EL3_FAVOURITE_BTN = "//div[@class='button-group']/button[2]"
EL4_COMPARE_BTN = "//div[@class='button-group']/button[3]"
EL5_CARD_IMAGE = "//div[@class='image']/a/img[@class='img-responsive']"
EL2_ASSERTION_TEXT = "Add to Cart"

# admin page as AP
AP_URL = "http://10.0.2.15:8081/admin/"
EL_1_INP_USERN = "//input[@name='username']"
EL_1_INP_UN_POSITV = "user"
EL_1_INP_UN_NEGAV = "admin"
EL_2_INP_PASS = "//input[@name='password']"
EL_2_INP_PASS_POSIV = "bitnami"
EL_2_INP_PASS_NEGAV = "bitnami1"
EL_3_LOG_BTN = "//button[@type='submit']"
EL_4_ALERT = "//div[@class='alert alert-danger alert-dismissible']"
EL_4_ALERT_ASSERT_TEXT = "No match for Username and/or Password.\n"
EL_4_ALERT_ASSERT_TEXT_2 = " Warning: Your account has exceeded allowed number of login attempts. Please try again in 1 hour or reset password.\n"
EL_5_VERIFY = "//span[@class='hidden-xs hidden-sm hidden-md']"
EL_5_VERIFY_ASSERT_TEXT = "Logout"

# registration page
REG_PAGE = "http://10.0.2.15:8081/index.php?route=account/register"
EL_REG_FN = "//input[@name='firstname']"
EL_REG_FN_VALUE = "test_firstname"
EL_REG_LN = "//input[@name='lastname']"
EL_REG_LN_VALUE = "test_lastname"
EL_REG_MAIL = "//input[@name='email']"
EL_REG_MAIL_VALUE = "123test@gmail.com"
EL_REG_PHONE = "//input[@name='telephone']"
EL_REG_PHONE_VALUE = "+77777777777"
EL_REG_PASS = "//input[@name='password']"
EL_REG_PASS_VALUE = "password"
EL_REG_PASS_CONFIRM = "//input[@name='confirm']"
EL_REG_PASS_CONFIRM_VALUE = "password"
EL_REG_NO_RDB = "//input[@name='newsletter' and @value='0']"
EL_REG_CHBX = "//input[@name='agree']"
EL_REG_CONT_BTN = "//input[@value='Continue']"
EL_REG_ASSERT = "//div[@class='alert alert-danger alert-dismissible']"




import time

def test_basket_is_present(browser):
    browser.get("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/")
    time.sleep(30)
    browser.find_element_by_id("add_to_basket_form")
    
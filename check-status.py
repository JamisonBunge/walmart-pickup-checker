from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.firefox.webdriver import FirefoxProfile
import time
from selenium.webdriver.firefox.options import Options

options = Options()
options.headless = True
#driver = webdriver.Chrome()
#from selenium.webdriver.chrome.options import Options

# options = Options()
# options.add_argument("user-data-dir=/tmp/jami")
#options.addArguments("user-data-dir=/path/to/your/custom/profile");


#profile = FirefoxProfile("/tmp/jamii")
#driver = webdriver.Firefox(profile)
driver = webdriver.Firefox(options=options)
#driver = webdriver.Firefox()
driver.implicitly_wait(3)
no_slots_message = "All of today and tomorrow's times are currently booked."
positive_response = "You can checkout. (or an error unsure right now)"
negitive_response = "No checkout times."
response = "unset"




def site_login():
    WebDriverWait(driver,10)
    driver.get("https://www.walmart.com/account/login?tid=0&vid=2&returnUrl=%2F")
    driver.find_element_by_id("email").send_keys("email")
    driver.find_element_by_id("password").send_keys("password")
    driver.find_element_by_css_selector("#sign-in-form > button.button.m-margin-top.text-capitalize").click()
    WebDriverWait(driver,10)
    #driver.get("https://grocery.walmart.com/checkout/book-slot")
    # WebDriverWait(driver,60)
    # driver.close()

def go_to_checkout():
    driver.get("https://grocery.walmart.com/checkout/book-slot")



    #sign-in-form > button.button.m-margin-top.text-capitalize
    #driver.find_element_by_id("signin-submit-btn").click()
     #driver.find_element_by_xpath('//button[contains(text(), "Sign In")]').click()
    # signin-submit-btn

def getHtml():
    html = driver.page_source
    if no_slots_message in html:
        response = negitive_response
    else:
        response = positive_response

    print(response)
    #html = driver.execute_script("return document.documentElement.outerHTML;")
    #print(html)

def main():
    site_login()
    time.sleep(5)
    go_to_checkout()
    time.sleep(5)
    getHtml()
    driver.close()


if __name__ == '__main__':
    main()

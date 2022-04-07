from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import time

chrom_driver_path ="./chromedriver_linux64/chromedriver"

driver = webdriver.Chrome(executable_path=chrom_driver_path)

driver.get("https://www.linkedin.com/jobs/search/?f_AL=true&f_E=3%2C4&f_JT=F%2CP&f_TPR=r86400&geoId=103644278&keywords=reactjs&location=United%20States")




sign_in_btn = driver.find_element_by_link_text("Sign in")

sign_in_btn.click()

email_field = driver.find_element_by_id("username")
email_field.send_keys("your email")


password_field = driver.find_element_by_id("password")
password_field.send_keys("your password")
password_field.send_keys(Keys.ENTER)

all_listings = driver.find_elements_by_css_selector(".job-card-container--clickable")

for listing in all_listings:
    print("called")
    listing.click()
    time.sleep(2)
    apply_btn = driver.find_element_by_css_selector(".jobs-apply-button ")
    apply_btn.click()
    time.sleep(2)
    next_btn = driver.find_element_by_css_selector("footer button")
    next_btn.click()
    time.sleep(2)

    review_btn = driver.find_elements_by_class_name("artdeco-button--primary")

    if review_btn.__getattribute__("data-control-name") == "continue_unify":
        close_button = driver.find_elements_by_class_name("artdeco-modal__dismiss")
        close_button.click()
        time.sleep(2)
        discard_btn = driver.find_elements_by_class_name("artdeco-modal__confirm-dialog-btn")[1]
        discard_btn.click()
        print("Complex Application")
    else:
        review_btn.click()
        time.sleep(2)
        submit_btn = driver.find_elements_by_class_name("artdeco-button--primary")
        if submit_btn.__getattribute__("data-control-name") == "submit_unify":
            submit_btn.click()
            time.sleep(2)
            close_button = driver.find_elements_by_class_name("artdeco-modal__dismiss")
            close_button.click()
        else:
            close_button = driver.find_elements_by_class_name("artdeco-modal__dismiss")
            close_button.click()
            time.sleep(2)
            discard_btn = driver.find_elements_by_class_name("artdeco-modal__confirm-dialog-btn")[1]
            discard_btn.click()
            print("Complex Application")
            continue
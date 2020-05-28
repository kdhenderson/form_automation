from selenium import webdriver
import time

chrome_browser = webdriver.Chrome('./chromedriver')

chrome_browser.maximize_window()
chrome_browser.get('https://www.seleniumeasy.com/test/basic-first-form-demo.html')

assert 'Selenium Easy Demo' in chrome_browser.title
assert 'Show Message' in chrome_browser.page_source

user_message = chrome_browser.find_element_by_id('user-message')
user_message.clear()
user_message.send_keys('I AM EXTRA COOOOL')

show_message_button = chrome_browser.find_element_by_class_name('btn-default')
show_message_button.click()

output_message = chrome_browser.find_element_by_css_selector('#display')

assert 'I AM EXTRA COOOOL' in output_message.text

time.sleep(1)

chrome_browser.close()

from selenium import webdriver

print(' Input your LinkedIn email address')
userEmail = input()

print(' Input your LinkedIn email password')
userPassword = input()

browser = webdriver.Firefox()
browser.get('https://www.linkedin.com/uas/login')

emailElem = browser.find_element_by_id('session_key-login')
emailElem.send_keys(userEmail)

passwordElem = browser.find_element_by_id('session_password-login')
passwordElem.send_keys(userPassword)
passwordElem.submit()
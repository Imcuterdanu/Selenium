from selenium import webdriver

print(' Input your LinkedIn email address')
userEmail = input()

print(' Input your LinkedIn email password')
userPassword = input()

browser = webdriver.Firefox()
browser.get('https://www.linkedin.com/uas/login')

logInElem = browser.find_element_by_id('session_key-login')
logInElem.click()

emailElem = browser.find_element_by_id('session_key-login')
emailElem.send_keys(userEmail)

passwordElem = browser.find_element_by_id('session_key-password')
passwordElem.click()

passwordElem.send_keys(userPassword)
emailElem.submit()
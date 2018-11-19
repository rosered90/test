# _*_ coding:utf-8 _*_
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time

login_url='https://passport.jd.com/uc/login'
uid='18668034256'
pwd=''

browser=webdriver.Chrome()
wait=WebDriverWait(browser, 10)

def login():
    try:
        browser.get(login_url)
        login_tab_u=wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div.login-tab:nth-child(3)")))
        login_tab_u.click()#这里我们没有获取那个a标签，而是直接获取外层的div标签，比较简单而且方便
        uid_input = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#loginname")))
        pwd_input=wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#nloginpwd")))
        login_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#loginsubmit")))
        uid_input.send_keys(uid)
        pwd_input.send_keys(pwd)
        login_button.click()
    except TimeoutException:
        login()

def main():
    login()
    time.sleep(5)
    browser.close()

if __name__=='__main__':
    main()
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
while True:
    driver = webdriver.Chrome(executable_path=r'/Users/jodio/Downloads/chromedriver')
    driver.get('https://zlapp.fudan.edu.cn/site/ncov/fudanDaily')
    element_username = driver.find_element_by_name("username")
    element_password = driver.find_element_by_name("password")
    element_username.send_keys("your username")
    element_password.send_keys("your password")
    element_password.send_keys(Keys.RETURN)
    driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/section/div[4]/ul/li[6]/div/input').click()
    driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/section/div[5]/div/a').click()
    time.sleep(86400)


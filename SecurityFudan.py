import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
while True:
    driver = webdriver.Chrome()
    driver.get('https://zlapp.fudan.edu.cn/site/ncov/fudanDaily')
    element_username = driver.find_element_by_name("username")
    element_password = driver.find_element_by_name("password")
    element_username.send_keys("你的账号")
    element_password.send_keys("你的密码")
    element_password.send_keys(Keys.RETURN)
    time.sleep(10)
    try:
        driver.find_element_by_xpath('/html/body/div[4]/div/div[2]/div').click()
    except:
        pass
    time.sleep(10)
    try:
        driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/section/div[4]/ul/li[6]/div/input').click()
    except:
        pass
    time.sleep(10) 
    try:
        driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/section/div[5]/div/a').click()
    except:
        pass   
    time.sleep(10)    
    try:
        driver.find_element_by_xpath('/html/body/div[6]/div/div[2]/div[2]').click()
    except:
        pass
    driver.close()
    time.sleep(86400)

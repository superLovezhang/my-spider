from selenium import webdriver

# options = webdriver.ChromeOptions()
# options.add_argument("--headless")
# browser = webdriver.Chrome(options=options)
browser = webdriver.Chrome()
browser.get('https://kyfw.12306.cn/otn/resources/login.html')
browser.implicitly_wait(5)
browser.find_element_by_xpath("//ul[@class='login-hd']/li[2]").click()


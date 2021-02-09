# from selenium import webdriver

# options = webdriver.ChromeOptions()
# options.add_argument("--headless")
# browser = webdriver.Chrome(options=options)
# browser = webdriver.Chrome()
# browser.get('https://kyfw.12306.cn/otn/resources/login.html')
# browser.implicitly_wait(5)
# browser.find_element_by_xpath("//ul[@class='login-hd']/li[2]").click()

'''
普通连接redis
'''
# import redis
#
# client = redis.Redis(host="localhost", port="6379", password=None, decode_responses=True) # decode_responses=True返回字符串而不是子节
# print(client.get("name"))
# client.close()

'''
连接池连接redis
'''
import redis

pool = redis.ConnectionPool(decode_responses=True)
client = redis.Redis(connection_pool=pool)
print(client.get("name"))
client.close()


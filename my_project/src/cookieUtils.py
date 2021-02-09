from selenium import webdriver
from .redisUtils import RedisUtils

class CookieUtils:
    @staticmethod
    def getCookies():
        broswer = webdriver.Chrome()
        broswer.get('http://exercise.kingname.info/exercise_login_success')
        broswer.implicitly_wait(1)
        broswer.find_element_by_xpath("//input[@name='username']").send_keys('kingname')
        broswer.find_element_by_xpath("//input[@name='password']").send_keys('genius')
        broswer.find_element_by_xpath("//button[@class='login']").click()
        cookies = broswer.get_cookies()
        broswer.close()
        redis = RedisUtils.client
        redis.set('cookies', cookies)
        return cookies
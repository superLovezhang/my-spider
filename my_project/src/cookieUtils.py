from selenium import webdriver
from .redisUtils import RedisUtils
import json

class CookieUtils:
    def defaultOperate(broswer):
        broswer.get('http://exercise.kingname.info/exercise_login_success')
        broswer.implicitly_wait(1)
        broswer.find_element_by_xpath("//input[@name='username']").send_keys('kingname')
        broswer.find_element_by_xpath("//input[@name='password']").send_keys('genius')
        broswer.find_element_by_xpath("//button[@class='login']").click()

    @staticmethod
    def getCookies(cookieOperate = defaultOperate):
        redis = RedisUtils.getClient()
        cookiesFromRedis = redis.get('cookies')
        if redis.get('cookies') is not None:
            return list(json.loads(cookiesFromRedis))
        option = webdriver.ChromeOptions()
        option.add_argument('--headless')
        broswer = webdriver.Chrome(options=option)
        cookieOperate(broswer)
        # broswer.implicitly_wait(0.5)
        cookies = broswer.get_cookies()
        broswer.close()
        redis.set('cookies', json.dumps(cookies))
        return cookies

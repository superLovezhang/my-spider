BOT_NAME = 'my_project'

SPIDER_MODULES = ['my_project.spiders']
NEWSPIDER_MODULE = 'my_project.spiders'

PROXIES = [
    'https://36.248.132.59:9999',
    'https://175.42.68.179:9999',
    'http://175.42.158.73:9999'
]

USER_AGENT_LIST = [
"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36",
  "Dalvik/1.6.0 (Linux; U; Android 4.2.1; 2013022 MIUI/JHACNBL30.0)",
  "Mozilla/5.0 (Linux; U; Android 4.4.2; zh-cn; HUAWEI MT7-TL00 Build/HuaweiMT7-TL00) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1",
  "AndroidDownloadManager",
  "Apache-HttpClient/UNAVAILABLE (java 1.4)",
  "Dalvik/1.6.0 (Linux; U; Android 4.3; SM-N7508V Build/JLS36C)",
  "Android50-AndroidPhone-8000-76-0-Statistics-wifi",
  "Dalvik/1.6.0 (Linux; U; Android 4.4.4; MI 3 MIUI/V7.2.1.0.KXCCNDA)",
  "Dalvik/1.6.0 (Linux; U; Android 4.4.2; Lenovo A3800-d Build/LenovoA3800-d)",
  "Lite 1.0 ( http://litesuits.com )",
  "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; .NET4.0C; .NET4.0E; .NET CLR 2.0.50727)",
  "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.122 Safari/537.36 SE 2.X MetaSr 1.0",
  "Mozilla/5.0 (Linux; U; Android 4.1.1; zh-cn; HTC T528t Build/JRO03H) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30; 360browser(securitypay,securityinstalled); 360(android,uppayplugin); 360 Aphone Browser (2.0.4)",
]

# 请求头得浏览器标识
USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36'

# 遵循爬虫协议
ROBOTSTXT_OBEY = False

# 并发请求数 默认16
# CONCURRENT_REQUESTS = 32

# See also autothrottle settings and docs
# DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
# CONCURRENT_REQUESTS_PER_DOMAIN = 16
# CONCURRENT_REQUESTS_PER_IP = 16

# 是否允许携带cookie
# COOKIES_ENABLED = True

# Disable Telnet Console (enabled by default)
# TELNETCONSOLE_ENABLED = False

# 默认请求头
# DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
# }

# 爬虫中间件
# SPIDER_MIDDLEWARES = {
#    'my_project.middlewares.MyProjectSpiderMiddleware': 543,
#    'my_project.middlewares.UAMiddleware': 600,
# }

# 下载中间件 直接操作request和response的
DOWNLOADER_MIDDLEWARES = {
    'my_project.middlewares.DoubanDownloaderMiddleware': 543,
    'my_project.middlewares.CookieMiddleware': 542,
    # 'my_project.middlewares.ProxyMiddleware': 543,
}

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
# EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
# }

# 管道流
# ITEM_PIPELINES = {
#     'my_project.pipelines.MyProjectPipeline': 300,
# }

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
# AUTOTHROTTLE_ENABLED = True
# The initial download delay
# AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
# AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
# AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
# AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
# HTTPCACHE_ENABLED = True
# HTTPCACHE_EXPIRATION_SECS = 0
# HTTPCACHE_DIR = 'httpcache'
# HTTPCACHE_IGNORE_HTTP_CODES = []
# HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'

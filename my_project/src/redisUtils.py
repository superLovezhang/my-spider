import redis

"""
单例Redis连接池工具类
"""


class RedisUtils:
    param = {
        'host': 'localhost',
        'port': 6379,
        'password': None,
        'decode_responses': True,  # 取出来的不是子节 而是字符串
        'max_connections': 10
    }
    client = None

    def __init__(self, params=None):
        if params is not None:
            RedisUtils.param = params
        RedisUtils._initPoolClient()

    def __del__(self):
        RedisUtils.client.close()

    @classmethod
    def _initPoolClient(cls):
        pool = redis.ConnectionPool(RedisUtils.param)
        cls.client = redis.Redis(connection_pool=pool)

    @classmethod
    def _initClient(cls):
        cls.client = redis.Redis(decode_responses=True)

    @classmethod
    def getClient(cls):
        if cls.client is None:
            cls._initClient()
        return cls.client

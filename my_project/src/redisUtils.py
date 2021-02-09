import redis

class RedisUtils():
    param: {
        'host': 'localhost',
        'port': 6379,
        'password': None,
        'decode_responses': True,
        'max_connections': 1024
    }
    client: None

    def __init__(self, params=None):
        if not params is None: RedisUtils.param = params
        self.__initClient()

    def __del__(self):
        RedisUtils.client.close()

    def __initClient(self):
        pool = redis.ConnectionPool(RedisUtils.param)
        RedisUtils.client = redis.Redis(connection_pool=pool)

    @property.getter
    def client(self):
        if RedisUtils.client is None:
            self.__initClient()
        return RedisUtils.client
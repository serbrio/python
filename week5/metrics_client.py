import socket
import time


class Client():
    def __init__(self, host, port, timeout=None):
        self.host = host
        self.port = port
        self.timeout = timeout

    @staticmethod
    def get_timestamp():
        return str(int(time.time()))

    def get(self, key):
        return {}
        pass

    def put(self, key, value, timestamp=None):
        timestamp = timestamp or self.get_timestamp()
        print('put key %s and value %s at time %s' % (key, value, timestamp))
        pass


class ClientError(Exception):  # hope to use it
    pass




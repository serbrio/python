import socket
import time


class Client:
    def __init__(self, host, port, timeout=None):
        self.host = host
        self.port = port
        self.timeout = timeout
        self.cli_sock = self.cli_sock(self.host, self.port, self.timeout)

    def cli_sock(self, host, port, timeout):
        sock = socket.create_connection((host, port), timeout)
        return sock

    @staticmethod
    def get_timestamp():
        return str(int(time.time()))

    def get(self, key):
        try:
            key = str(key)
            self.cli_sock.sendall(("get %s\n" % key).encode("utf-8"))
        except Exception:
            raise ClientError

    def put(self, key, value, timestamp=None):
        timestamp = timestamp or self.get_timestamp()
        try:
            if not type(key) == str and not type(value) == float and not type(timestamp) == int:
                raise ClientError
            self.cli_sock.sendall(("put %s %s %s\n" % (key, value, timestamp)).encode("utf-8"))
        except ClientError:
            print('client error')


class ClientError(Exception):  # hope to use it
    pass


# with socket.create_connection(("127.0.0.1", 10001), 5) as sock:
#    # set socket read timeout
#    sock.settimeout(2)
#    try:
#        sock.sendall("ping".encode("utf-8"))
#    except socket.timeout:
#        print("send data timeout")
#    except socket.error as ex:
#        print("send data error: ", ex)

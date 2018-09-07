import requests
import ssl
import socket
import argparse
from datetime import datetime


#hosts = []

parser = argparse.ArgumentParser()
parser.add_argument('--hosts', default='data.browser.mail.ru;updtbrwsr.com;updtapi.com;brwsrapi.com;'
                    'mrbrwsr.com;savebrwsr.com;svbrwsr.com', help='List of host names divided by a semicolon'
                    'Example: "data.browser.mail.ru;updtbrwsr.com"')
parser.add_argument('--days_to_exp', default='10', help='Days to expiration; alarm if certificate'
                                                               'expires in given days or less.')
args = parser.parse_args()
hosts = args.hosts.split(';')
days = int(args.days_to_exp)


def main_check(host):
    host = 'https://' + host
    try:
        requests.get(host)
    except Exception as err:
        print("Main check failed for %s" % host)
        print(err, '\n')
        return False
    return True


def ssl_expiration_date_check(host, d):
    ctx = ssl.create_default_context()
    s = ctx.wrap_socket(socket.socket(), server_hostname=host)
    s.connect((host, 443))
    cert = s.getpeercert()
    expires_at_raw = cert['notAfter']
    expires_at_raw = ' '.join(expires_at_raw.split())
    expires_at = datetime.strptime(expires_at_raw, '%b %d %H:%M:%S %Y %Z')
    delta = expires_at - datetime.now()
    if delta.days > d:
        pass
    else:
        print("Certificate for %s will expire in %s days." % (host, str(delta.days)))


def main():
    for host in hosts:
        if main_check(host):
            print('Main check passed for %s' % host)
            ssl_expiration_date_check(host, days)
            print('\n')


if __name__ == '__main__':
    main()



#def test_f(hosts):
    #hs = hosts.split(';')
    #for host in hs:
#        assert main_check(hosts) is True



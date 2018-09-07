#just test version, it does not work

import pytest


def pytest_addoption(parser):
    parser.addoption("--hosts", default="data.browser.mail.ru",
                     #;updtbrwsr.com;updtapi.com;brwsrapi.com;mrbrwsr.com;savebrwsr.com;svbrwsr.com",
                     help="List of host names divided by a semicolon")


def pytest_generate_tests(metafunc):
    if 'hosts' in metafunc.fixturenames:
        metafunc.parametrize("hosts", metafunc.config.getoption('hosts'))


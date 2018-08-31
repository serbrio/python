hosts = ['one', 'two', 'three']

def func(h):
    if h != 'two':
        r = 'https://' + h + '.com'
    else:
        r = 'opa!!!'
    return r

def test_f():
    for host in hosts:
        assert func(host) == 'https://' + host + '.com'

from http.cookies import SimpleCookie


def parse_cookie(query: str) -> dict:
    cookie = SimpleCookie()
    cookie.load(query)
    output_cookie = {k: v.value for k, v in cookie.items()}
    return output_cookie


long_string = 'BAh7DUkiD3Nlc3NpbWVfZV9uYW1lBjsARkkiH1BhY2lmaWMgVGltZSAoVVMgJiBDYW5hZgitGEpBjsAVEkiFXNpZ25pbl9wZXJzb25' \
              'faWQGOwBGaQMSvRpJIhRsYXN0X2xvZ2luX2RhdGUGOwBGVTogQWN0aXZlU3VwcG9ydDo6VGltZVdpdGhab25lWwhJdToVGltZQ2T3' \
              'RzAAABA7QY6CXpvbmVJIghVVEMGOwBUSSIfUGFjaWZpZWRfZGFzaGJvYXJkX21lc3NhZ2UGOwBGVA%3D%3D--6ce6ef4bd6bc1a4' \
              '69164b6740e7571c754b31cca'

if __name__ == '__main__':
    assert parse_cookie('name=Dima;') == {'name': 'Dima'}
    assert parse_cookie('') == {}
    assert parse_cookie('any_information') == {}
    assert parse_cookie('name=Dima;age=28;') == {'name': 'Dima', 'age': '28'}
    assert parse_cookie('name=Dima=User;age=28;') == {'name': 'Dima=User', 'age': '28'}
    assert parse_cookie('type=high-heels') == {'type': 'high-heels'}
    assert parse_cookie('units=metric;time=1400') == {'units': 'metric', 'time': '1400'}
    assert parse_cookie('keebler=E=mc2') == {'keebler': 'E=mc2'}
    assert parse_cookie('devicePixelRatio=1; ident=exists; __utma=13103r6942.2918;') == {'devicePixelRatio': '1',
                                                                                         'ident': 'exists',
                                                                                         '__utma': '13103r6942.2918'}
    assert parse_cookie(
        'devicePixelRatio=1;ident=exists;'
        '__utma=13103r6942.2918;'
        't_session='
        'BAh7DUkiD3Nlc3NpbWVfZV9uYW1lBjsARkkiH1BhY2lmaWMgVGltZSAoVVMgJiBDYW5hZgitGEpBjsAVEkiFXNpZ25pbl9wZXJzb25' 
        'faWQGOwBGaQMSvRpJIhRsYXN0X2xvZ2luX2RhdGUGOwBGVTogQWN0aXZlU3VwcG9ydDo6VGltZVdpdGhab25lWwhJdToVGltZQ2T3' 
        'RzAAABA7QY6CXpvbmVJIghVVEMGOwBUSSIfUGFjaWZpZWRfZGFzaGJvYXJkX21lc3NhZ2UGOwBGVA%3D%3D--6ce6ef4bd6bc1a4' 
        '69164b6740e7571c754b31cca') == {
               'devicePixelRatio': '1',
               'ident': 'exists',
               '__utma': '13103r6942.2918',
               't_session': long_string}


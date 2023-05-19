from urllib.parse import urlparse, parse_qs
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





def parse(URL: str) -> dict:
    parsed_url = urlparse(URL)
    output = parse_qs(parsed_url.query)
    for key, value in output.items():
        output.update({key: str(value[0])})
    return output


if __name__ == '__main__':
    assert parse('https://example.com/path/to/page?name=ferret&color=purple') == {'name': 'ferret', 'color': 'purple'}
    assert parse('https://example.com/path/to/page?name=ferret&color=purple&') == {'name': 'ferret', 'color': 'purple'}
    assert parse('http://example.com/') == {}
    assert parse('http://example.com/?') == {}
    assert parse('http://example.com/?name=Dima') == {'name': 'Dima'}
    assert parse('/shoes/women-shoes?type=high-heels') == {'type': 'high-heels'}
    assert parse('GET /surfreport/beachId?days=3&units=metric&time=1400') == {'days': '3', 'units': 'metric',
                                                                              'time': '1400'}
    assert parse('GET /surfreport/beachId?days=3&&&units=metric&&&time=1400') == {'days': '3', 'units': 'metric',
                                                                                  'time': '1400'}
    assert parse('https://www.google.com/search?q=abstract+api') == {'q': 'abstract api'}
    assert parse('https://www.google.com/search?q=abstract+api&rlz=1C1CHBF_enUS923US923&oq=abstract+api&aqs=chrome'
                 '..69i57j0i10i433j0j0i10i433j0i10l6.1705j0j7&sourceid=chrome&ie=UTF-8') == {'q': 'abstract api',
                                                                                             'rlz': '1C1CHBF_enUS923'
                                                                                                    'US923',
                                                                                             'oq': 'abstract api',
                                                                                             'aqs': 'chrome'
                                                                                                    '..69i57j0i10i433j'
                                                                                                    '0j0i10i433j0i10l'
                                                                                                    '6.1705j0j7',
                                                                                             'sourceid': 'chrome',
                                                                                             'ie': 'UTF-8'}


from urllib.parse import urlparse, parse_qs


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

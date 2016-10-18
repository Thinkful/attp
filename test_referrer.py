import unittest

from flask import Flask, request

app = Flask(__name__)


@app.route('/')
def index():
    return unicode(request.referrer or '')


class TestReferrer(unittest.TestCase):

    def test(self):
        c = app.test_client()
        resp = c.get('/', headers={'Referer': '/somethingelse'})
        self.assertEqual('/somethingelse', resp.data)

    def test_empty(self):
        c = app.test_client()
        resp = c.get('/')
        self.assertEqual('', resp.data)

    def test_regex(self):
        from attp import get_domain

        urls = {
            'https://medium.com/famous-blog/': 'medium.com',
            'https://medium.com/': 'medium.com',
            'http://www.medium.com': 'www.medium.com',
            '/verdura': None,
            None: None
        }

        for url, domain in urls.items():
            self.assertEqual(get_domain(url), domain)


if __name__ == '__main__':
    unittest.main()

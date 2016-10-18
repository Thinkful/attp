import re
import os

from flask import Flask, request, redirect

app = Flask(__name__)


def get_domain(url):
    mtch = re.match('https?://(?P<domain>[\w\d.\-\_]+)/?(.+)?', url or '')
    if mtch and mtch.groupdict():
        return mtch.groupdict().get('domain', None)
    return None


@app.route('/')
def index():
    rfrr = request.referrer or ''
    dmn = get_domain(rfrr)
    utm = '?utm_referer={}'.format(dmn) if dmn else ''

    return redirect(
        'https://www.thinkful.com/atlanta-tech-talent-pipeline/{}'.format(utm),
        code=302)


if __name__ == '__main__':
    app.run(port=os.environ.get('PORT', 8080))

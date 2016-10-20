import re
import os
import logging

from flask import Flask, request, redirect

app = Flask(__name__)


l = logging.getLogger(__name__)
l.addHandler(logging.StreamHandler())
l.level = logging.INFO


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

    l.info("Redirecting with utm={}".format(utm))

    return redirect(
        'https://www.thinkful.com/atlanta-tech-talent-pipeline/{}'.format(utm),
        code=302)


if __name__ == '__main__':
    app.run(port=os.environ.get('PORT', 8080))

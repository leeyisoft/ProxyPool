from flask import Flask
from flask import g
from flask import request

from .setting import api_sign_key
from .utils import md5
from .db import RedisClient

__all__ = ['app']

app = Flask(__name__)


def get_conn():
    if not hasattr(g, 'redis'):
        g.redis = RedisClient()
    return g.redis


@app.route('/')
def index():
    return '<h2>Welcome to Proxy Pool System</h2>'


@app.route('/random')
def get_proxy():
    """
    Get a proxy
    :return: 随机代理
    """
    sign = request.args.get('sign')
    if md5(api_sign_key)!=sign:
        return 'sign error: %s' % sign
    conn = get_conn()
    return conn.random()


@app.route('/count')
def get_counts():
    """
    Get the count of proxies
    :return: 代理池总量
    """
    sign = request.args.get('sign')
    if md5(api_sign_key)!=sign:
        return 'sign error: %s' % sign
    conn = get_conn()
    return str(conn.count())


if __name__ == '__main__':
    app.run()

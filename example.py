#!/usr/bin/env python
# coding: utf-8
from __future__ import print_function

import tornado.ioloop
import greenlet
from functools import wraps
import mykaze

def within_greenlet(func):
    @wraps(func)
    def meth(*args, **kw):
        g = greenlet.greenlet(lambda: func(*args, **kw))
        return g.switch()
    return meth

@within_greenlet
def sample():
    #conn = mykaze.connect(host='127.0.0.1', unix_socket='/tmp/mysql.sock', user='root', passwd=None, db='mysql')
    conn = mykaze.connect(host='127.0.0.1', port=3306, user='root', passwd='root', db='mysql')

    cur = conn.cursor()

    cur.execute("SELECT Host,User FROM user")

    # r = cur.fetchall()
    # print r
    # ...or...
    for r in cur:
       print(r)

    cur.close()
    conn.close()

io_loop = tornado.ioloop.IOLoop.instance()
io_loop.add_callback(sample)
io_loop.start()

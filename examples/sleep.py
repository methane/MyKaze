#!/usr/bin/env python
# coding: utf-8
from __future__ import print_function

import tornado.ioloop
import greenlet
from functools import wraps
import mykaze
from mykaze.util import wrap_green


@wrap_green
def sample(n):
    con = mykaze.connect('localhost', 'root', 'root')
    print('connected')
    cur = con.cursor()
    for i in range(100):
        cur.execute("SELECT SLEEP(1)")
        print(n, i, cur.fetchone()[0])

io_loop = tornado.ioloop.IOLoop.instance()
for n in range(20):
    io_loop.add_callback(sample, n)
io_loop.start()

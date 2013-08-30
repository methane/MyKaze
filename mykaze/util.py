import struct
import greenlet
from functools import wraps

def byte2int(b):
    if isinstance(b, int):
        return b
    else:
        return struct.unpack("!B", b)[0]

def int2byte(i):
    return struct.pack("!B", i)

def join_bytes(bs):
    if len(bs) == 0:
        return ""
    else:
        rv = bs[0]
        for b in bs[1:]:
            rv += b
        return rv

def wrap_green(func):
    @wraps(func)
    def meth(*args, **kw):
        g = greenlet.greenlet(func)
        return g.switch(*args, **kw)
    return meth

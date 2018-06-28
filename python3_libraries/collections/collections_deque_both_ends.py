#!/usr/bin/env python3
# encoding: utf-8
#
# Copyright (c) 2008 Doug Hellmann All rights reserved.
#
"""Burning a candle at both ends.
"""

#end_pymotw_header
import collections
import threading
import time

candle = collections.deque(range(5))


def burn(direction, nextSource):
    while True:
        try:
            next = nextSource()
        except IndexError:
            break
        else:
            print('{:>8}: {}'.format(direction, next))
            time.sleep(0.1)
    print('{:>8} done'.format(direction))
    return


left = threading.Thread(target=burn,
                        args=('Left', candle.popleft))
right = threading.Thread(target=burn,
                         args=('Right', candle.pop))

left.start()
right.start()

left.join()
right.join()

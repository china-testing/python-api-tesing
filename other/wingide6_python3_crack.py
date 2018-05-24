#!/usr/bin/python
# -*- coding: utf-8 -*-
# Author:    xurongzhong#126.com wechat:pythontesting qq:37391319
# CreateDate: 2018-1-12
# From http://blog.csdn.net/q15920659569/article/details/54577098
'''
先执行本程序，生成序列号，然后从wingide中复制请求码，生成激活码。
'''

import string
import random
import hashlib

BASE16 = '0123456789ABCDEF'
BASE30 = '123456789ABCDEFGHJKLMNPQRTVWXY'


def randomstring(size=20, chars=string.ascii_uppercase + string.digits):
    return ''.join((random.choice(chars) for _ in range(size)))


def BaseConvert(number, fromdigits, todigits, ignore_negative=True):
    if not ignore_negative and str(number)[0] == '-':
        number = str(number)[1:]
        neg = 1
    else:
        neg = 0
    x = 0
    for digit in str(number):
        x = x * len(fromdigits) + fromdigits.index(digit)

    res = ''
    while x > 0:
        digit = x % len(todigits)
        res = todigits[digit] + res
        x //= len(todigits)

    if neg:
        res = '-' + res
    return res


def AddHyphens(code):
    return code[:5] + '-' + code[5:10] + '-' + code[10:15] + '-' + code[15:]


def SHAToBase30(digest):
    tdigest = ''.join([c for i, c in enumerate(digest) if i // 2 * 2 == i])
    result = BaseConvert(tdigest, BASE16, BASE30)
    while len(result) < 17:
        result = '1' + result
    return result


def loop(ecx, lichash):
    part = 0
    for c in lichash:
        part = ecx * part + ord(c) & 1048575
    return part


rng = AddHyphens('CN' + randomstring(18, '123456789ABCDEFGHJKLMNPQRTVWXY'))
print('License id: {}'.format(rng))
act30 = input('Enter request code:')
lichash = act30
hasher = hashlib.sha1()
act30 = act30.encode()
hasher.update(act30)
rng = rng.encode()
hasher.update(rng)
lichash = AddHyphens(lichash[:3] + SHAToBase30(hasher.hexdigest().upper()))
part5 = format(loop(23, lichash), '05x') + format(loop(161, lichash), '05x') + \
    format(loop(47, lichash), '05x') + format(loop(9, lichash), '05x')
part5 = BaseConvert(part5.upper(), BASE16, BASE30)

while len(part5) < 17:
    part5 = '1' + part5

part5 = 'AXX' + part5
print('Activation code: {}'.format(AddHyphens(part5)))

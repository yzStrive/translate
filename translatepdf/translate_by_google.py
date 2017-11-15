#coding:utf-8
import requests
import tk
import os
import sys


def translate_google(cont):
    googleUrl = 'https://translate.google.cn/translate_a/single'
    sl = 'en'
    tl = 'zh-CN'
    hl = 'zh-CN'
    q = cont
    _tk = tk.create_tk(q)
    payload = {
        'q': q,
        "client": 't',
        "sl": sl,
        "tl": tl,
        "hl": hl,
        "ie": 'UTF-8',
        "oe": 'UTF-8',
        "source": 'bh',
        "ssel": 0,
        "tsel": 0,
        "kc": 1,
        "tk": _tk,
        "dt": ['at', 'bd', 'ex', 'ld', 'md', 'qca', 'rw', 'rm', 'ss', 't']
    }
    r = requests.get(googleUrl, params=payload)
    return r.json()


if __name__ == '__main__':
    print(translate_google('test google translate api'))

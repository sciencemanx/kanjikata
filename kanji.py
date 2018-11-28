#! /bin/env python3

from crabigator.wanikani import WaniKani
import requests as r

import os
from functools import reduce

key = 'XXXX'
url_fmt = 'https://kanji.sljfaq.org/kanjivg/memory.cgi?c={}'

wk = WaniKani(key)

def mk_url(kanji):
	code = hex(ord(kanji))[2:]

	return url_fmt.format(code)

def download_stroke_diagram(kanji):
	url = mk_url(kanji)
	res = r.get(url).content
	while b"HTML" in res:
		res = r.get(url).content
	return res

def do(level, folder="./"):
	path = os.path.join(folder, str(level))
	path = os.path.expanduser(path)

	if os.path.exists(path):
		if not os.path.isdir(path):
			return
	else:
		os.mkdir(path)

	ks = wk.get_kanji(levels=[level])

	for i, k in enumerate(ks):
		diagram = download_stroke_diagram(k.character)
		meanings = ', '.join(k.meaning)
		k_path = os.path.join(path, "{}:{} - {}.png".format(level, i+1, meanings))
		with open(k_path, "wb") as f:
			f.write(diagram)
		print("{} - {}".format(k.character, meanings))

if __name__ == '__main__':
	for i in range(17, 60):
		print("---------   {}   -----------".format(i + 1))
		do(i + 1, folder='~/kanji/')

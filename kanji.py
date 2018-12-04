from crabigator.wanikani import WaniKani
import requests as r

import os
from functools import reduce

DIAGRAM_URL_FMT = 'https://kanji.sljfaq.org/kanjivg/memory.cgi?c={}'

def mk_url(kanji):
  code = hex(ord(kanji))[2:]

  return DIAGRAM_URL_FMT.format(code)

def download_stroke_diagram(kanji):
  url = mk_url(kanji)
  res = r.get(url).content
  while b"HTML" in res:
    res = r.get(url).content
  return res

def get_kanjis(wk_key, wk_level):
  wk = WaniKani(wk_key)
  kanjis = wk.get_kanji(levels=[wk_level])

  def process_kanji(i, kanji):
    diagram = download_stroke_diagram(kanji.character)
    meanings = ', '.join(kanji.meaning)

    kanji_path = '{}-{}-{}.png'.format(wk_level, i, meanings)
    with open(kanji_path, "wb") as f:
      f.write(diagram)

    return meanings, kanji_path

  processed_kanji = [process_kanji(i, k) for i, k in enumerate(kanjis)]

  return processed_kanji

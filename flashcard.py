import os

import genanki
from progressbar import progressbar

import kanji


# don't change this unless you know what you're doing
MODEL_ID = 1129694196
DECK_ID_BASE = 1866861533

FIELDS = [
  {'name': 'level'},
  {'name': 'meaning'},
  {'name': 'image'},
]

MEANING_DIAGRAM_TEMPLATE = {
  'name': 'meaning -> stroke diagram',
  'qfmt': '{{meaning}} (from level {{level}})',
  'afmt': '{{FrontSide}}<hr id="answer">{{image}}',
}

KANJI_MODEL = genanki.Model(
  MODEL_ID,
  'Kanji Stroke Diagram Model',
  fields=FIELDS,
  templates=[
    MEANING_DIAGRAM_TEMPLATE,
  ]
)


def make_deck(wk_level, kanjis):
  deck_id = DECK_ID_BASE + wk_level
  deck_name = 'Kanji Stroke Diagrams::Level {}'.format(wk_level)

  deck = genanki.Deck(deck_id, deck_name)

  for meaning, image in kanjis:
    image_tag = '<img src="{}">'.format(image)
    note = genanki.Note(
      model=KANJI_MODEL,
      fields=[str(wk_level), meaning, image_tag]
    )
    deck.add_note(note)

  return deck


def make_flashcards(wk_key, wk_levels):
  decks = []
  images = []

  for wk_level in progressbar(wk_levels):
    kanjis = kanji.get_kanjis(wk_key, wk_level)
    deck = make_deck(wk_level, kanjis)

    images += [image for _, image in kanjis]
    decks.append(deck)

  package = genanki.Package(decks)
  package.media_files = images

  tmp_pkg_path = os.path.join(os.getcwd(), 'tmp.apkg')

  package.write_to_file(tmp_pkg_path)

  return tmp_pkg_path

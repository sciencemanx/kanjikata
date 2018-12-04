# kanjikata
Create Anki flashcards for kanji stroke order diagrams. Creating the flashcards requires a WaniKani V1 API key from an active WaniKani account. These flashcards will eventually be available on https://ankiweb.net/shared/decks/.

## Installation

- `git clone https://github.com/sciencemanx/kanjikata.git`
- `cd kanjikata`
- `pip3 install git+https://github.com/sciencemanx/genanki.git@class-reorg`
- `pip3 install progressbar2`

### Note
The special genanki install is temporary until my patch is accepted by the
original author. My patch is needed as the original deck does not properly
support multi-deck anki packages.

## Usage

`python3 kanjikata.py -k <wanikani api key> -l <level> ...`

For example, the following command would download flashcards for levels 1, 2, 3,
and 60 using the V1 WaniKani API key "abcd1234".

`python3 kanjikata.py -k abdc1234 -l 1 2 3 60`

## Credits
Thanks to:
- wanikani.com
- kanji.sljfaq.org

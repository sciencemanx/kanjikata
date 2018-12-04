#! /bin/env python3

import argparse
import os
import shutil
import tempfile
import time

import flashcard


ALL_LEVELS = [i + 1 for i in range(60)]


def default(x, y):
  return x if x is not None else y


def main(wk_key, wk_levels):
  wk_levels = default(wk_levels, ALL_LEVELS)
  assert wk_levels != []
  assert all(1 <= i and i <= 60 for i in wk_levels)

  current_path = os.getcwd()

  with tempfile.TemporaryDirectory() as tmpdir:
    os.chdir(tmpdir)

    now = int(time.time())
    package_file = 'kanjikata-{}.apkg'.format(now)
    package_path = os.path.join(current_path, package_file)

    tmp_pkg_path = flashcard.make_flashcards(wk_key, wk_levels)

    os.chdir(current_path)

    shutil.copyfile(tmp_pkg_path, package_path)

    print('wrote package file to {}'.format(package_path))


if __name__ == '__main__':
  parser = argparse.ArgumentParser()
  parser.add_argument('-k', '--key')
  parser.add_argument('-l', '--levels', nargs='+', type=int)

  args = parser.parse_args()

  main(args.key, args.levels)

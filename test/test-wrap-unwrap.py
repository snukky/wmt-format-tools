#!/usr/bin/env python

import sys
from pathlib import Path

import wmtformat

def main():
  sampledir = Path(sys.argv[0]).parent / "sample-data"

  wrapped = wmtformat.wrap((sampledir / "sample-src.xml").as_posix(), sampledir / "sample-hyp.ha", "ha", name="test-team")
  with open("out.xml", "w") as ofh:
    print(wrapped, file=ofh, end="")

  src_lang, src_lines, ref_lang, ref_lines, hyp_lang, hyp_lines = \
     wmtformat.unwrap((sampledir / "sample-src-ref.xml").as_posix(), missing_message = "NO TRANSLATION AVAILABLE")

  with open("out." + src_lang, "w") as ofh:
    for line in src_lines:
      print(line, file=ofh)

  with open("out." + ref_lang, "w") as ofh:
    for line in ref_lines['A']:
      print(line, file=ofh)



if __name__ == "__main__":
  main()

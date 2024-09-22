# This is a scratch file for testing and playing with the D&D references.

from dnd_references import *

for itype in ITEM_TYPES:
  print(f"{itype}: {len([i for i in ITEMS if i.type == itype])}")


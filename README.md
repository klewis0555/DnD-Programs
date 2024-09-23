# D&D Programs
This repo was written with python version 3.11.2. Any of the programs can be run with

`python3 <program_name>`

There are currently 4 classes in dnd_references.py:
- `Items` - magic items
  - `name` - name of the item
  - `price` - base price of the item
  - `type` - type of the item, one of the following strings:
    - Wondrous Item, Armor, Class Item, Clothing, Consumable, Jewelry, Spell Scroll, Tattoo, Wand/Staff, Weapon
  - `attunement` - boolean of whether the item requires attunement or not
  - `rarity` - The item's rarity from "Common" to "Legendary"
  - `options` (optional param) - if the item has options, like armor type, weapon type, or spell,
- `Weapon` - weapons
  - `name` - name of the weapon
  - `price` - base price of the weapon
  - `prof` - string to represent "Simple" or "Martial"
  - `type` - category of the weapon: swords, axes, polearms, etc
  - `dtype` - damage type of the weapon
  - `props` - weapon properties
- `Armor` - armor
  - `name` - name of the armor
  - `price` - base price of the armor
  - `type` - light, heavy or medium
- `Spell` - spells
  - `name` - name of the spell
  - `level` - level of the spell
  - `school` - school of the spell

Currently, the references module is seeded with every all base material from 5e and 5.5e, as well as many from the expanded sources like Xanathar's Guide to Everything, Tasha's Cauldron of Everything, Fizban's Treasury of Dragons, Bigby Presents: Glory to the Giants, Explorer's Guide to Wildemount, The Book of Many Things, and a few homebrew entries.

Base prices are included for every magic item. These are merely a guideline for the shop, and are completely subjective to my own opinions. These prices were decided over many late nights and spans of time in between, so consistency and accuracy are not guaranteed. Prices in the actual shop are randomized with a window of 25% on either side.

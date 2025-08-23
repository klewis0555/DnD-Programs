import sys
from random import randint, random, randrange
from prettytable import PrettyTable
from dnd_references import *

def check_input(input: str, start: int, max: int):
  try:
    number = int(input)
    if number < start or number > max:
      raise ValueError
    return(number)
  except ValueError:
    print(f"Invalid input, please enter a number between {start} and {max}.")

def choose_option(item):
  if not item.options:
    return None
  return item.options[randrange(len(item.options))]

def generate_name(item, option = None):
  if not option:
    return item.name
  return item.name.replace("___", option.name)

def generate_price(item, option = None):
  price = randint(int(item.price*0.75), int(item.price*1.25)) # Random price
  if option and (item.type == "Armor" or item.type == "Weapon"):
    price += option.price # update price for armor and weapons
    if item.options == WEAPONS and option.type == "Ranged":
      price *= 1.25 # ranged weapons get a 25% increase
      if option.name == "Pistol" or option.name == "Musket":
        price *= 1.20 # firearms price increase to 50% increase
  return int(price)

def create_entry(item, name: str, price: int, shop_size: int):
  price_string = f"{price} GP"
  stock = randint(1, (RARITIES.index(item.rarity) + 1)) + shop_size if item.type == "Consumable" else "-"
  attunement = item.attunement
  category = item.type
  rarity = item.rarity
  return [name, price_string, stock, attunement, category, rarity]

def create_rows(count: int, items: list, item_set: set, shop_size: int):
  rows = []
  for i in range(count): # populate items
    row_item = items[randrange(len(items))] # choose item
    option = choose_option(row_item)
    name = generate_name(row_item, option)
    price = generate_price(row_item, option)
    if name not in item_set: # don't add duplicate items
      item_set.add(name)
      rows.append(create_entry(row_item, name, price, shop_size))
  return rows

def add_rows_to_shop(rows: list, shop: PrettyTable):
  rows.sort()
  for x in range(len(rows)):
    set_divider = True if x == (len(rows) - 1) else False
    shop.add_row(rows[x], divider=set_divider)

def generate_shop(shop_size: int, shop_type: int):
  shop = PrettyTable()
  shop_items = set()
  shop.field_names = ["Name", "Price", "Stock", "Attunement", "Category", "Rarity"]

  # build counts for shop size
  common_count = 0
  uncommon_count = 0
  rare_count = 0
  very_rare_count = 0
  legendary_count = 0
  match shop_size:
    case 1: # extra small
      common_count = randint(4,8)
      uncommon_count = randint(1,4)
      rare_count = int(random() <= 0.3333)
      very_rare_count = 0
      legendary_count = 0
    case 2: # small
      common_count = randint(5,10)
      uncommon_count = randint(4,8)
      rare_count = randint(0,3)
      very_rare_count = int(random() <= 0.3333)
      legendary_count = 0
    case 3: # medium
      common_count = randint(6,12)
      uncommon_count = randint(6,12)
      rare_count = randint(2,8)
      very_rare_count = randint(0,2)
      legendary_count = 0
    case 4: # large
      common_count = randint(8,16)
      uncommon_count = randint(10,15)
      rare_count = randint(8,14)
      very_rare_count = randint(2,6)
      legendary_count = int(random() <= 0.3333)
    case 5: # extra large
      common_count = randint(10,20)
      uncommon_count = randint(10,15)
      rare_count = randint(12,20)
      very_rare_count = randint(6,12)
      legendary_count = randint(1,5)

  # filter items based on shop type
  items = [i for i in ITEMS if i.type == ITEM_TYPES[shop_type]] if shop_type else ITEMS
  common_items = [i for i in items if i.rarity == "Common"]
  uncommon_items = [i for i in items if i.rarity == "Uncommon"]
  rare_items = [i for i in items if i.rarity == "Rare"]
  very_rare_items = [i for i in items if i.rarity == "Very Rare"]
  legendary_items = [i for i in items if i.rarity == "Legendary"]

  common_rows = create_rows(common_count, common_items, shop_items, shop_size)
  add_rows_to_shop(common_rows, shop)

  uncommon_rows = create_rows(uncommon_count, uncommon_items, shop_items, shop_size)
  add_rows_to_shop(uncommon_rows, shop)

  rare_rows = create_rows(rare_count, rare_items, shop_items, shop_size)
  add_rows_to_shop(rare_rows, shop)

  very_rare_rows = create_rows(very_rare_count, very_rare_items, shop_items, shop_size)
  add_rows_to_shop(very_rare_rows, shop)

  legendary_rows = create_rows(legendary_count, legendary_items, shop_items, shop_size)
  add_rows_to_shop(legendary_rows, shop)

  return shop

# generate the prompt for the user based on provided options (starting at 1)
def generate_input_string(start_string: str, options: list):
  input_string = start_string
  for i in range(len(options)):
    input_string += f"{i+1} for {options[i]}, "
  input_string = input_string[:-2] + ": "
  return input_string

def run_shop():
  if __name__ == "__main__":
    if len(sys.argv) > 1:
      shop_size_input = sys.argv[1]
    else:
      shop_size_input = input(generate_input_string("Shop Size? ", ["Extra Small", "Small", "Medium", "Large", "Extra Large"]))
    shop_size = check_input(shop_size_input, 1, 5)
    if type(shop_size) != int:
      return
    
    if len(sys.argv) > 2:
      shop_type_input = sys.argv[2]
    else:
      shop_type_input = input(generate_input_string("Shop Type? 0 for General, ", ITEM_TYPES[1:]))
    shop_type = check_input(shop_type_input, 0, len(ITEM_TYPES) - 1)
    if type(shop_type) != int:
      return

    shop = generate_shop(shop_size, shop_type)
    print(shop)

run_shop()

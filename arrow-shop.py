import sys
from random import randint, randrange
from prettytable import PrettyTable
from dnd_references import *

def generate_shop(input):
  shop = PrettyTable()
  shop.field_names = ['Name', 'Stock', 'Price Per', 'Price Per 20', 'Rarity']

  # loop through rarities
  for rarity, values in ARROWS.items():
    inventory = set()
    weight = values['weight']
    # generate options for arrows for current rarity
    for x in range((input * weight) - randint(0,2)):
      inventory.add(values['types'][randint(0,len(values['types']) - 1)])
    # if nothing in set, skip this rarity
    if len(inventory) > 0:
      # generate table row 
      for item in list(inventory):
        set_divider = (item == list(inventory)[-1]) and rarity != 'Very Rare'
        # generate inventory stock amount
        stock = randint((weight * input), (5 * weight * input))

        # generate price
        price_range_multiplier = [20, 10, 5, 2, 1]
        price = randint((4 * price_range_multiplier[weight - 1]), (6 * price_range_multiplier[weight - 1]))

        # add row to shop table
        shop.add_row([item, stock, f"{price} sp", f"{price * 2} gp", rarity], divider=set_divider)
  
  slaying_inventory = set()
  # for x in range(1, input):
  for x in range(0, randrange(0, input)):
    slaying_inventory.add('Arrow of _ Slaying'.replace('_', SLAYING[randint(0,len(SLAYING)-1)]))
  for item in list(slaying_inventory):
    shop.add_row([item, randint(1,input), f"{randint(6,20)*5} gp", '---', 'Very Rare'])
  return shop

if __name__ == "__main__":
  try:
    if len(sys.argv) > 1:
      user_input = sys.argv[1]
    else:
      user_input = input("Shop Size? 1 for Small, 2 for Medium, 3 for Large, 4 for Extra Large.\n")
    number = int(user_input)
    if number < 1 or number > 4:
      raise ValueError
    shop = generate_shop(number)
    print(shop)
  except ValueError:
    print("Invalid input, please enter a number between 1 and 4.")



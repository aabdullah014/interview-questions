from types import List
from .espresso_drink import EspressoDrink

class EspressoMachine:
  def __init__(self, drink_list: dict = None):
    pass

  def get_drink_params(self, drink_name: str) -> List[float, float, float]:
  # Assume only ratios that exist are coffee_ratio, milk_ratio, water_ratio, and espresso_ratio
  # Assume that for drinks that have single and double options, we will calculate amount of ingredients for a single shot
  # Will use coffee_in_espresso variable from above where needed to save some time
    coffee_ratio = 0
    water_ratio = 0
    milk_ratio = 0
    espresso_ratio = 0
    mL = 0
    for ing in drink_name:
      if ing == 'coffee_ratio': 
        coffee_ratio = self.drink_list[drink_name][ing]
      elif ing == 'water_ratio':
        water_ratio = self.drink_list[drink_name][ing]
      elif ing == 'milk_ratio':
        milk_ratio = self.drink_list[drink_name][ing]
      elif ing == 'espresso_ratio':
        espresso_ratio = self.drink_list[drink_name][ing]
        coffee_ratio = espresso_ratio
        water_ratio = 2*espresso_ratio
      else:
        # If there is an option for a single shot, use it
        if self.drink_list[drink_name][ing]['single']:
          mL = self.drink_list[drink_name][ing]['single']
        else:
        # Otherwise, set mL variable to mL quantity, which should be ing at this point
          mL = ing
    
      total_ingredient_parts = coffee_ratio + milk_ratio + water_ratio + espresso_ratio
      coffee_amount = (coffee_ratio/total_ingredient_parts)*mL*0.54
      water_amount = (water_ratio/total_ingredient_parts)*mL
      milk_amount = (milk_ratio/total_ingredient_parts)*mL

    drink_params = [coffee_amount, water_amount, milk_amount]

    return drink_params

  def add_drink_to_menu(self, drink_name: str):
    if drink_name in self.drink_list:
      print('This drink recipe is already known!')
    else:
      self.drink_list.append(drink_name)

  def time_to_make_drink(self, drink_name: str):
    # This is an iterative implementation. A more efficient implementation would be to treat the dictionary like a Tree.
    time = 0
    ingredient_count = 0
    mL = 0
    for ing in drink_name:
      if ing == 'coffee_ratio' or 'water_ratio' or 'milk_ratio': 
        ingredient_count += 1
      # This next step assumes the existence of espresso_ratio means there is no water_ratio or coffee_ratio in drink_name, or else we would be double counting
      elif ing == 'espresso_ratio':
        ingredient_count += 2
      else:
        # If there is an option for a single shot, use it
        if self.drink_list[drink_name][ing]['single']:
          mL = self.drink_list[drink_name][ing]['single']
        elif self.drink_list[drink_name][ing]['double']:
          mL = self.drink_list[drink_name][ing]['double']
        # Otherwise, set mL variable to mL quantity, which should be ing at this point
        else:
          mL = ing
    time = (ingredient_count*5) + (mL/8)
    return time
import json
from controllers.espresso_machine import EspressoMachine
from tabulate import tabulate

if __name__ == "__main__":
  with open('data/drinks.json', 'r') as drink_file: 
    coffee_recipes = json.loads(drink_file.read())
  print(coffee_recipes)

  # TODO: 1a - display amount of coffee in a single shot of espresso
  #0.54g coffee = 1mL liquid
  #single shot = 30mL, using ratio, there are 10mL of coffee, so there are 0.54(10)= 5.4g coffee

  #obtain ratios of coffee and water from coffee_recipes
  espresso_coffee_ratio = coffee_recipes['espresso']['coffee_ratio']
  espresso_water_ratio = coffee_recipes['espresso']['water_ratio']
  espresso_total_ingredient_parts = espresso_coffee_ratio + espresso_water_ratio

  #obtain amount of mL in a single shot
  mL_single = coffee_recipes['espresso']['mL']['single']

  #find amount of coffee using ratio of coffee, multiplying by single shot to get liquid amount, then *0.54 to get grams of coffee
  coffee_in_espresso = (espresso_coffee_ratio/espresso_total_ingredient_parts)*mL_single*0.54
  print(f"The amount of coffee in a single shot of espresso is: {coffee_in_espresso}")

  # TODO: 1b - display amount of water in a flat white
  # Water amount not explicitly stated, but we can work backwards using the espresso_ratio
  # Each part espresso adds 1 part coffee and 2 parts water
  flat_white_coffee_ratio = coffee_recipes['espresso']['coffee_ratio']
  flat_white_water_ratio = 2*coffee_recipes['espresso']['water_ratio']
  flat_white_total_ingredient_parts = flat_white_coffee_ratio + flat_white_water_ratio +coffee_recipes['flat_white']['milk_ratio']

  water_in_flat_white = (flat_white_water_ratio/flat_white_total_ingredient_parts)*165
  print(f"The amount of water in a flat white is: {water_in_flat_white}")  

  # TODO: 1c (i) - print a table showing coffee / water / milk for each drink
  # Will use tabulate to print out a table
  # Initalize drink_list to print, with list containing len(coffee_recipes)-1 lists that will contain the three desired values plus the name
  espresso_machine = EspressoMachine(coffee_recipes)
  for drink in coffee_recipes:
    print(f"{drink}: {espresso_machine.get_drink_params(drink)}")

  # TODO: 1c (ii) - add drink to menu
  espresso_machine.add_drink_to_menu('espresso')
  # TODO: 1c (iii) - implement time component to create each drink
  espresso_machine.time_to_make_drink('espresso')
  

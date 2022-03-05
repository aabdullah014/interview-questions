import time
from python.problems.p1 import coffee_recipes
from python.problems.p2_task import enjoyDrink
from python.problems.controllers.espresso_machine import EspressoMachine


if __name__ == "__main__":
  espresso_machine = EspressoMachine(coffee_recipes)

  queue_p3 = []
  # changed parameter from one drink to the list of drinks
  def createDrinkNotBroken(drink_list: str):
    # If queue is empty, print this
    if not queue_p3.pop(0):
      print('There are no current orders!')
    # iterate through drinks in the queue and sleep before "making" each one
    for drink in drink_list:
      time.sleep(espresso_machine.time_to_make_drink(drink))
      queue_p3.pop(0)
      enjoyDrink(drink)
  
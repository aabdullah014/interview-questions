import time
from python.problems.p1 import coffee_recipes
from python.problems.p2_task import enjoyDrink
from python.problems.controllers.espresso_machine_broken import EspressoMachineBroken


if __name__ == "__main__":
  # TODO: 2a - create Espresso machine object, queuing up espresso orders as delivered by p2_task
  broken_espresso_machine = EspressoMachineBroken(coffee_recipes)

  queue_p2 = []
  # Changed parameter from one drink to the list of drinks
  def createDrink(drink_list: str):
    # If queue is empty, print this
    if not queue_p2.pop(0):
      print('There are no current orders!')

    # iterate through drinks in the queue and sleep before "making" each one
    for drink in drink_list:
      time.sleep(broken_espresso_machine.time_to_make_drink(drink))
      queue_p2.pop(0)
      enjoyDrink(drink)
  
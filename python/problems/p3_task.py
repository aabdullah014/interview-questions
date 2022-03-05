from venv import create
from python.problems.p1 import coffee_recipes
from python.problems.p2_worker import queue_p2, createDrink
from python.problems.p3_worker import queue_p3, createDrinkNotBroken
from python.problems.controllers.espresso_machine import time_to_make_drink
if __name__ == "__main__":

  def requestDrink(drink_name):
    # If the drink doesn't exist, print out that it is not available
    if drink_name not in coffee_recipes:
      print('Sorry this drink is not available')
      pass
    else:
      # This object will only be used to run the time_to_make_drink method
      espresso_machine = espresso_machine(coffee_recipes)

      # Compare the items between the two queues and see which queue will take longer to iterate through
      q2_time = 0
      for drink2 in queue_p2:
        q2_time += espresso_machine.time_to_make_drink(drink2)
        
      q3_time = 0
      for drink3 in queue_p3:
        q3_time += espresso_machine.time_to_make_drink(drink3)

      # Add the new requested item to the shorter queue
      if q3_time <= q2_time:
        queue_p3.append(drink_name)
        createDrinkNotBroken(queue_p3)
      else:
        queue_p2.append(drink_name)
        createDrink(queue_p2)

  def enjoyDrink(drink_name):
    print(f"Ahh, that's a tasty {drink_name}")
  pass
  
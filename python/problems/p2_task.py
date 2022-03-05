from venv import create
from python.problems.p1 import coffee_recipes
from python.problems.p2_worker import queue_p2, createDrink
if __name__ == "__main__":
  # TODO: 2a - specify different coffee drinks and send to p2_worker to create

  def requestDrink(drink_name):
    if drink_name not in coffee_recipes:
      print('Sorry this drink is not available')
      pass
    else:
      queue_p2.append(drink_name)
      createDrink(queue_p2)

  def enjoyDrink(drink_name):
    print(f"Ahh, that's a tasty {drink_name}")
  pass
  
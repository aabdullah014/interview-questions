Edited ristretto drink in drinks.json file to say “water_ratio” and “coffee_ratio” instead of “water” and “coffee”

1. - a. Assume that “coffee_ratio: 1” and “milk_ratio: 2” implies for every one part coffee, there are two parts milk.
   - b. Water is not explicitly stated in flat_white, but espresso ratio is, so work backwards


1. - c i. If drink does not exist, print out some error message, otherwise iterate through the list of drinks and print out their coffee, water, and milk values using the get_drink_params method
   - c ii. If drink is known, prints out something, if not known, add it to coffee_recipes
   - c iii. If time permitted, would try to implement a BFS search instead of the iterative approach used. Can imagine traversing the dictionary as traversing a tree, with going from “espresso_ratio” to the “espresso” drink to gather its parameters. Iterative approach also assumes the only ratios that exist are water_ratio, milk_ratio, coffee_ratio, and espresso_ratio


2. - a. P2_worker: takes drink orders in form of a queue, sleeps thread for duration of creation time specified early. can return [None, None, None], so must be able to handle this scenario as well as a successful output. My implementation uses the queue as a parameter in the createDrink function. This made it easier to iterate through the order queue.
   - b. P2_task: if requested drink not on the menu, print out some error message, otherwise add the drink to the queue for P2_worker to make
3. An effective method would be to implement a load-balancing algorithm that allocates orders to the machines based on the time it will take their queue to finish, e.g. it would be inefficient to give an order to machine 1 when it’s order queue is already twice as long as machine 2. In the case there are no order queues for any machine, it will allocate to p3. 


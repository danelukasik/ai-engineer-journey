#  🍕 Pizza Builder — Challenge Steps
#
# 1. Define a Pizza class that stores:
#    - size, crust type, and a list of toppings
# 2. Add a method to add a new topping
# 3. Add a method to remove a topping if it exists
# 4. Add a method to print pizza details:
#    - size, crust, and all toppings (or “No toppings yet!”)
# 5. Create a pizza object, customize it, and print the summary

class Pizza:
    def __init__(self, size, crust_type, toppings=None):
        self.size = size
        self.crust_type = crust_type
        if toppings is None:
            self.toppings = []
        else:
            self.toppings = list(toppings)
    
    def add_topping(self):
        while True:
            topping = input(f'Write a topping to add. Enter \'done\' to move on. Your current toppings include: {", ".join(self.toppings)}').lower()
            if topping == 'done':
                break
            else:
                self.toppings.append(topping)
                continue
    
    def remove_topping(self):
        while True:
            topping = input(f'Write a topping to remove. Enter \'done\' to move on. Your current toppings include: {", ".join(self.toppings)}').lower()
            if topping == 'done':
                break
            else:
                try:
                    self.toppings.remove(topping)
                except ValueError:
                    print('Topping not on pizza.')
                except:
                    print('There\'s been an error')
                continue
                
    def pizza_deets(self):
        print(f'---Your Pizza---')
        print(f'Size: {self.size}')
        print(f'Crust Type: {self.crust_type}')
        if len(self.toppings) == 0:
            print('No toppings yet!')
        else:
            print(f'Topping(s): {", ".join(self.toppings)}')
            
my_pizza = Pizza('12in','Detroit Style')
my_pizza.add_topping()
my_pizza.remove_topping()
my_pizza.pizza_deets()
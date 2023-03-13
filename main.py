import csv
import datetime 

with open("Menu.txt", "w") as menu_file:
    menu_file.write("* Please select a Pizza base:\n1: Classic\n2: Margherita\n")
    menu_file.write("3: TurkishPizza\n4: Dominos Pizza\n* and your choice of sauce:\n")
    menu_file.write("11: Olives\n12: Mushrooms\n13: Goat Cheese\n14: Meat\n")
    menu_file.write("15: Onion\n16: Corn\n* Thank you!")

class Pizza:
    def __init__(self, description, cost):
       self.description = description
       self.cost = cost
    
    def get_description(self):
       return self.description
    
    def get_cost(self):
        return self.cost
        
class Classic(Pizza):
    def __init__(self):
        super().__init__("Classic Pizza", 10)

class Margherita(Pizza):
    def __init__(self):
        super().__init__("Margherita Pizza", 11)

class Turkish(Pizza):
    def __init__(self):
        super().__init__("Turkish Pizza", 12)

class Dominos(Pizza):
    def __init__(self):
        super().__init__("Dominos Pizza", 13)

class Decorator(Pizza): 
    def __init__(self, component):
        self.component = component
        self.description = ""
        self.cost = 0.0
        
    def get_cost(self):
        return self.component.get_cost() + self.cost

    def get_description(self):
        return self.component.get_description() + ' ' + self.description
    
class Olives(Decorator):
    def __init__(self, component):
        super().__init__(component)
        self.description = "Olives" 
        self.cost = 2.0

class Mushrooms(Decorator):
    def __init__(self, component):
        super().__init__(component)
        self.description = "Mushrooms" 
        self.cost = 3.0
        
class GoatCheese(Decorator):
    def __init__(self, component):
        super().__init__(component)
        self.description = "Goat Cheese" 
        self.cost = 5.0
        
class Meat(Decorator):
    def __init__(self, component):
        super().__init__(component)
        self.description = "Meat" 
        self.cost = 7.0
        
class Onion(Decorator):
    def __init__(self, component):
        super().__init__(component)
        self.description = "Onion" 
        self.cost = 1.5
        
class Corn(Decorator):
    def __init__(self, component):
        super().__init__(component)
        self.description = "Corn" 
        self.cost = 2.0

def main():

    with open('Menu.txt', 'r') as menu_file:
        print(menu_file.read())

    pizza_choice = input("Please choose a Pizza (1-4): ")
    if pizza_choice == "1":
        my_pizza = Classic()
    elif pizza_choice == "2":
        my_pizza = Margherita()
    elif pizza_choice == "3":
        my_pizza = Turkish()
    else:
        my_pizza = Dominos()
    
    sauce_choice = input("Please choose a sauce (11-16) or enter '0' to finish: ")
    sauces = []
    while sauce_choice != "0":
        if sauce_choice == "11":
            my_pizza = Olives(my_pizza)
        elif sauce_choice == "12":
            my_pizza = Mushrooms(my_pizza)
        elif sauce_choice == "13":  
            my_pizza = GoatCheese(my_pizza)
        elif sauce_choice == "14":
            my_pizza = Meat(my_pizza)
        elif sauce_choice == "15":
            my_pizza = Onion(my_pizza)
        elif sauce_choice == "16":
            my_pizza = Corn(my_pizza)
        else:
            print("Invalid choice. Please try again.")
        sauces.append(sauce_choice)
        sauce_choice = input("Please choose another sauce (11-16) or enter '0' to finish: ")    
    
    # Print out the final pizza order
    
    print("Your pizza with the following toppings will be ready shortly:")
    
    if my_pizza:
        print(my_pizza.get_description())
        print("Total cost: $", my_pizza.get_cost())
    else:
        print("No pizza has been ordered.")

    name = input("Please enter your name: ")
    id_number = input("Please enter your TC ID number: ")
    cc_number = input("Please enter your credit card number: ")
    cc_password = input("Please enter your credit card password: ")

    with open("Orders_Database.csv", "a", newline="") as orders_db:
        writer = csv.writer(orders_db)
        writer.writerow([name, id_number, cc_number, cc_password, 
                         datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), 
                         my_pizza.get_description(), my_pizza.get_cost()])

main()
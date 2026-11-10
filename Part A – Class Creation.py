print("---Start Here---")

##Part A: Class Creation
#(here create the main class ShoppingCart with self, customer name and items)

class ShoppingCart:       #Create a clas here
    def __init__(self, customer_name, items=None): #Constructor initialize
        self.customer_name = customer_name
        if items is None:  #If no items then empty list
            self.items = []
        else:
            self.items = items.copy()
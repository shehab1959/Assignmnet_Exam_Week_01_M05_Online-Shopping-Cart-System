##Part D: Operator Overloading---------------------------------------
#(here combine name and items)

    def __add__(self, other): #combine two cart
        name = self.customer_name + " & " + other.customer_name   #combine both customer names
        items = self.items + other.items   #Combine both item lists

        return ShoppingCart(name, items)  #Return a new ShoppingCart object
#Final Assignment Solve


print("---Start Here--\n")
print("Online Shopping Cart System:\n")


##Part A: Class Creation
#(here create the main class ShoppingCart with self, customer name and items)

class ShoppingCart:       #Create a clas here
    def __init__(self, customer_name, items=None): #Constructor initialize
        self.customer_name = customer_name
        if items is None:  #If no items then empty list
            self.items = []
        else:
            self.items = items.copy()





##Part B: Core Methods---------------------------------------
#(here apply add item, remove item, total price, discount price inside the ShoppingCart class:)

    def add_item(self, price):  # 1.Add a new item
        if price > 0:  #use condition to check positive or not
            self.items.append(price)
            print(price, "added to the cart.")
        else:
            print("Price must be positive.")


    def remove_item(self, price): #2.Remove item from the cart
        if price in self.items: #Check price exists in the cart or not
            self.items.remove(price)
            print(price, "removed from the cart.")
        else:
            print(price, "not found in the cart.")


    def calculate_total(self):  #3.Calculate total price
        total = 0
        for price in self.items:
            total = total + price
        return total


    def apply_discount(self): #4.Apply discount
        total = self.calculate_total() #tootal calculate
        if total >= 3000: #apply discunt
            discount = total * 10 / 100
            final_amount = total - discount
        else:
            final_amount = total
        return final_amount






##Part C: Display and Utility Methods---------------------------------------
#(here disply customer name,items,total amount, amount after discount, total items)

    def display_cart(self):  # Display all information
        print("\n=====Shopping Cart =======")
        print("Customer Name:", self.customer_name) #customer name
        print("Items:", self.items) #items
        print("Total Amount:", self.calculate_total()) #amount
        print("Final Amount:", self.apply_discount()) #amount after discount
        print("Number of Items:", len(self.items)) #total item
        print("---------------------------")

    def clear_cart(self): #clear all item from cart
        self.items.clear()
        print(self.customer_name, "'s cart has been cleared.")





##Part D: Operator Overloading---------------------------------------
#(here combine name and items)

    def __add__(self, other): #combine two cart
        name = self.customer_name + " & " + other.customer_name   #combine both customer names
        items = self.items + other.items   #Combine both item lists

        return ShoppingCart(name, items)  #Return a new ShoppingCart object



# Part E: Object Usage and Output------------------------------
#(here first create two carta with basis of two different person and then combine and display those)

# Create two shopping cart objects
cart1 = ShoppingCart("Alice")
cart2 = ShoppingCart("Bob")

print("Alice's Cart Operations:")
cart1.add_item(1500) # Add items
cart1.add_item(2100) # Add items
cart1.add_item(700) # Add items
cart1.remove_item(700) # Remove one item


print("\nBob's Cart Operations:")
cart2.add_item(1200) # Add items
cart2.add_item(1800) # Add items
cart2.add_item(900) # Add items
cart2.remove_item(900) # Remove one


# Display Alices cart
print("\nAlice's Shopping Cart:")
cart1.display_cart()

# Display Bobs cart
print("\nBob's Shopping Cart:")
cart2.display_cart()


# Combine both
combined_cart = cart1 + cart2

# Display combined cart
print("\nCombined Shopping Cart:")
combined_cart.display_cart()


print("\n---End Here--")







"""
##Output##
---Start Here--

Online Shopping Cart System:

Alice's Cart Operations:
1500 added to the cart.
2100 added to the cart.
700 added to the cart.
700 removed from the cart.

Bob's Cart Operations:
1200 added to the cart.
1800 added to the cart.
900 added to the cart.
900 removed from the cart.

Alice's Shopping Cart:

=====Shopping Cart =======
Customer Name: Alice
Items: [1500, 2100]
Total Amount: 3600
Final Amount: 3240.0
Number of Items: 2
---------------------------

Bob's Shopping Cart:

=====Shopping Cart =======
Customer Name: Bob
Items: [1200, 1800]
Total Amount: 3000
Final Amount: 2700.0
Number of Items: 2
---------------------------

Combined Shopping Cart:

=====Shopping Cart =======
Customer Name: Alice & Bob
Items: [1500, 2100, 1200, 1800]
Total Amount: 6600
Final Amount: 5940.0
Number of Items: 4
---------------------------

---End Here--
"""
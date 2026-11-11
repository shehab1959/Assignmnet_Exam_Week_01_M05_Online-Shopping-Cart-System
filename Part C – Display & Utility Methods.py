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

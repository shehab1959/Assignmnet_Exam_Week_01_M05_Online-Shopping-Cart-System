#After Part-A:


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

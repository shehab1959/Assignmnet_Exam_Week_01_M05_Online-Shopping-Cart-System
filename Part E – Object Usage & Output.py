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
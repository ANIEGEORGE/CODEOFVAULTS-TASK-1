#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Grocery Store Inventory Management

# Define an initial inventory as a dictionary
inventory = {
    'Apple': {'quantity': 50, 'price': 10.0},
    'Banana': {'quantity': 30, 'price': 18.50},
    'Bread': {'quantity': 20, 'price': 15.00},
    'Milk': {'quantity': 10, 'price':20.00}
}


def view_inventory():
    print("\nCurrent Inventory:")
    for item, details in inventory.items():
        print(f"{item.capitalize()}: Quantity - {details['quantity']}, Price - Rs.{details['price']}")
    print("\n")
    
    
def add_item():
    item_name = input("Enter the name of the new item: ")
    quantity = int(input("Enter the quantity of the item: "))
    price = float(input("Enter the price of the item: "))
    
    # Check if the item already exists
    if item_name in inventory:
        print("Item already exists. Updating quantity.")
        inventory[item_name]['quantity'] += quantity
    else:
        inventory[item_name] = {'quantity': quantity, 'price': price}
        print("Item added to the inventory.")


def update_quantity():
    item_name = input("Enter the name of the item to update: ")
    
    # Check if the item exists
    if item_name in inventory:
        new_quantity = int(input("Enter the new quantity: "))
        inventory[item_name]['quantity'] = new_quantity
        print("Quantity updated.")
    else:
        print("Item not found in the inventory.")

def view_inventory():
    print("\nCurrent Inventory:")
    for item, details in inventory.items():
        print(f"{item.capitalize()}: Quantity - {details['quantity']}, Price - Rs.{details['price']}")
    print("\n")

def remove_item():
    item_name = input("Enter the name of the item to remove: ")
    
    # Check if the item exists
    if item_name in inventory:
        del inventory[item_name]
        print("Item removed from the inventory.")
    else:
        print("Item not found in the inventory.")

def main():
    while True:
        print("Grocery Store Inventory Management")
        print("1. View current inventory ")
        print("2. Add new item")
        print("3. Update item quantity")
        print("4. Remove item from inventory")
        print("5. Quit")
        
        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            view_inventory()
        elif choice == '2':
            add_item()
        elif choice == '3':
            update_quantity()
        elif choice == '4':
            remove_item()
        elif choice == '5':
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()


def manage_inventory(inventory, action, item=None, price=None):
    if action == "update":
        if item and price is not None:
            inventory[item] = price
            print(f"Updated {item} price to ${price}")
        else:
            print("Error: Item name and price required for update action.")
    elif action == "delete":
        if item and item in inventory:
            del inventory[item]
            print(f"Deleted {item} from inventory.")
        else:
            print("Error: Item not found in inventory.")
    elif action == "print":
        print("Current Inventory:")
        for key, value in inventory.items():
            print(f"{key}: ${value}")
    else:
        print("Error: Invalid action. Use 'update', 'delete', or 'print'.")

    return inventory

inventory = {"Apple": 1.5, "Banana": 0.75, "Orange": 1.25}
manage_inventory(inventory, "update", "Apple", 1.75)
manage_inventory(inventory, "delete", "Banana")
manage_inventory(inventory, "print")




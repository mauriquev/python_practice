inventory = {}

def add_to_inventory(item, quantity=1):
    if item in inventory:
        inventory[item] += quantity
    else:
        inventory[item] = quantity 
    print(f"Picked up {quantity} {item}")

def check_inventory():
    if not inventory:
        print(f"Your inventory is empty.")
    else:
        print("\nInventory:")
        for item, quanity in inventory.items():
            print(f"- {item}: {quanity}")
    

def start_game():
    player_name = input("What is your name, adventurer? ")
    print(f"Welcome, {player_name}! Let the adventure begin!")

    explore_forest()

def explore_forest():
    print("\nYou find youself in a dark forest. There is a cave on the right and a path on ahead.")
    choice = input("Do you want to do to enter the cave or follow the path? (cave/path): ").lower()

    if choice == "cave":
        cave_option()
    elif choice == "path":
        path_option()
    else:
        print("Invalid choice. please chose between cave or path")
        explore_forest()
def cave_option():
    print("\nYou enter the cave and find a treasure chest!")

def path_option():
    print("\nYou follow the path and discover a village.")

start_game() 
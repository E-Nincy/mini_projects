# Define the set of allowed user input options (e.g., "go", "take", "fight", "inventory", "quit")

# Create a dictionary to store player's inventory (e.g., empty at the beginning)

# Define the rooms:
# Each room has a name, a description, and optionally:
# - an item to collect
# - an opponent to fight
# - directions to other rooms

# Start in the initial room

# Game loop begins
    # Show current room name and description
    # If the room has an item and it's not yet collected, allow the player to collect it
    # If the room has an opponent:
        # Ask the player if they want to fight or run
        # If they choose to fight:
            # Check if they have needed items to fight
            # Use the random module to simulate a dice roll or random multiplier
            # Decide win/loss based on inventory + randomness
            # If they lose:
                # Empty the inventory
                # Maybe return them to a previous room
    # Ask the player what they want to do next (e.g., go north, check inventory, quit)
    # Process input and move to the next room or execute action

# End the game if player quits or dies


import random

# Allowed commands
commands = {"go", "take", "fight", "inventory", "quit"}

# Player inventory
inventory = set()

# Game rooms and structure
rooms = {
    "forest": {
        "description": "You are in a spooky forest. There is a sword lying on the ground.",
        "item": "sword",
        "north": "cave",
        "east": "lake"
    },
    "cave": {
        "description": "A dark cave. A fierce dragon blocks your path!",
        "opponent": "dragon",
        "south": "forest"
    },
    "lake": {
        "description": "A peaceful lake. There's a shield here.",
        "item": "shield",
        "west": "forest"
    }
}

# Starting position
current_room = "forest"

def show_inventory():
    if inventory:
        print("Inventory:", ", ".join(inventory))
    else:
        print("Your inventory is empty.")

def fight_opponent(opponent):
    print(f"You are fighting a {opponent}!")
    if opponent == "dragon":
        if "sword" in inventory:
            roll = random.randint(1, 6)
            print(f"You roll a {roll}...")
            if roll >= 4:
                print("You defeated the dragon! 🎉")
                return True
            else:
                print("The dragon defeated you! You drop all your items and flee! 💀")
                inventory.clear()
                return False
        else:
            print("You have no weapon to fight the dragon! You must run!")
            return False
    return True

# Main game loop
while True:
    room = rooms[current_room]
    print("\n" + room["description"])

    if "item" in room and room["item"] not in inventory:
        choice = input(f"Do you want to take the {room['item']}? (yes/no): ").lower()
        if choice == "yes":
            inventory.add(room["item"])
            print(f"You picked up the {room['item']}.")

    if "opponent" in room:
        action = input("Do you want to fight or run?: ").lower()
        if action == "fight":
            if not fight_opponent(room["opponent"]):
                current_room = "forest"
                continue
        else:
            print("You ran back to the forest!")
            current_room = "forest"
            continue

    command = input("What do you want to do? (go [direction] / inventory / quit): ").lower()

    if command == "inventory":
        show_inventory()
    elif command.startswith("go"):
        parts = command.split()
        if len(parts) == 2:
            direction = parts[1]
            if direction in room:
                current_room = room[direction]
            else:
                print("You can't go that way.")
        else:
            print("Please use 'go' followed by a direction, like 'go north'.")
    elif command == "quit":
        print("Thanks for playing!")
        break
    else:
        print("Invalid command. Try one of:", ", ".join(commands))
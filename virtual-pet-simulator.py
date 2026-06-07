# ==========================================================
# Virtual Pet Simulator
# Description:
# A simple command-line virtual pet game where the user can
# feed, play with, and monitor a pet's happiness and hunger.
# ==========================================================

# ----------------------------
# Function: Keep values between 0 and 100
# ----------------------------
def limit_stats(pet):
    pet["happiness"] = max(0, min(100, pet["happiness"]))
    pet["hunger"] = max(0, min(100, pet["hunger"]))


# ----------------------------
# Function: Feed the pet
# Hunger decreases
# Happiness decreases slightly
# ----------------------------
def feed_pet(pet):
    pet["hunger"] -= 15
    pet["happiness"] -= 2

    limit_stats(pet)

    print(f"\nYou fed {pet['name']}!")
    print("Hunger decreased by 15.")
    print("Happiness decreased by 2.")


# ----------------------------
# Function: Play with the pet
# Happiness increases
# Hunger increases slightly
# ----------------------------
def play_with_pet(pet):
    pet["happiness"] += 15
    pet["hunger"] += 10

    limit_stats(pet)

    print(f"\nYou played with {pet['name']}!")
    print("Happiness increased by 15.")
    print("Hunger increased by 10.")


# ----------------------------
# Function: Display pet status
# ----------------------------
def check_status(pet):

    if pet["happiness"] >= 70:
        mood = "😊 Happy"
    elif pet["happiness"] >= 40:
        mood = "😐 Neutral"
    else:
        mood = "😢 Sad"

    print("\n========== PET STATUS ==========")
    print(f"Name      : {pet['name']}")
    print(f"Happiness : {pet['happiness']}/100")
    print(f"Hunger    : {pet['hunger']}/100")
    print(f"Mood      : {mood}")
    print("================================")


# ----------------------------
# Function: Simulate time passing
# Called every few actions
# ----------------------------
def time_passes(pet):
    pet["hunger"] += 5
    pet["happiness"] -= 3

    limit_stats(pet)

    print("\n⏳ Time has passed...")
    print("Hunger increased by 5.")
    print("Happiness decreased by 3.")


# ----------------------------
# Function: Check if pet is very hungry
# ----------------------------
def hungry_effect(pet):

    if pet["hunger"] > 80:
        pet["happiness"] -= 10

        limit_stats(pet)

        print("\n⚠ Your pet is very hungry!")
        print("Happiness decreased by 10.")


# ----------------------------
# Function: Check game over conditions
# Returns True if game should end
# ----------------------------
def game_over(pet):

    if pet["hunger"] >= 100:
        print("\n💀 GAME OVER!")
        print(f"{pet['name']} became too hungry.")
        return True

    if pet["happiness"] <= 0:
        print("\n💀 GAME OVER!")
        print(f"{pet['name']} became too sad.")
        return True

    return False


# ----------------------------
# Function: Display menu
# ----------------------------
def display_menu():
    print("\n========== VIRTUAL PET ==========")
    print("1. Feed Pet")
    print("2. Play With Pet")
    print("3. Check Status")
    print("4. Quit")
    print("=================================")


# ==========================
# Main Program Starts Here
# ==========================

print("🐾 Welcome to the Virtual Pet Simulator!")

# Ask user to name the pet
pet_name = input("Enter your pet's name: ")

# Store pet information in a dictionary
pet = {
    "name": pet_name,
    "happiness": 50,
    "hunger": 50
}

# Counts user actions
action_count = 0

# Controls the main game loop
game_running = True

print(f"\nYour pet {pet['name']} has been created!")
print("Take good care of your pet!")

# Main game loop
while game_running:

    display_menu()

    choice = input("Enter your choice (1-4): ")

    # --------------------
    # Feed Pet
    # --------------------
    if choice == "1":
        feed_pet(pet)
        action_count += 1

    # --------------------
    # Play With Pet
    # --------------------
    elif choice == "2":
        play_with_pet(pet)
        action_count += 1

    # --------------------
    # Check Status
    # --------------------
    elif choice == "3":
        check_status(pet)
        action_count += 1

    # --------------------
    # Quit Game
    # --------------------
    elif choice == "4":
        print("\nThanks for playing!")
        print(f"Goodbye from {pet['name']}! 👋")
        break

    # --------------------
    # Invalid Choice
    # --------------------
    else:
        print("\n❌ Invalid choice.")
        print("Please enter a number between 1 and 4.")
        continue

    # -----------------------------------
    # Every 3 actions, time passes
    # -----------------------------------
    if action_count == 3:
        time_passes(pet)
        action_count = 0

    # -----------------------------------
    # If hunger is very high,
    # pet becomes sad
    # -----------------------------------
    hungry_effect(pet)

    # -----------------------------------
    # Check game over conditions
    # -----------------------------------
    if game_over(pet):
        game_running = False

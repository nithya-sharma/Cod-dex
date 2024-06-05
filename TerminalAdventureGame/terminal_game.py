import random

print("Hello, Welcome to Phoenix Rebirth!")
print("As the first light of dawn breaks over the horizon, you awaken in your nest, nestled high in the ancient, towering trees of the Mystical Forest.") 
print("Your feathers glisten with a fiery glow, reflecting the early morning sun.") 
print("Below, the forest is alive with the sounds of nature—chirping birds, rustling leaves, and the distant roar of a waterfall.")
print("Today is no ordinary day. You sense it in the air. There are challenges to face, choices to make, and paths that will shape your destiny as a phoenix.")
print("Your goal is clear: survive the day, interact with the inhabitants of this magical realm, and make decisions that will guide your journey.")

# Player Status
hp = 100

# Morning Choices
print("\nWhat do you want to do today?")
print("1) Fly to the nearby forest.")
print("2) Visit the village.")
print("3) Rest at the camp.")
morning_choice = int(input("Enter the number of your choice: "))

if morning_choice == 1:
    print("You fly to the magical forest...")
    event = random.choice(["strange animal", "friendly traveler", "hidden treasure"])
    if event == "strange animal":
        print("You encounter a strange animal and engage in combat.")
        combat_result = random.choice(["win", "lose"])
        if combat_result == "win":
            print("You defeat the strange animal and gain 10 health points.")
            hp += 10
        else:
            print("You lose the battle and lose 20 health points.")
            hp -= 20
    elif event == "friendly traveler":
        print("You meet a friendly traveler who offers you food. You gain 50 health points.")
        hp += 50
    else:
        print("You find a hidden treasure and gain 100 health points and experience points.")
        hp += 100
      
elif morning_choice == 2:
    print("You fly over to the nearby village...")
    print("You meet a kid who feeds you and asks for a ride in the sky as return.")
    print("Do you accept the request?")
    print("1) Yes.")
    print("2) No.")
    village_choice = int(input("Enter the number of your choice: "))
    if village_choice == 1:
        print("You make a friend and gain 20 health points.")
        hp += 20
    else:
        print("You politely decline and continue your journey.")
elif morning_choice == 3:
    print("You rest at the camp and regain your strength.")
    hp += 20

# Afternoon Choices
print("\nIt's now afternoon, what would you like to do next?")
print("1) Visit the nearby wishing well.")
print("2) Explore the healing waterfall.")
afternoon_choice = int(input("Enter the number of your choice: "))

if afternoon_choice == 1:
    print("You visit the wishing well...")
    print("You encounter a wizard in disguise who asks for a feather.")
    print("Do you give the wizard a feather?")
    print("1) Yes.")
    print("2) No.")
    wizard_choice = int(input("Enter the number of your choice: "))
    if wizard_choice == 1:
        print("The wizard grants you a wish and you gain 100 health points.")
        hp += 100
    else:
        print("The wizard curses you and you lose 100 health points.")
        hp -= 100
elif afternoon_choice == 2:
    print("You explore the healing waterfall...")
    print("You feel rejuvenated by the healing properties of the waterfall.")
    hp += 50

# Night Choices
print("\nThe night falls, what would you like to do to end the day?")
print("1) Go back to your nest.")
print("2) Fly in search of your next adventure.")
night_choice = int(input("Enter the number of your choice: "))

if night_choice == 1:
    print("You return to your nest and rest for the night. See you tomorrow!")
else:
    print("You fly in search of your next adventure. Coming soon...")

# Final Status
print(f"\nFinal Health Points: {hp}")

if hp <= 0:
    print("You have lost all your health points. Game Over!")
else:
    print("Congratulations! You have survived the day and gained valuable experiences.")

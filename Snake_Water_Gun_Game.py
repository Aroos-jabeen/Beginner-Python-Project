import random

title = '''
=================================================
=       +++++++ Let's Play +++++++              =
=      ****************************** =
=      * SNAKE , WATER , GUN      * =
=      ****************************** =
================================================='''
print(title)

options = ["Snake", "Water", "Gun"]
user_score = 0
comp_score = 0

while True:
    print(f"\nScore -> You: {user_score} | Computer: {comp_score}")
    user_turn = input("\nEnter choice (Snake, Water, Gun) or 'Exit' to quit: ").capitalize()

    if user_turn == "Exit":
        print("\nFinal Results:")
        print(f"You: {user_score} | Computer: {comp_score}")
        print("Thanks for playing! Goodbye.")
        break

    if user_turn not in options:
        print(" Invalid choice! Please type Snake, Water, or Gun.")
        continue

    system_choice = random.choice(options)
    print(f"--- Computer chose: {system_choice} ---")

    # Game Logic
    if user_turn == system_choice:
        print(" It's a Draw!")
    
    elif (user_turn == "Snake" and system_choice == "Water") or \
         (user_turn == "Gun" and system_choice == "Snake") or \
         (user_turn == "Water" and system_choice == "Gun"):
        print( "You Win this round!")
        user_score += 1
        
    else:
        print(" You Lose this round!")
        comp_score += 1
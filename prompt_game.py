#!/usr/bin/env python3
"""
Prompt Quest — simple text prompt game
Save as prompt_game.py and run: python prompt_game.py
"""

import random
import sys
import time

def slow_print(text, delay=0.03):
    for ch in text:
        print(ch, end="", flush=True)
        time.sleep(delay)
    print()

def get_choice(prompt, choices):
    """Ask user until they enter one of choices (case-insensitive)."""
    choices_lower = [c.lower() for c in choices]
    while True:
        ans = input(prompt).strip().lower()
        if ans in choices_lower:
            return ans
        print(f"Please type one of: {', '.join(choices)}")

def intro():
    slow_print("Welcome to Prompt Quest!")
    slow_print("A tiny text-adventure where your choices matter.\n")

def forest_encounter(player):
    slow_print("You enter a moonlit forest. Two paths appear.")
    choice = get_choice("Do you go LEFT (l) or RIGHT (r)? ", ["l", "r", "left", "right"])
    if choice.startswith("l"):
        slow_print("A friendly fox offers you a riddle.")
        return riddle_challenge(player)
    else:
        slow_print("You stumble on a sleeping goblin who drops a coin purse.")
        player['gold'] += 10
        slow_print("You pick up 10 gold.")
        return player

def riddle_challenge(player):
    slow_print('"I speak without a mouth and hear without ears. I have nobody, but I come alive with wind. What am I?"')
    attempts = 3
    while attempts:
        answer = input(f"Your answer ({attempts} attempts left): ").strip().lower()
        if "echo" in answer:
            slow_print("The fox nods approvingly and gives you a charm (+1 luck).")
            player['luck'] += 1
            return player
        attempts -= 1
    slow_print("The fox shrugs and disappears. Better luck next time.")
    return player

def cave_encounter(player):
    slow_print("You reach a dark cave with a locked gate and a keypad.")
    code = str(random.randint(1, 9)) + str(random.randint(1, 9))  # two-digit code
    # give hints based on luck
    if player['luck'] > 0:
        slow_print("Your charm tingles — you sense the code is two digits between 1 and 9.")
    attempts = 3
    while attempts:
        guess = input(f"Enter the 2-digit code ({attempts} attempts left): ").strip()
        if guess == code:
            slow_print("The gate opens! You find a treasure chest (+50 gold).")
            player['gold'] += 50
            return player
        else:
            slow_print("Incorrect.")
        attempts -= 1
    slow_print("You retreat from the cave empty-handed.")
    return player

def final_choice(player):
    slow_print("\nA dragon blocks the path to the castle. You have two options:")
    slow_print("A) Offer gold to distract it.")
    slow_print("B) Challenge it (fight).")
    pick = get_choice("Choose A or B: ", ["a", "b", "A", "B"])
    if pick.lower() == "a":
        if player['gold'] >= 30:
            slow_print("You toss gold. The dragon snatches it and lets you pass. You're clever!")
            player['gold'] -= 30
            player['score'] += 50
        else:
            slow_print("Not enough gold! The dragon is annoyed and scorches you. Ouch.")
            player['score'] -= 10
    else:
        power = random.randint(1, 10) + player['luck']
        slow_print(f"You charge! (your attack power roll: {power})")
        if power >= 7:
            slow_print("You defeat the dragon with bravery! Glory is yours.")
            player['score'] += 80
        else:
            slow_print("The dragon overpowers you and you barely escape.")
            player['score'] += 5
    return player

def game_loop():
    player = {'gold': 0, 'luck': 0, 'score': 0}
    intro()
    name = input("Adventurer name: ").strip() or "Traveler"
    slow_print(f"Good luck, {name}!\n")
    time.sleep(0.3)

    # Stage 1: Forest
    player = forest_encounter(player)
    time.sleep(0.3)

    # Stage 2: Cave
    player = cave_encounter(player)
    time.sleep(0.3)

    # Stage 3: Final
    player = final_choice(player)
    time.sleep(0.3)

    slow_print("\n--- Game Over ---")
    slow_print(f"Name : {name}")
    slow_print(f"Gold : {player['gold']}")
    slow_print(f"Luck : {player['luck']}")
    slow_print(f"Score: {player['score']}")
    if player['score'] >= 80:
        slow_print("Legendary outcome — you will be sung about for ages! 🏆")
    elif player['score'] >= 30:
        slow_print("A fine adventure — well done!")
    else:
        slow_print("That was rough. Try again to improve your score.")
    input("\nPress Enter to exit...")

if __name__ == "__main__":
    try:
        game_loop()
    except KeyboardInterrupt:
        print("\nGoodbye!")
        sys.exit(0)

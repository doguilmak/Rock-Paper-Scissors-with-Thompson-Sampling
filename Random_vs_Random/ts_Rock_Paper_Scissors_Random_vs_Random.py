# -*- coding: utf-8 -*-
"""
Created on Wed Sep 28 21:53:46 2022

@author: doguilmak
"""
#%%
# 1.Random Selection        

import matplotlib.pyplot as plt
import random
import seaborn as sns
import pandas as pd

#%%
# 2.Building game

random_1_win = 0
random_1_lost = 0
random_2_win = 0
random_2_lost = 0
draw = 0        
    
rounds = 0

rock_row = {'r': 1, 'p': 0, 's': 0}
paper_row = {'r': 0, 'p': 1, 's': 0}
scissors_row = {'r': 0, 'p': 0, 's': 1}
possible_actions = ["rock", "paper", "scissors"]

random_1_df = pd.DataFrame(columns=['r', 'p', 's'])
random_2_df = pd.DataFrame(columns=['r', 'p', 's'])

while True:
    
    if rounds == 100:
        print("\nRANDOM SELECTION - 1")
        print(f"Random Selection Lose: {random_1_lost}")
        print(f"Random Selection Wins: {random_1_win}")
        print(f"Draws: {draw}")
        print(f"\nRock-Paper-Scissors Random Selection DataFrame:\n{random_1_df}\n")
        print("\nRANDOM SELECTION - 2")
        print(f"Random Selection Lose: {random_2_lost}")
        print(f"Random Selection Wins: {random_2_win}")
        print(f"Draws: {draw}")
        print(f"\nRock-Paper-Scissors Random Selection DataFrame:\n{random_2_df}\n")
        break   
    
    # Random Selection - 1
    random_1 = random.choice(possible_actions)
    if random_1 == "rock":
        random_1_df = random_1_df.append(rock_row, ignore_index=True)      
    elif random_1 == "paper":
        random_1_df = random_1_df.append(paper_row, ignore_index=True) 
    else:
        random_1_df = random_1_df.append(scissors_row, ignore_index=True)
    
    # Random Selection - 2
    random_2 = random.choice(possible_actions)
    if random_2 == "rock":
        random_2_df = random_2_df.append(rock_row, ignore_index=True)      
    elif random_2 == "paper":
        random_2_df = random_2_df.append(paper_row, ignore_index=True) 
    else:
        random_2_df = random_2_df.append(scissors_row, ignore_index=True)

    print(f"\n----------------- Round {str(rounds)} -----------------\n"+ \
          "\nRandom selection 1 action: " +  str(random_1) + \
          "\nRandom selection 2 action: " + str(random_2))
     
    if random_1 == random_2:
        print(f"Both players selected {random_1}. It's a TIE!")
        draw += 1
    elif random_1 == "rock":
        if random_2 == "scissors":
            print("Rock smashes scissors! Random selection one WIN!")
            random_1_win += 1
            random_2_lost += 1
        else:
            print("Paper covers rock! Random selection two WIN!")
            random_1_lost += 1
            random_2_win += 1
    elif random_1 == "paper":
        if random_2 == "rock":
            print("Paper covers rock! Random selection one WIN!")
            random_1_win += 1
            random_2_lost += 1
        else:
            print("Scissors cuts paper! Random selection two WIN!")
            random_1_lost += 1
            random_2_win += 1
    elif random_1 == "scissors":
        if random_2 == "paper":
            print("Scissors cuts paper! Random selection one WIN!")
            random_1_win += 1
            random_2_lost += 1
        else:
            print("Rock smashes scissors! Random selection two WIN!")
            random_1_lost += 1
            random_2_win += 1

    rounds += 1
# Save dataframes as xlsx
random_1_df.to_excel("random_1_df.xlsx")
random_2_df.to_excel("random_2_df.xlsx")

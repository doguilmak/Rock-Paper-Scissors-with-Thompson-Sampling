# -*- coding: utf-8 -*-
"""
Created on Mon Nov  1 21:56:58 2021

@author: doguilmak
"""
#%%
# Importing Libraries

import matplotlib.pyplot as plt
import random
import seaborn as sns
import numpy as np
import pandas as pd
from random import randint

#%%
# Thompson Sampling

def thompson_sampling(df):
    
    N = df.shape[0]  # Number of rows
    d = df.shape[1]  # Number of ads (columns)
    summation = 0  # Summation reward
    chosen = []  # Ni(n) 
    ones = [0] * d
    zeros = [0] * d
    for n in range(1, N):
        ad = 0  # Chosen
        max_th = 0
        for i in range(0, d):
            rasbeta = random.betavariate(ones[i] + 1, zeros[i] + 1)
            if rasbeta > max_th:
                max_th = rasbeta
                ad = i
        chosen.append(ad)
        reward = df.values[n, ad]
        if reward == 1:
            ones[ad] = ones[ad] + 1
        else:
            zeros[ad] = zeros[ad] + 1
        summation = summation + reward
        
    chosen.append(randint(0, 2))
    thompson=np.bincount(chosen).argmax()
    print(f"Summation: {summation} - Thompson sampling: {thompson}")
    
    plt.figure(figsize = (12, 12))
    sns.set_style('whitegrid')    
    sns.histplot(data=chosen, kde=True)
    plt.title("Thompson Sampling")
    plt.xlabel("Selections")
    plt.ylabel("Numbers of the Chosen Number")
    plt.show()    

    return thompson


wins = 0
loses = 0
draws = 0
d = pd.DataFrame(columns=['r', 'p', 's'])

while True:
    
    user_action = input("Enter a choice (rock, paper, scissors): ") 
           
    if user_action == 'q':
        print("\n\nYou have completed the duel.")
        print("\nTHOMPSON SAMPLING")
        thompson_sampling(d)
        print(f"Loses: {loses}")
        print(f"Wins: {wins}")
        print(f"Draws: {draws}")
        print(f"Rock-Paper-Scissors DataFrame:\n{d}\n")        
        break
      
    if user_action == "rock":
        new_row = {'r': 1, 'p': 0, 's': 0}
        d = d.append(new_row, ignore_index=True)        
        
        # Thompson Sampling
        thompson_choose=thompson_sampling(d)
        if thompson_choose== 0:
            computer_action="paper"
        elif thompson_choose == 1:
            computer_action="scissors"
        else:
            computer_action="rock"
    
    elif user_action == "paper":
        new_row = {'r': 0, 'p': 1, 's': 0}
        d = d.append(new_row, ignore_index=True)        
        
        # Thompson Sampling
        thompson_choose=thompson_sampling(d)
        if thompson_choose== 0:
            computer_action="paper"
        elif thompson_choose == 1:
            computer_action="scissors"
        else:
            computer_action="rock"
    
    elif user_action == "scissors":
        new_row = {'r': 0, 'p': 0, 's': 1}
        d = d.append(new_row, ignore_index=True)        
        
        # Thompson Sampling
        thompson_choose=thompson_sampling(d)
        if thompson_choose == 0:
            computer_action="paper"
        elif thompson_choose == 1:
            computer_action="scissors"
        else:
            computer_action="rock"
    else:
        print("Unexpected input.")
        
    print(f"You chose {user_action}, computer chose {computer_action}.")
    if user_action == computer_action:
        print(f"Both players selected {user_action}. It's a TIE!")
        draws += 1
    elif user_action == "rock":
        if computer_action == "scissors":
            print("Rock smashes scissors! You WIN!")
            wins += 1
        else:
            print("Paper covers rock! You LOSE.")
            loses += 1
    elif user_action == "paper":
        if computer_action == "rock":
            print("Paper covers rock! You WIN!")
            wins += 1
        else:
            print("Scissors cuts paper! You LOSE.")
            loses += 1
    elif user_action == "scissors":
        if computer_action == "paper":
            print("Scissors cuts paper! You WIN!")
            wins += 1
        else:
            print("Rock smashes scissors! You LOSE.")
            loses += 1
            
#%%    
"""
# Random Selection        

import random

wins_rand = 0
loses_rand = 0
draws_rand = 0        
    
games2play = int(input('How many games would you like to play?\n'))


possible_actions = ["rock", "paper", "scissors"] 

while True:
    
    if games2play == 0:
        print("\nRANDOM SELECTION")
        print(f"Loses: {loses_rand}")
        print(f"Wins: {wins_rand}")
        print(f"Draws: {draws_rand}")
        break   
        
    computer_action_random = random.choice(possible_actions)
    
    user_action = input("Enter a choice (rock, paper, scissors): ")
    print(f"You chose {user_action}, computer chose {computer_action_random}.")
    if user_action == computer_action_random:
        print(f"Both players selected {user_action}. It's a TIE!")
        draws_rand += 1
    elif user_action == "rock":
        if computer_action_random == "scissors":
            print("Rock smashes scissors! You WIN!")
            wins_rand += 1
        else:
            print("Paper covers rock! You LOSE.")
            loses_rand += 1
    elif user_action == "paper":
        if computer_action_random == "rock":
            print("Paper covers rock! You WIN!")
            wins_rand += 1
        else:
            print("Scissors cuts paper! You LOSE.")
            loses_rand += 1
    elif user_action == "scissors":
        if computer_action_random == "paper":
            print("Scissors cuts paper! You WIN!")
            wins_rand += 1
        else:
            print("Rock smashes scissors! You LOSE.")
            loses_rand += 1
    
    games2play-=1
"""    

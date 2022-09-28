# -*- coding: utf-8 -*-
"""
Created on Mon Nov  1 21:56:58 2021

@author: doguilmak
"""
#%%
# 1.Importing Libraries

import matplotlib.pyplot as plt
import random
import seaborn as sns
import numpy as np
import pandas as pd
from random import randint

#%%
# 2.Thompson Sampling

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

#%%
# 3.Building Game

rs_win = 0
rs_lose = 0
ts_win = 0
ts_lose = 0
draws = 0
rounds = 0

rs_df = pd.DataFrame(columns=['r', 'p', 's'])
ts_df = pd.DataFrame(columns=['r', 'p', 's'])

rock_row = {'r': 1, 'p': 0, 's': 0}
paper_row = {'r': 0, 'p': 1, 's': 0}
scissors_row = {'r': 0, 'p': 0, 's': 1}
desicion = ['rock', 'paper', 'scissors']

while True:

    if rounds == 100:
        print("\nTHOMPSON SAMPLING")
        print(f"Thompson Sampling: {thompson_sampling(rs_df)}")
        print(f"Thompson Sampling Lose: {ts_lose}")
        print(f"Thompson Sampling Wins: {ts_win}")
        print(f"Draws: {draws}")
        print(f"Rock-Paper-Scissors Thompson Sampling DataFrame:\n{ts_df}\n")
        print("\nRANDOM SELECTION")
        print(f"Random Selection Lose: {rs_lose}")
        print(f"Random Selection Wins: {rs_win}")
        print(f"Draws: {draws}")
        print(f"Rock-Paper-Scissors Random Selection DataFrame:\n{rs_df}\n")
        break
    
    # Random Selection
    random_action = random.choice(desicion)
    if random_action == "rock":
        rs_df = rs_df.append(rock_row, ignore_index=True)      
    elif random_action == "paper":
        rs_df = rs_df.append(paper_row, ignore_index=True) 
    else:
        rs_df = rs_df.append(scissors_row, ignore_index=True)        
    
    # Thompson Sampling
    thompson_choose=thompson_sampling(rs_df)
    if thompson_choose== 0:
        ts_df = ts_df.append(paper_row, ignore_index=True)
        thompson_action="paper"
    elif thompson_choose == 1:
        ts_df = ts_df.append(scissors_row, ignore_index=True)
        thompson_action="scissors"
    else:
        ts_df = ts_df.append(rock_row, ignore_index=True)
        thompson_action="rock"
      
    print(f"\n----------------- Round {str(rounds)} -----------------\n"+ \
          "\nRandom selection action: " +  str(random_action) + "\nAI action: "\
          + str(thompson_action))
    if random_action == thompson_action:
        print(f"Both players selected {random_action}. It's a TIE!")
        draws += 1
    elif random_action == "rock":
        if thompson_action == "scissors":
            print("Rock smashes scissors! Random selection WIN!")
            rs_win += 1
            ts_lose += 1
        else:
            print("Paper covers rock! Thompson sampling WIN!")
            rs_lose += 1
            ts_win += 1
    elif random_action == "paper":
        if thompson_action == "rock":
            print("Paper covers rock! Random selection WIN!")
            rs_win += 1
            ts_lose += 1
        else:
            print("Scissors cuts paper! Thompson sampling WIN!")
            rs_lose += 1
            ts_win += 1
    elif random_action == "scissors":
        if thompson_action == "paper":
            print("Scissors cuts paper! Random selection WIN!")
            rs_win += 1
            ts_lose += 1
        else:
            print("Rock smashes scissors! Thompson sampling WIN!")
            rs_lose += 1
            ts_win += 1
        
    rounds += 1
       
# Save dataframes as xlsx
ts_df.to_excel("ts_df.xlsx")
rs_df.to_excel("rs_df.xlsx")
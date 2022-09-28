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

ai2_win = 0
ai1_win = 0
ai1_lose = 0
ai2_lose = 0
draws = 0
rounds = 0

ts_1 = pd.DataFrame(columns=['r', 'p', 's'])
ts_2 = pd.DataFrame(columns=['r', 'p', 's'])

rock_row = {'r': 1, 'p': 0, 's': 0}
paper_row = {'r': 0, 'p': 1, 's': 0}
scissors_row = {'r': 0, 'p': 0, 's': 1}

while True:
       
    if rounds == 100:
        print("\nTHOMPSON SAMPLING-1")
        print(f"AI-1 Thompson Sampling: {thompson_sampling(ts_1)}")
        print(f"AI-1 Loses: {ai1_lose}")
        print(f"AI-1 Wins: {ai1_win}")
        print(f"Draws: {draws}\n")
        print(f"Rock-Paper-Scissors Thompson Sampling-1 DataFrame:\n{ts_1}\n")        
        print("\nTHOMPSON SAMPLING-2")
        print(f"AI-2 Thompson Sampling: {thompson_sampling(ts_2)}")
        print(f"AI-2 Loses: {ai2_lose}")
        print(f"AI-2 Wins: {ai2_win}")
        print(f"Draws: {draws}")
        print(f"Rock-Paper-Scissors Thompson Sampling-2 DataFrame:\n{ts_2}\n")
        break
      
    # Thompson Sampling AI - 1
    ai1_choose=thompson_sampling(ts_2)
    if ai1_choose== 0:
        ts_1 = ts_1.append(paper_row, ignore_index=True)
        ai1_action="paper"
    elif ai1_choose == 1:
        ts_1 = ts_1.append(scissors_row, ignore_index=True)
        ai1_action="scissors"
    else:
        ts_1 = ts_1.append(rock_row, ignore_index=True)
        ai1_action="rock"
    
    # Thompson Sampling AI - 2
    ai2_choose = thompson_sampling(ts_1)
    if ai2_choose== 0:
        ts_2 = ts_2.append(paper_row, ignore_index=True)
        ai2_action="paper"
    elif ai2_choose == 1:
        ts_2 = ts_2.append(scissors_row, ignore_index=True)
        ai2_action="scissors"
    else:
        ts_2 = ts_2.append(rock_row, ignore_index=True)
        ai2_action="rock"
    
    
    print(f"\n----------------- Round {str(rounds)} -----------------\n"+ \
      "\nAI-1 action action: " +  str(ai1_action) + "\nAI-2 action: "\
      + str(ai2_action))
        
    if ai2_action == ai1_action:
        print(f"Both players selected {ai2_action}. It's a TIE!")
        draws += 1
    elif ai2_action == "rock":
        if ai1_action == "scissors":
            print("Rock smashes scissors! AI-2 WIN!")
            ai2_win += 1
            ai1_lose += 1
        else:
            print("Paper covers rock! AI-1 WIN!")
            ai2_lose += 1
            ai1_win += 1
    elif ai2_action == "paper":
        if ai1_action == "rock":
            print("Paper covers rock! AI-2 WIN!")
            ai2_win += 1
            ai1_lose += 1
        else:
            print("Scissors cuts paper! AI-1 WIN!")
            ai2_lose += 1
            ai1_win += 1
    elif ai2_action == "scissors":
        if ai1_action == "paper":
            print("Scissors cuts paper! AI-2 WIN!")
            ai2_win += 1
            ai1_lose += 1
        else:
            print("Rock smashes scissors! AI-1 WIN!")
            ai2_lose += 1
            ai1_win += 1
        
    rounds += 1
       
# Save dataframes as xlsx
ts_1.to_excel("ts_1.xlsx")
ts_2.to_excel("ts_2.xlsx")
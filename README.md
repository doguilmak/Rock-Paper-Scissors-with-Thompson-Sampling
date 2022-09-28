**<h1 align=center><font size = 6>Rock Paper Scissors with Thompson Sampling</font></h1>**

 <img src="https://pxt.azureedge.net/blob/68f66c3ddc3acfc4c53157abf92eace202d46db2/static/courses/csintro/conditionals/rock-paper-scissors-items.png" width=1000 height=400 >

<small>Picture Source: <a href="pxt.azureedge.net">pxt.azureedge.net</a></small>

<br>

<h2>Problem Statement</h2>

<p>This project aims to achieve maximum success by the algorithm in the rock-paper-scissors game together with the <b>reinforcement (Thompson sampling) learning</b>method. The achievement of this success will be shaped by the preferences chosen by the user. At the end of each action, the rock, paper, or scissors with the <b>highest beta value and the corresponding value were selected.</b> Compared to the bots that make a random choice, the <b>artificial intelligence model and the integrated model have proven to be more successful</b> in my tests.</p>

<br>

<h2>Dataset</h2>

<p>The dataset was <b>created automatically. As a result of the values selected from the rock-paper-scissors options</b> selected by the user. There was no educational or training background in the method. The results and the dataset are personal.</p>

<br>

<h2>Methodology</h2>

<p>In this project, as stated in the title, results were obtained through the <b>Thompson sampling</b> algorithm. </p>

<br>

$$\theta_i(n) = \beta(N_i^1(n) + 1, N_i^0(n) + 1)$$

<br>

<p>As seen in the formula:</p>

1. First, $N_i^0(n)$ and $N_i^1(n)$ numbers were calculated for each action.

	$N_i^0(n)$ = The number of times 0 received as a reward so far.

	$N_i^1(n)$= Number of times 1 received as a reward so far.

2. Secondly, a random number is generated in the beta distribution specified in the formula for each claim.

3. Finally, we took the value with the highest beta value. This value will indicate the option the algorithm will play against us.

<p>The results were showed on the histogram at the end of each operation. In other words, the tendency of the sampling was indicated on the histogram. Thompson sampling was much more successful than a random one.</p>

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

<p>You are free to visit <a  href="https://en.wikipedia.org/wiki/Thompson_sampling">Thompson sampling</a>  Wikipedia website for learn the method better.</p>

<br>

<h2>Analysis</h2>

<h3>Branching process</h3>

<p>The general outline of the game was created in below. Then the game continued until the user pressed the <b>q</b> key, with a while loop.</p>

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

<br>

<p><b>Thompson Sampling Results</b></p>

<p>The histogram specified in <i>ts_histogram.png</i> shows the distribution of the last round. In line with the preferences, the algorithm obtained inferences from the user's preferences and only 1 win was obtained in 12 rounds. The system made a <b>random choice only in the first round.</b></p>

<p>You can find detailed preferences and results in <i>console_ts.xml</i>.</p>

<i>Loses: 5</i>

<i>Wins: 1</i>

<i>Draws: 6</i>

<br>

<p><b>Random Selection Results</b></p>

<i>Loses: 1</i>

<i>Wins: 6</i>

<i>Draws: 5</i>

<p>These results show only one of the obtained results. Many more virtual duels can be created and hypothesis tested through various loops. As can be understood, Thompson sampling prevailed more.</p>

<br>

<h3>Comparing Random Selection and Thompson Sampling</h3>

<p>Within the scope of this project, 100 different games were simulated to reach more detailed inferences and results. Within the scope of this project, 100 different games were simulated to reach more detailed inferences and results. In total, we simulated 300 games; Random vs. Random, Random vs. Thompson Sampling, and finally Thompson Sampling vs. Thompson Sampling. These results were performed using Thompson Sampling 1 and Random Selection 1.</p>

<b>Rounds Probabilities</b>

|  | Random Selection | Thompson Sampling |
|:--:|:--:|:--:|
| Random Selection | Win: %35, Lose: %37, Draw: %28 | Win: %25, Lose: %38, Draw: %37 |
| Thompson Sampling | Win: %38, Lose: %25, Draw: %37 | Win: %44, Lose: %48, Draw: %8 |

<br>

<h4>Each Rounds on Excel File</h4>

<p>The decisions made per round played were created as dataframes and then saved in different files in <i>.xlsx</i> format. There are two different excel files for each situation. This is because there are two different game players. A different dataframe was created for each player.</p>

<ul>
	<li><a href="https://github.com/doguilmak/Rock-Paper-Scissors-with-Thompson-Sampling-AI/tree/main/Random_vs_Random">Random Selection vs Random Selection</a>
<ol>
	    <li><a href="https://github.com/doguilmak/Rock-Paper-Scissors-with-Thompson-Sampling-AI/blob/main/Random_vs_Random/random_1_df.xlsx">random_1_df.xlsx</a></li>
	    <li><a href="https://github.com/doguilmak/Rock-Paper-Scissors-with-Thompson-Sampling-AI/blob/main/Random_vs_Random/random_2_df.xlsx">random_2_df.xlsx</a></li>
  </ol>
</li>
	<li><a href="https://github.com/doguilmak/Rock-Paper-Scissors-with-Thompson-Sampling-AI/tree/main/Random_vs_TS">Random Selection vs Thompson Sampling</a>
	<ol>
	    <li><a href="https://github.com/doguilmak/Rock-Paper-Scissors-with-Thompson-Sampling-AI/blob/main/Random_vs_TS/rs_df.xlsx">rs_df.xlsx</a></li>
	    <li><a href="https://github.com/doguilmak/Rock-Paper-Scissors-with-Thompson-Sampling-AI/blob/main/Random_vs_TS/ts_df.xlsx">ts_df.xlsx</a></li>
  </ol></li>
	<li><a href="https://github.com/doguilmak/Rock-Paper-Scissors-with-Thompson-Sampling-AI/tree/main/TS_vs_TS">Thompson Sampling vs Thompson Sampling</a>
	<ol>
	    <li><a href="https://github.com/doguilmak/Rock-Paper-Scissors-with-Thompson-Sampling-AI/blob/main/TS_vs_TS/ts_1.xlsx">ts_1.xlsx</a></li>
	    <li><a href="https://github.com/doguilmak/Rock-Paper-Scissors-with-Thompson-Sampling-AI/blob/main/TS_vs_TS/ts_2.xlsx">ts_2.xlsx</a></li>
  </ol>
  </li>
</ul>

<h4 align=center><font size = 4>Thompson Sampling vs Thompson Sampling</font></h4>

| Thompson Sampling 1 | Thompson Sampling 2 |
|--|--|
| <img  src="https://raw.githubusercontent.com/doguilmak/Rock-Paper-Scissors-with-Thompson-Sampling-AI/main/TS_vs_TS/TS-1.png"  width=1000  height=500  alt="https://github.com/iamvigneshwars/rock-paper-scissors-ai"> | <img  src="https://raw.githubusercontent.com/doguilmak/Rock-Paper-Scissors-with-Thompson-Sampling-AI/main/TS_vs_TS/TS-2.png" width=1000 height=500 alt="https://github.com/iamvigneshwars/rock-paper-scissors-ai"> |

<small>Picture Source: <a href="https://github.com/doguilmak/Rock-Paper-Scissors-with-Thompson-Sampling-AI">doguilmak</a></small>

<p>You can examine the preference distribution of two different thompson sampling users on the above-mentioned histogram graphs.</p>

<h4 align=center><font size = 4>Random Selection vs Thompson Sampling</font></h4>

<img  src="https://raw.githubusercontent.com/doguilmak/Rock-Paper-Scissors-with-Thompson-Sampling-AI/main/Random_vs_TS/Random_vs_TS.png"  width=1000  height=500  alt="https://github.com/iamvigneshwars/rock-paper-scissors-ai">

<small>Picture Source: <a href="https://raw.githubusercontent.com/doguilmak/Rock-Paper-Scissors-with-Thompson-Sampling-AI/main/Random_vs_TS/Random_vs_TS.png">doguilmak</a></small>

<p>You can examine the preference distribution Random Selection and Thompson Sampling users on the above-mentioned histogram graphs.</p>

<br>

<h2>How to Run Code</h2>

<p>Before running the code make sure that you have these libraries:</p>

 - pandas 
 - matplotlib
 - seaborn
 - numpy
 - random
 
<h2>Contact Me</h2>

If you have something to say to me please contact me: 

 - Twitter: [Doguilmak](https://twitter.com/Doguilmak) 
 - Mail address: doguilmak@gmail.com
 

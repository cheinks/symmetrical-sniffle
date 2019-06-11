# imports - modules, A.P.I.'s, libraries
import random


# Definitions of functions, classes
def who_won(player, computer):  # Interprets player and computer responses, returns either win, loss, or tie.
    if player == computer:
        print("It's a tie!")
        return 'T'
    elif player == 0:
        if computer == 1:
            print("Ha ha, I won.")
            return 'L'
        elif computer == 2:
            print("Looks like you beat me this time.")
            return 'W'
    elif player == 1:
        if computer == 2:
            print("Ha ha, I won.")
            return 'L'
        elif computer == 0:
            print("Looks like you beat me this time.")
            return 'W'
    else:
        if computer == 0:
            print("Ha ha, I won.")
            return 'L'
        elif computer == 1:
            print("Looks like you beat me this time.")
            return 'W'


def what_to_play(r_times, p_times, s_times, games):  # Checks for a pattern in the player's responses, otherwise plays
    if games % 2 == 0:                               # a random choice.
        if r_times > p_times and r_times > s_times:
            return 1
        elif p_times > r_times and p_times > s_times:
            return 2
        elif s_times > r_times and s_times > p_times:
            return 0
        else:
            return random.randint(0, len(possible_outcomes) - 1)
    else:
        return random.randint(0, len(possible_outcomes) - 1)


# Define global variables, lists, dictionaries
possible_outcomes = ['r', 'p', 's']
printed_outcomes = ['rock', 'paper', 'scissors']
result = ''
wins = 0
ties = 0
losses = 0

times_played_r = 0
times_played_p = 0
times_played_s = 0

games_played = 0
win_percent = 0.0

# Main program - program logic or algorithm
start = input("When you are ready to begin, press enter! ")
playing = True
print("If at any time you wish to quit, type 'q'.\n")
while playing:  # Continuous loop to be broken by player - they don't want to play anymore.
    computer_choice = what_to_play(times_played_r, times_played_p, times_played_s, games_played)
    user_choice = input("Rock! Paper! Scissors! ").lower()
    user_choice += ' '
    if user_choice == 'q ':
        if games_played <= 0:
            games_played = 1
        playing = False
        win_percent = str(wins / games_played * 100)
        print("\nOh... Nice playing against you!\n")
        print("Wins: " + str(wins) + ", Losses: " + str(losses) + ", Ties: " + str(ties))
        print("Win Percentage: " + win_percent[:5] + '%')
    elif user_choice[0] in possible_outcomes:  # Counts the times each choice, rock, paper, or scissors, was played.
        if user_choice[0] == 'r':
            times_played_r += 1
        elif user_choice[0] == 'p':
            times_played_p += 1
        else:
            times_played_s += 1
        user_choice = possible_outcomes.index(user_choice[0])
        print("I choose " + printed_outcomes[computer_choice] + '.')
        result = who_won(user_choice, computer_choice)
        if result == 'W':  # Counts up the wins, losses, and ties based on the 'who_won' function result.
            wins += 1
        elif result == 'L':
            losses += 1
        else:
            ties += 1
        print()
        games_played += 1
    else:
        print("Next time give a valid input.\n ")

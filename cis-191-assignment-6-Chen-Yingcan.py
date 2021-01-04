# CIS191 Assignment 6 Yingcan Chen
# ID: 29849802
# 2020 Oct 11
# Format tested in Terminal
# Player Names
red_team_players = [ "Einstein", "Bond 007", "Spock", "N00B", "Solid Snake", "Mysterious Pineapple", "Scorpion", "Aladdin", "Stormy", "Easy Target", "Optimus Prime" ]
green_team_players = [ "Cupcake", "Boss Level 3000", "Pudding", "Watermelon", "Ham Sandwich", "Hot Sauce", "Jelly Bean", "Rambo", "Ron Weasley", "Sherlock" ]

# Team Scores for Games 1-8
red_team_scores = [ 249815, 261790, 401110, 287185, 495795, "Not Available", "Not Available", "Not Available" ]
green_team_scores = [ 393950, 401875, 259365, 337580, 387310, "Not Available", "Not Available", "Not Available" ]

# Red Player Scores for Games 1-8
red_player_scores_game_1 = [ 35661, 14230, 10558,  5617, 24826, 27794, 15880, 34050, 29762, 22512, 28926 ]
red_player_scores_game_2 = [ 37647, 18989,  3553, 52322, 24309, 30787, 31014,  6888, 11023, 40542,  4717 ]
red_player_scores_game_3 = [ 79180, 73057, 32997, 22423, 18956, 27327,  2391, 31673, 63695, 38808, 10604 ]
red_player_scores_game_4 = [ 28874, 20313, 30203, 35622, 27757, 30733, 35770, 19394, 10552, 29682, 18285 ]
red_player_scores_game_5 = [ 71846,  5401, 73934, 19881, 11642, 53273, 10690, 73436, 44311, 74439, 56942 ]
red_player_scores_game_6 = [  8214, 43435, 82115, 61043, 83126, 42722, 39179, 52228,  9665, 18600, 11923 ]
red_player_scores_game_7 = [ 13901, 16779,  8963,  9597, 32825, 12855, 21677, 14482, 28692, 20104, 12960 ]
red_player_scores_game_8 = [ 27018,  6975, 27687,  3296, 13189, 26900, 15055, 16067,  6264,   865, 37624 ]

# Green Player Scores for Games 1-8
green_player_scores_game_1 = [ 36180, 16592, 14065, 82496, 28658, 95382, 47472, 25553,  7818, 39735 ]
green_player_scores_game_2 = [ 21052, 39375, 10764, 56320, 60872, 41596,  1253, 52714, 73704, 44225 ]
green_player_scores_game_3 = [  4619, 54683, 55840, 30296,  3298, 32484, 46848,  9964,  3835, 17499 ]
green_player_scores_game_4 = [ 30532, 56276, 31169, 29752, 39882, 43932, 22620, 39264,  7517, 36637 ]
green_player_scores_game_5 = [ 22529, 20498, 49719, 65871,  1963, 41934, 35550, 29307, 65899, 54040 ]
green_player_scores_game_6 = [ 59778, 16995, 13353, 26358, 11835, 22476, 10103, 64042, 14581, 66208 ]
green_player_scores_game_7 = [  8901, 74062, 75375, 22299, 35679, 48364, 81189, 41643, 14674,  1728 ]
green_player_scores_game_8 = [ 31655, 28003, 46976, 60048,  9958, 61574, 59716,  9282, 15591,  5826 ]

# Problem 6.1: Team Roster Dashboard Prototype

# find out the number of players on the Green team and store the value
num_green_players = len(green_team_players)
# find out the number of games played and store the value, the length of the list "team scores" will be the numbers of game played
num_games_played = len(green_team_scores)

# print the output
print("Problem 6.1: Team Roster Dashboard Prototype\n--------------------------------------------\n\n")
print("The Green Team has {} players.\nThe Green Team has played {} games.\n\n".format(num_green_players, num_games_played))

print("Player \t Name\n\n------\t ----\n")
# set up a counter for the while loop
counter = 0
# Use while loop to dynamically print out the result
while counter <= num_green_players-1 :
    print("{}.\t {}".format(counter+1, green_team_players[counter]))
    counter += 1



# Problem 6.2: Game Summary Dashboard Prototype A
# Print an empty line to seperate the result
print()
# initalize variable to find out green team score for Game 6
greenTeamScore6 = 0
# Use for loop to calculate tem score for Game 6
for i in green_player_scores_game_6:
    greenTeamScore6 = greenTeamScore6 + i

# initalize variable to find out green team score for Game 7
greenTeamScore7 = 0
# Use for loop to calculate tem score for Game 7
for i in green_player_scores_game_7:
    greenTeamScore7 = greenTeamScore7 + i

# initalize variable to find out green team score for Game 8
greenTeamScore8 = 0
# Use for loop to calculate tem score for Game 8
for i in green_player_scores_game_8:
    greenTeamScore8 = greenTeamScore8 + i

# Replace "Not Available" with calculated score values
green_team_scores[5] = greenTeamScore6
green_team_scores[6] = greenTeamScore7
green_team_scores[7] = greenTeamScore8

# initalize variable to find out red team score for Game 6
redTeamScore6 = 0
# Use for loop to calculate team score for Game 6
for i in red_player_scores_game_6:
    redTeamScore6 = redTeamScore6 + i

# initialize variable to find out red team score for Game 7
redTeamScore7 = 0
# Use for loop to calculate team score for Game 7
for i in red_player_scores_game_7:
    redTeamScore7 = redTeamScore7 + i

# initialize variable to find out red team score for Game 8
redTeamScore8 = 0
# Use for loop to calculate team score for Game 8
for i in red_player_scores_game_8:
    redTeamScore8 = redTeamScore8 + i

# Replace "Not Available" with calculated score values
red_team_scores[5] = redTeamScore6
red_team_scores[6] = redTeamScore7
red_team_scores[7] = redTeamScore8

# Print the result
print("Problem 6.2: Game Summary Dashboard Prototype A\n-----------------------------------------------\n")
print("Game\tGreen\t\tRed\n----\t-----\t\t---")
for i in range(num_games_played):
    print("{}\t{:,}\t\t{:,}".format(i+1, green_team_scores[i], red_team_scores[i]))




# Problem 6.3: Game Summary Dashboard Prototype B
# Print an empty line to separate the Problem
print()
# Initialize empty list
games_winners = []
games_total_points = []

# Use for loop to go through every element in the list, if Green them has higher score, record, if Red team has higher score, Record
for i in range(num_games_played):
    if green_team_scores[i] > red_team_scores[i]:
        games_winners.append("Green")
    else:
        games_winners.append("Red")
    games_total_points.append(green_team_scores[i]+red_team_scores[i])

# Print the result for 6.3
print("Problem 6.3: Game Summary Dashboard Prototype B\n-----------------------------------------------\n")
print("Game\tGreen\t\tRed\t\tTotal\t\t\tWinner\n----\t-----\t\t---\t\t-----\t\t\t------")
# Use for loop to print output dynamically
for i in range(num_games_played):
    print("{}\t{:,}\t\t{:,}\t\t{:,}\t\t\t{}".format(i+1, green_team_scores[i], red_team_scores[i], games_total_points[i], games_winners[i]))




# Problem 6.4: Green Team Post-Game Dashboard Prototype A
# print an empty line to separate problems
print()
# Use for loop to find out the number of games won by Green team
# initialize variable to count the number of wins by green team
num_games_won_by_green_team = 0
for i in games_winners:
    if i == "Green":
        num_games_won_by_green_team += 1
green_team_win_percentage = num_games_won_by_green_team / num_games_played * 100

# Using For loop to calculate the Average Green Team score per game
greenTeamTotalScore = 0
for scores in green_team_scores:
    greenTeamTotalScore += scores
green_team_average_score = greenTeamTotalScore / num_games_played
green_player_total_points = []
# Using for loop to find out total individual points for each Green Team player across all games
for i in range(num_green_players):
    current_player_total_points = 0
    # for each player, calculate his total score by adding his score in each game together
    current_player_total_points = green_player_scores_game_1[i] + green_player_scores_game_2[i] + \
                                  green_player_scores_game_3[i] + green_player_scores_game_4[i] + \
                                  green_player_scores_game_5[i] + green_player_scores_game_6[i] + green_player_scores_game_7[i] + green_player_scores_game_8[i]
    green_player_total_points.append(current_player_total_points)
# Print result for Problem 6.4
print("Problem 6.4: Green Team Post-Game Dashboard Prototype A\n-------------------------------------------------------\n")

print("Number of players: \t\t{}\nGames won:\t\t\t{} of {}({}%)\nAverage team score:\t\t{:,.0f} points".format(num_green_players, num_games_won_by_green_team, num_games_played, green_team_win_percentage, green_team_average_score))





# Problem 6.5: Green Team Post-Game Dashboard Prototype B
# print an empty line to separate the two problems
print()
# create empty list
all_stars = []
for i in range(len(green_player_total_points)):
    if green_player_total_points[i]/num_games_played >= 35000:
        all_stars.append(green_team_players[i])
# Initialize variable "mvp_name" to be an empty string
mvp_name = ""
# Initialize variable "mvp_total_points" to be zero
mvp_total_points = 0
# Using for loop to go through the list "green_player_total_points, \
# and find out the greatest scores and assign the person to be MVP
for i in range(len(green_player_total_points)):
    if green_player_total_points[i] > mvp_total_points:
        mvp_total_points = green_player_total_points[i]
        mvp_name = green_team_players[i]
# using for loop to remove the MVP name in the all_stars list
for names in all_stars:
    if names == mvp_name:
        all_stars.remove(names)

# Print 6.5 result

# print an empty line to sepreateate the two problems
print("Problem 6.5: Green Team Post-Game Dashboard Prototype B\n-------------------------------------------------------\n")

print("Number of players: \t\t{}\nGames won:\t\t\t{} of {}({}%)\nAverage team score:\t\t{:,.0f} points\nAll-Stars:\t\t\t{}\nMVP:\t\t\t\t{}({:,} total points)".format(num_green_players, num_games_won_by_green_team, num_games_played, green_team_win_percentage, green_team_average_score, ', '.join(all_stars), mvp_name, mvp_total_points))




# Problem 6.6: Player Summary Dashboard Prototype
# print an empty line to separate the problems
print()
# Calculate the total number of points scored by the Green Team across all games
green_team_total_score = 0
for scores in green_team_scores:
    green_team_total_score += scores
# Create a list called "green_team_score_data" to store score data for every single player for easier access
green_team_score_data = [green_player_scores_game_1, green_player_scores_game_2, \
                         green_player_scores_game_3, green_player_scores_game_4, green_player_scores_game_5, green_player_scores_game_6, green_player_scores_game_7, green_player_scores_game_8]
# Calculate and print the result dynamically using for loop
print("Problem 6.6: Player Summary Dashboard Prototype\n-----------------------------------------------\n")
for i in range(num_green_players):
    current_player_highest_score = 0  # initialize the variable "current_player_highest_score to be zero, it will be assigned a new value when a  new higher score is found until the highest
    current_player_lowest_score = 1000000  # initalize the variable "current_player_lowest_score" to be 1000000, it will be replaced every time a lower score is found in the for loop, until reach the lowest
    current_player_total_points = 0  # initialize variable "current_player_total_points" to be zero
    current_player_best_game = 0  # initialize variable "current_player_best_game" to be zero
    current_player_worst_game = 0  # initialize variable " current_player_worst_game" to be zero
    for j in range(num_games_played):
        # when a new higher score is found, using if statement to update the highest score and best game, until optimal is reached
        if green_team_score_data[j][i] > current_player_highest_score:
            current_player_highest_score = green_team_score_data[j][i]
            current_player_best_game = j+1  # update best game
        # When a new lower score is found, using if statement to update the lowest score and worst game, until optimal is reached
        if green_team_score_data[j][i] < current_player_lowest_score:
            current_player_lowest_score = green_team_score_data[j][i]
            current_player_worst_game = j+1  # update worst game
        current_player_total_points += green_team_score_data[j][i]  # Calculate the total score in the loop
    current_player_average_score = current_player_total_points/num_games_played  # Calculate current player average score
    current_player_total_points_percentage = current_player_total_points/green_team_total_score*100
    # For every player, print out the summary information
    print("#{}. {}\n\nBest Score: {:,}\t\tWorst Score: {:,}\t\tAverage Score:{:,.0f}\nBest Game: Game {} \t\tWorst Game: Game {}\nTotal Points: {:,} of {:,} ({:.2f}%)\n".format(i+1, green_team_players[i], current_player_highest_score, current_player_lowest_score, current_player_average_score, current_player_best_game, current_player_worst_game, current_player_total_points, green_team_total_score, current_player_total_points_percentage))
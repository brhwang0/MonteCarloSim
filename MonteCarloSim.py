import random
import matplotlib.pyplot as plt


# Player funds
totalFunds = 100
# How much the player wagers each bet
wager = 10
# Times the player plays
totalPlays = 20


# A 100-sided dice is rolled
# House wins if number is 1-51, Player wins if number is 52-100
# House has a 51% chance of winning, Player has a 49% chance
def rollDice():

    dice = random.randint(1, 100)

    if dice <= 51:
        return False
    else:
        return True

def play(totalFunds, wager, totalPlays):

    playNum = []
    funds = []

    play = 1

    while play < totalPlays:
        # Player wins
        if rollDice():
            totalFunds += wager
            playNum.append(play)
            funds.append(totalFunds)
        # House wins
        else:
            totalFunds -= wager
            playNum.append(play)
            funds.append(totalFunds)

        play += 1

    plt.plot(playNum, funds)
    final_funds.append(funds[-1])
    return(final_funds)


# Main
scenario_num = 1
final_funds = []

# Simulate multiple scenarios
while scenario_num < 100:
    ending_fund = play(totalFunds, wager, totalPlays)
    scenario_num += 1

plt.xlabel("Number of Bets")
plt.ylabel('Player Money')
plt.show()

print("The player started the game with " + str(totalFunds) + " and ends with $" + str(sum(ending_fund)/len(ending_fund)))

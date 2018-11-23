import argparse
from random import randint

# Set up parser for args
parser = argparse.ArgumentParser(description='Takes in parameters for testing a random dungeon')
parser.add_argument('thresholds', type=int, nargs=4,
                    help='thresholds on a d20 for the appearance of [monsters, loot, dressing, hazards]')
parser.add_argument('rooms', type=int, nargs=1, help='number of rooms to roll')

args = parser.parse_args()


# def roll functions
def rollOnTable(table):
    dieValue = randint(1, 20)
    if dieValue != 20:
        return table[dieValue-1][0:(len(table[dieValue-1])-1)]
    else:
        return rollOnTable(table) + ', ' + rollOnTable(table)


def roll(dc):
    dieValue = randint(1, 20)
    ret = dieValue > dc
    return ret


# Load tables
tableFiles = ['monsters', 'loot', 'dressing', 'hazards']
tables = [[], [], [], []]

for t in range(0, 4):
    fileName = 'data/' + tableFiles[t] + '.txt'
    file = open(fileName, "r")
    for line in file:
        tables[t].append(line)

# for number of rooms
for r in range(0,args.rooms[0]):
    print("Room #" + str(r+1) + ":")
    print("========")
    for i in range(0, 4):
        if roll(args.thresholds[i]):
            print(tableFiles[i] + ': ' + rollOnTable(tables[i]))
        else:
            print("No " + tableFiles[i])
    print("")

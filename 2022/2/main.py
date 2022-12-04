from enum import Enum, IntEnum

from numpy import mat

class Sign(IntEnum):
    ROCK = 1
    PAPER = 2
    SCISSOR = 3

class MatchOutcome(Enum):
    WIN = 1
    LOSE = 2
    DRAW = 3

def get_input(path):
    with open(path) as f:
        lines = f.readlines()
        return lines


def identifyHandsign(char):
    if(char == 'A' or char == 'X'):
        return Sign.ROCK
    if(char == 'B' or char == 'Y'):
        return Sign.PAPER
    if(char == 'C' or char == 'Z'):
        return Sign.SCISSOR

def evaluateMatch(sign1, sign2):
    if(sign1 == sign2):
        return MatchOutcome.DRAW
    if(sign1 == Sign.ROCK):
        if(sign2 == Sign.PAPER):
            return MatchOutcome.LOSE
        if(sign2 == Sign.SCISSOR):
            return MatchOutcome.WIN
    if(sign1 == Sign.PAPER):
        if(sign2 == Sign.SCISSOR):
            return MatchOutcome.LOSE
        if(sign2 == Sign.ROCK):
            return MatchOutcome.WIN
    if(sign1 == Sign.SCISSOR):
        if(sign2 == Sign.ROCK):
            return MatchOutcome.LOSE
        if(sign2 == Sign.PAPER):
            return MatchOutcome.WIN


lines = get_input('./2022/2/input.txt')

total = 0
for line in lines:
    
    enemyHandsign = identifyHandsign(line[0])
    playerHandsign = identifyHandsign(line[2])
    matchResult = evaluateMatch(playerHandsign, enemyHandsign)
    print("______________")
    print("enemyHandsign: ", enemyHandsign)
    print("playerHandsign: ", playerHandsign)
    print("matchResult: ", matchResult)
    scoreAddition = 0
    if(matchResult == MatchOutcome.WIN):
        scoreAddition = 6 + int(playerHandsign)
    elif(matchResult == MatchOutcome.DRAW):
        scoreAddition = 3 + int(playerHandsign)
    else:
        scoreAddition = int(playerHandsign)
    print(scoreAddition)
    total = total + scoreAddition

print("Total: ", total)
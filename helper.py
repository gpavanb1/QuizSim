import numpy as np
from random import random

#### 
# MISC
####

def getBool(prob):
    return (random() <= prob)


#### 
# POUNCE RELATED
####

def knowAnswer(strength):
    return [getBool(s) for s in strength]

def willPounce(dare):
    return [getBool(s) for s in dare]

def pounceScore(pList, cList, POUNCE_RIGHT, POUNCE_WRONG):
    res = []
    for i, p in enumerate(pList):
        isCorrect = cList[i]
        if p == True:
            if isCorrect:
                res.append(POUNCE_RIGHT)
            else:
                res.append(POUNCE_WRONG)
        else:
            res.append(0.0)

    return np.array(res)


#### 
# BOUNCE RELATED
####

def checkBounce(questionAt, pounceList, knowList, \
BOUNCE_RIGHT, BOUNCE_TYPE):
    numTeams = len(pounceList)
    teams = range(0, numTeams)
    bounceScore = [0.0] * numTeams

    q = questionAt
    doneRound = False
    while not doneRound:
        # If team knows answer
        if knowList[q] == True:
            # Team didn't pounce
            # Even if direct team pounces, it gets it now
            # as it is False on pounceList
            if pounceList[q] == False:
                bounceScore[q] = BOUNCE_RIGHT
                # Direct to next team
                questionAt = (q + 1) % numTeams
                break
        # Moves on to next team
        q = int((q + 1) % numTeams)

        # Back to original team if no one gets it
        if not doneRound and q == questionAt:
            # Change questionAt based on bounce mode
            if BOUNCE_TYPE == 'Bengaluru':
                questionAt = int((questionAt + 1) % numTeams)
            break

    return np.array(bounceScore), questionAt

    
#### 
# MAIN HELPERS
####

def checkPounce(questionAt, POUNCE_DARE, TEAM_STRENGTH, \
POUNCE_RIGHT, POUNCE_WRONG):
    # Get who got correct
    pounceList = willPounce(POUNCE_DARE)
    # Set direct team to False
    pounceList[questionAt] = False

    correctList = knowAnswer(TEAM_STRENGTH)
    scoreList = pounceScore(pounceList, correctList, \
    POUNCE_RIGHT, POUNCE_WRONG)
    return scoreList, pounceList
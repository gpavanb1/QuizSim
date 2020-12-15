# TODO : Part points
import numpy as np
from quizsim.helper import checkBounce, checkPounce, knowAnswer

def runQuiz(NUM_QUESTIONS=30,\
TEAM_STRENGTH=[1.0, 0.0], \
POUNCE_DARE=[1.0, 0.0], \
CAN_POUNCE=True, \
BOUNCE_TYPE='Bengaluru', \
# Points
POUNCE_RIGHT = 15, \
POUNCE_WRONG = -10, \
BOUNCE_RIGHT = 10):
    # Check team sizes are consistent
    numTeams = len(TEAM_STRENGTH)
    try:
        if len(POUNCE_DARE) != numTeams:
            raise AttributeError('POUNCE_DARE and TEAM_STRENGTH \
            must be of same size')

        if numTeams == 0:
            raise AttributeError('No teams specified')    


        # Start quiz
        questionAt = 0   
        scores = np.zeros(numTeams)
        for q in range(NUM_QUESTIONS):
            knowList = knowAnswer(TEAM_STRENGTH)
            if CAN_POUNCE:
                qPounceScore, pounceList = checkPounce(questionAt, POUNCE_DARE, \
                TEAM_STRENGTH, POUNCE_RIGHT, POUNCE_WRONG)
            else:
                qPounceScore = [0.0] * numTeams
                pounceList = [False] * numTeams
            qBounceScore, questionAt = checkBounce(questionAt, \
            pounceList, knowList, BOUNCE_RIGHT, BOUNCE_TYPE)
            scores += qBounceScore + qPounceScore

        return scores
    
    except Exception as e:
        print(e)
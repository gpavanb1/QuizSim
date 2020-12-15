import unittest
import numpy as np
from quizsim.main import runQuiz

class TestRunQuiz(unittest.TestCase):
    def test_wrong_dim(self):
        try:
            runQuiz(30, [0.0], [1.0, 0.0])
        except:
            self.assertTrue()

    def test_null(self):
        try:
            runQuiz(30, [], [])
        except:
            self.assertTrue()


    def test_stupid_teams_chennai(self):
        CAN_POUNCE = True
        BOUNCE_TYPE = 'Chennai'
        POUNCE_DARE = [1.0, 1.0]
        TEAM_STRENGTH = [0.0, 0.0]
        output = runQuiz(30, TEAM_STRENGTH, \
        POUNCE_DARE, CAN_POUNCE, BOUNCE_TYPE)
        # Q1 - Team 1 direct, misses it. Team 2 pounced and negs
        # Chennai bounce so Team 1 direct again and so on
        expected = np.array([0.0, -300.0])
        self.assertTrue(np.alltrue(output == expected))

    def test_stupid_teams_bengaluru(self):
        CAN_POUNCE = True
        BOUNCE_TYPE = 'Bengaluru'
        POUNCE_DARE = [1.0, 1.0]
        TEAM_STRENGTH = [0.0, 0.0]
        output = runQuiz(30, TEAM_STRENGTH, \
        POUNCE_DARE, CAN_POUNCE, BOUNCE_TYPE)
        # Q1 - Team 1 direct, misses it. Team 2 pounced and negs
        # Team 2 direct now
        # Q2 - Team 1 pounces and negs. Team 2 misses it.
        # Team 1 now and so on
        expected = np.array([-150.0, -150.0])
        self.assertTrue(np.alltrue(output == expected))

    def test_only_pounce_chennai(self):
        CAN_POUNCE = True
        BOUNCE_TYPE = 'Chennai'
        POUNCE_DARE = [0.0, 1.0]
        TEAM_STRENGTH = [0.0, 1.0]
        output = runQuiz(30, TEAM_STRENGTH, \
        POUNCE_DARE, CAN_POUNCE, BOUNCE_TYPE)
        # Q1 - Team 1 direct, Team 2 gets on pounce, Team 1 misses, 
        # Now Team 1 direct and so on
        expected = np.array([0.0, 450.0])
        self.assertTrue(np.alltrue(output == expected))

    def test_only_pounce_bengaluru(self):
        CAN_POUNCE = True
        BOUNCE_TYPE = 'Bengaluru'
        POUNCE_DARE = [0.0, 1.0]
        TEAM_STRENGTH = [0.0, 1.0]
        output = runQuiz(30, TEAM_STRENGTH, \
        POUNCE_DARE, CAN_POUNCE, BOUNCE_TYPE)
        # Q1 - Team 1 direct, Team 2 gets on pounce, Team 1 misses, 
        # Now Team 2 direct and so on
        # Q2 - Team 2 gets on direct, now to Team 1 and so on
        expected = np.array([0.0, 375.0])
        self.assertTrue(np.alltrue(output == expected))

    def test_only_bounce_chennai(self):
        CAN_POUNCE = False
        BOUNCE_TYPE = 'Chennai'
        POUNCE_DARE = [0.0, 1.0]
        TEAM_STRENGTH = [0.0, 1.0]
        output = runQuiz(30, TEAM_STRENGTH, \
        POUNCE_DARE, CAN_POUNCE, BOUNCE_TYPE)
        # Q1 - Team 2 gets on bounce, now Team 1 direct and so on
        expected = np.array([0.0, 300.0])
        self.assertTrue(np.alltrue(output == expected))

    def test_only_bounce_bengaluru(self):
        CAN_POUNCE = False
        BOUNCE_TYPE = 'Bengaluru'
        POUNCE_DARE = [0.0, 1.0]
        TEAM_STRENGTH = [0.0, 1.0]
        output = runQuiz(30, TEAM_STRENGTH, \
        POUNCE_DARE, CAN_POUNCE, BOUNCE_TYPE)
       # Q1 - Team 2 gets on bounce, now Team 1 direct and so on
        expected = np.array([0.0, 300.0])
        self.assertTrue(np.alltrue(output == expected))

    def test_only_bounce_bengaluru_team1(self):
        CAN_POUNCE = False
        BOUNCE_TYPE = 'Bengaluru'
        POUNCE_DARE = [1.0, 0.0]
        TEAM_STRENGTH = [1.0, 0.0]
        output = runQuiz(30, TEAM_STRENGTH, \
        POUNCE_DARE, CAN_POUNCE, BOUNCE_TYPE)
       # Q1 - Team 1 gets on direct, now Team 2 direct
       # Q2 - Team 2 misses on direct, Team 1 gets on bounce, 
       # now Team 2 direct and so on
        expected = np.array([300.0, 0.0])
        self.assertTrue(np.alltrue(output == expected))

    def test_can_pounce_no_depend_on_dare(self):
        POUNCE_DARE = [0.0, 1.0]
        o1 = runQuiz(POUNCE_DARE=POUNCE_DARE, CAN_POUNCE=False)
        POUNCE_DARE = [0.0, 0.0]
        o2 = runQuiz(POUNCE_DARE=POUNCE_DARE, CAN_POUNCE=False)
        self.assertTrue(np.alltrue(o1 == o2))

if __name__ == '__main__':
    unittest.main()
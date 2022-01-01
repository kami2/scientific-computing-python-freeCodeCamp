import copy
import random


class Hat:


    def __init__(self, **kwargs):
        contents = []
        self.contents = contents
        for key, value in kwargs.items():
            for amountOfBall in range(value):
                self.contents.append(key)



    def draw(self, numberToDraw):
        if numberToDraw >= len(self.contents):
            return self.contents
        else:
            i = 0
            drawnBalls = []
            while i < numberToDraw:
                drawBall = random.choice(self.contents)
                drawnBalls.append(drawBall)
                self.contents.remove(drawBall)
                i += 1

            return drawnBalls



def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    expectedBallsList = []

    for key, value in expected_balls.items():
        for amountOfBall in range(value):
            expectedBallsList.append(key)

    i = 0
    foundMatch = 0

    while i < num_experiments:
        copyHat = copy.deepcopy(hat)
        drawnBalls = copyHat.draw(num_balls_drawn)
        drawnBalls.sort()

        commonElements = list(set(expectedBallsList) & set(drawnBalls))
        commonElements.sort()

        if num_balls_drawn > len(hat.contents):
            probability = 1.0
            return probability

        ballCheck = 0
        ik = 0
        for ball in commonElements:
            expectedBallAmount =  expectedBallsList.count(ball)
            drawnBallAmount = drawnBalls.count(ball)
            if drawnBallAmount == expectedBallAmount:
                ballCheck += 1
            if (ballCheck / len(commonElements)) == 1:
                foundMatch += 1


        i += 1

    probability = (foundMatch * len(commonElements)) / num_experiments

    return probability



hat = Hat(blue=3,red=2,green=6)
probability = experiment(hat=hat,
                  expected_balls={"blue":2,"green":1},
                  num_balls_drawn=4,
                  num_experiments=1000)
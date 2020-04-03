"""
    Given a bag with 100 balls simulate choosing the a ball
    randomly each time and discard the choosen ball. 
"""
from random import randint


def pick_balls(balls, n):
    """
        
    """

    right = n - 1

    for _ in range(right):

        random_index = randint(0, right)
        # swap them 
        print(balls[random_index])
        balls[random_index], balls[right] = balls[right], balls[random_index]

        right -= 1

n = 100000
balls = list(range(1, n+1))
pick_balls(balls, n)



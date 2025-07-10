"""
Template - Compute and print powerball numbers.
"""

import random

###################################################
# Powerball function
# Student should enter function on the next lines.
def powerball():
    one = random.randrange(1,60)
    two = random.randrange(1,60)
    three = random.randrange(1,60)
    four = random.randrange(1,60)
    five = random.randrange(1,60)
    six = random.randrange(1,36)
    
    print(f"today's no. are {one} {two} {three} {four} and {five}. The powerball number is {six}.")


    
###################################################
# Tests
# Student should not change this code.
    
powerball()
powerball()
powerball()
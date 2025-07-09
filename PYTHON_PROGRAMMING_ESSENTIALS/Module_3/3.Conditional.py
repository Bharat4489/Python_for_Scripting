"""
Demonstration of if statements.
"""

def greet(friend, money):
    """
    Greet people.  Say hi if they are your friend and give them
    $20 if you have enough money.
    """
    if friend:
        print("Hi!")
    else:
        print("Hello! not a friend!")
    if money > 20:
        money = money - 20

    return money


money = 24

money = greet(False, money)
print("Money:", money)
print()

money = greet(True, money)
print("Money:", money)
print()

money = greet(True, money)
print("Money:", money)
print()

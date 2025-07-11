"""
Template - Echo a string multiple times to the console
"""

def echo(call, repeats):
    """
    Echo the string call to the console repeats number of time
    Each echo should be on a separate line
    """

    #BOTH OF THE BELOW METHODS WORK
    #print(((call + "\n") * repeats).rstrip())
    # Using a loop to print the call multiple times
    # This avoids the need for rstrip() since each print adds a new line
    # and we control the number of repetitions directly.
    #print(((call+ "\n")*repeats).rstrip())
    for _ in range(repeats):
        print(call)


# Tests
echo("Hello", 5)
echo("Goodbye", 3)

# Output
#Hello
#Hello
#Hello
#Hello
#Hello
#Goodbye
#Goodbye
#Goodbye
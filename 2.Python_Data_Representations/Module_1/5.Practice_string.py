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

print("\n###OVER###\n")

"""
Template - Function that tests for substring
"""


def is_substring(example_string, test_string):
    """
    Function that returns True if test_string
    is a substring of example_string and False otherwise
    """
    return test_string in example_string
    

# Tests

example_string = "It's just a flesh wound."

print(is_substring(example_string, "just"))
print(is_substring(example_string, "flesh wound"))
print(is_substring(example_string, "piddog"))
print(is_substring(example_string, "it's"))
print(is_substring(example_string, "It's"))

print("\n###OVER###\n")


"""
Template - Function that uses format to create a nametag
"""


def make_nametag(first_name, topic):
    """
    Given two strings first_name and topic,
    return a string of the form ""Hi! My name 
    is XXX. This lecture covers YYY." where
    XXX and YYY are first_name and topic.
    """
    
    # enter code here
    return "Hi! My name is {}. This lecture covers {}.".format(first_name, topic)
    # Alternatively_1, 
    #   using f-string
    #   return f"Hi! My name is {first_name}. This lecture covers {topic}."
    #I'M GOING TO REMEMBER THE ABOVE AY ONLY
    #Alternative_2
    #   template = "Hi! My name is {0}. This lecture covers {1}."
    #   return template.format(first_name, topic)    
# Tests

print(make_nametag("Scott", "Python"))
print(make_nametag("Joe", "games"))
print(make_nametag("John", "programming tips"))

print("\n###OVER###\n")
"""
Template - Function that swaps and capitalizes first and last names
"""


def name_swap(name_string):
    """
    Given the string name string of the form "first last", return 
    the string "Last First" where both names are now capitalized
    """
    
    (first, last) = name_string.split(" ")
    return last.capitalize() + " " + first.capitalize()
    
# Tests

print(name_swap("joe warren"))
print(name_swap("scott rixner"))
print(name_swap("john greiner"))

print("\n###OVER###\n")
"""
Template - counting number of vowels in a string
"""
def count_vowels(string):
    vowel = "aeiou"
    count=0
    for chars in string:
        if chars in vowel:
            count=count+1
    return count


print(count_vowels("aaassseefffgggiiijjjoOOkkkuuuu"))
print(count_vowels("aovvouOucvicIIOveeOIclOeuvvauouuvciOIsle"))

print("\n###OVER###\n")
"""
Template - replacing characters in a string
"""
def demystify(string):
    count=""
    for char in string:
        if char == "l":
            count=count+"a"
        else:
            count=count+"b"
    return count


print(demystify("lll111l1l1l1111lll"))
print(demystify("111l1l11l11lll1lll1lll11111ll11l1ll1l111"))


    
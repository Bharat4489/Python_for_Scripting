"""
Example of program that use a loop to compute the minimum number in a non-empty list
"""
def ne_list_minimum(numbers):
    """
    Compute the minimum of a non-empty list of numbers - contains an error
    """
    
    min_num = numbers[0]
    for num in numbers[1 :]:
        if num < min_num:
            min_num = num  # Set "Run to cursor" on this line
    return min_num

def run_tests():
    """
    Run an example using list_minimum
    """
    print(ne_list_minimum([1.0]))
    print(ne_list_minimum([-1.0, -2.0, 3.3]))
    print(ne_list_minimum([4.6, 5.9, 2.1, 5.7, 1.1, 8.3]))

run_tests()

print("================")
"""
Template- Create a list of the first six primes and print the 2nd, 4th, and 6th
"""
def create_prime():
    prime_list = list()
    
    for i in range(2,100):
        is_prime = True
        for j in prime_list:
            if i%j == 0:
                is_prime = False
                break
        if is_prime:
            prime_list.append(i)

    return prime_list

print("prime_list")
list_of_prime = create_prime()
print (list_of_prime[1], list_of_prime[3], list_of_prime[5])


print("================")
"""
Template - Create a list formed by the first and last items of example_list
"""

example_list = [2, 3, 5, 7, 11, 13]

firstlast_list = example_list[0],example_list[-1]
print(firstlast_list)

print("================")
# Initial list
list1 = [2, 3, 5, 7, 11, 13]
print("list1:", list1)
list2 = list1
#ABOVE WE HAVE CREATED A REFERENCE TO THE SAME LIST
# Now we modify list2
list2[0] = 1
# This will also change list1 because list2 is a reference to the same list
print("list1:", list1)
print("list2:", list2)
#TO CREATE A COPY OF THE LIST, WE CAN USE THE list() FUNCTION
list3 = list(list1)
# Now we modify list3
list3[0] = 0
# This will not change list1 or list2 because list3 is a separate copy
print("list1:", list1)
print("list2:", list2)
print("list3:", list3)

def strange_sum(numlist):
    sum = 0
    for i in range(len(numlist)):
        if numlist[i]%3!=0:
            sum+=numlist[i]
    return sum
print(strange_sum([1, 2, 3, 4, 5, 1, 2, 3, 4, 5]))
print(strange_sum(list(range(123)) + list(range(77))))
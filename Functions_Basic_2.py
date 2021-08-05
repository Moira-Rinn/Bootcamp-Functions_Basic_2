# 1. Countdown - Create a function that accepts a number as an input. Return a new list that counts down by one, from the number (as the 0th element) down to 0 (as the last element).

def countDown(num):
    lst = [num]
    for x in range(num):
        num -= 1
        lst.append(num)
    return lst


print(countDown(5))

# 2. Print and Return - Create a function that will receive a list with two numbers. Print the first value and return the second.


def printReturn(lst):
    print(lst[0])
    return lst[1]


print(printReturn([1, 2]))

# 3. First Plus Length - Create a function that accepts a list and returns the sum of the first value in the list plus the list's length.


def fstPlusLen(lst):
    sum = lst[0] + len(lst)
    return sum


print(fstPlusLen([1, 2, 3, 4, 5]))

# 4. Values Greater than Second - Write a function that accepts a list and creates a new list containing only the values from the original list that are greater than its 2nd value. Print how many values this is and then return the new list. If the list has less than 2 elements, have the function return False.


def valGreaterThanSec(lst):
    newlst = []
    for x in range(len(lst)):
        if len(lst) < 2:
            return False
        if lst[1] < lst[x]:
            newlst.append(lst[x])
    print(len(newlst))
    return newlst


print(valGreaterThanSec([5, 2, 3, 2, 1, 4]))

# 5. This Length, That Value - Write a function that accepts two integers as parameters: size and value. The function should create and return a list whose length is equal to the given size, and whose values are all the given value.


def lenVal(size, val):
    lst = []
    for x in range(size):
        lst.append(val)
    return lst


print(lenVal(4, 7))

"""DESCRIPTION:
Take an array and remove every second element from the array. Always keep the first element and start removing with the
next element.

Example:
["Keep", "Remove", "Keep", "Remove", "Keep", ...] --> ["Keep", "Keep", "Keep", ...]"""
import math


def remove_every_other(my_list):
    indexes = slice(0, len(my_list), 2)
    # return my_list[::2]
    return my_list[indexes]


"""Your goal in this kata is to implement a difference function, which subtracts one list from another and returns the
 result.

It should remove all values from list a, which are present in list b keeping their order.

array_diff([1,2],[1]) == [2]
If a value is present in b, all of its occurrences must be removed from the other:

array_diff([1,2,2,2,3],[2]) == [1,3]"""


def array_diff(a, b):
    b_set = set(b)
    return [x for x in a if x not in b_set]


"""My friend John and I are members of the "Fat to Fit Club (FFC)". John is worried because each month a list with 
the weights of members is published and each month he is the last on the list which means he is the heaviest.

I am the one who establishes the list so I told him: "Don't worry any more, I will modify the order of the list". It was
 decided to attribute a "weight" to numbers. The weight of a number will be from now on the sum of its digits.

For example 99 will have "weight" 18, 100 will have "weight" 1 so in the list 100 will come before 99.

Given a string with the weights of FFC members in normal order can you give this string ordered by "weights" of these 
numbers?

Example:
"56 65 74 100 99 68 86 180 90" ordered by numbers weights becomes: 

"100 180 90 56 65 74 68 86 99"
When two numbers have the same "weight", let us class them as if they were strings (alphabetical ordering) and not 
numbers:

180 is before 90 since, having the same "weight" (9), it comes before as a string.

All numbers in the list are positive numbers and the list can be empty.

Notes
it may happen that the input string have leading, trailing whitespaces and more than a unique whitespace between two 
consecutive numbers
For C: The result is freed."""


def order_weight(weights):
    weights_list = sorted(weights.split(' '))
    sorted_weights = sorted(weights_list, key=foo)
    return " ".join(sorted_weights)


def foo(n):
    return sum([int(item) for item in n])


"""Write an algorithm that takes an array and moves all of the zeros to the end, preserving the order of the other 
elements.

move_zeros([1, 0, 1, 2, 0, 1, 3]) # returns [1, 1, 2, 1, 3, 0, 0]"""


def move_zeros(lst):
    count_zero = lst.count(0)
    result = [x for x in lst if x != 0]
    result.extend([0] * count_zero)
    return result


"""Write a program that will calculate the number of trailing zeros in a factorial of a given number.

N! = 1 * 2 * 3 *  ... * N

Be careful 1000! has 2568 digits...

For more info, see: http://mathworld.wolfram.com/Factorial.html

Examples
zeros(6) = 1
# 6! = 1 * 2 * 3 * 4 * 5 * 6 = 720 --> 1 trailing zero

zeros(12) = 2
# 12! = 479001600 --> 2 trailing zeros"""


def zeros(n):
    factorial = str(math.factorial(n))
    count_zero = factorial.count('0')
    return count_zero

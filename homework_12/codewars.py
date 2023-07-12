"""In this kata you will create a function that takes a list of non-negative integers
and strings and returns a new list with the strings filtered out."""
import statistics


def filter_list(lst):
    result = list(filter(lambda x: isinstance(x, int), lst))
    return result


assert filter_list([1, 2, 'a', 'b']) == [1, 2]
assert filter_list([1, 'a', 'b', 0, 15]) == [1, 0, 15]
assert filter_list([1, 2, 'aasf', '1', '123', 123]) == [1, 2, 123]

"""An isogram is a word that has no repeating letters, consecutive or non-consecutive. Implement a function that 
determines whether a string that contains only letters is an isogram. Assume the empty string is an isogram. 
Ignore letter case.

Example: (Input --> Output)

"Dermatoglyphics" --> true "aba" --> false "moOse" --> false (ignore letter case)"""


def is_isogram(word):
    return len(set(word.lower())) == len(word)


assert is_isogram("Dermatoglyphics") == True
assert is_isogram("isogram") == True
assert is_isogram("aba") == False
assert is_isogram("moOse") == False
assert is_isogram("isIsogram") == False
assert is_isogram("") == True


"""There was a test in your class and you passed it. Congratulations!
But you're an ambitious person. You want to know if you're better than the average student in your class.

You receive an array with your peers' test scores. Now calculate the average and compare your score!

Return True if you're better, else False!

Note:
Your points are not included in the array of your class's points. For calculating the average point you may add your 
point to the given array!"""


def better_than_average(class_points, your_points):
    mean_value = statistics.mean(class_points)
    return mean_value < your_points


assert better_than_average([2, 3], 5) == True
assert better_than_average([100, 40, 34, 57, 29, 72, 57, 88], 75) == True
assert better_than_average([12, 23, 34, 45, 56, 67, 78, 89, 90], 69) == True
assert better_than_average([41, 75, 72, 56, 80, 82, 81, 33], 50) == False
assert better_than_average([29, 55, 74, 60, 11, 90, 67, 28], 21) == False

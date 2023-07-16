"""You are going to be given a word. Your job is to return the middle character of the word. If the word's length is odd, return the middle character.
If the word's length is even, return the middle 2 characters.
https://www.codewars.com/kata/56747fd5cb988479af000028"""


def get_middle(word):
    index_middle = len(word) // 2
    if len(word) % 2 != 0:
        return word[index_middle]
    else:
        return word[index_middle - 1: index_middle + 1]


assert get_middle("test") == "es"
assert get_middle("testing") == "t"
assert get_middle("middle") == "dd"
assert get_middle("A") == "A"
assert get_middle("of") == "of"

"""Nathan loves cycling.

Because Nathan knows it is important to stay hydrated, he drinks 0.5 litres of water per hour of cycling.

You get given the time in hours and you need to return the number of litres Nathan will drink, rounded to the smallest value.
https://www.codewars.com/kata/582cb0224e56e068d800003c"""


def litres(time):
    return round(time // 2)


assert litres(2) == 1
assert litres(1.4) == 0
assert litres(12.3) == 6
assert litres(0.82) == 0
assert litres(1787) == 893

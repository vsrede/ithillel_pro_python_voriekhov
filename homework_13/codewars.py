"""Write a function to convert a name into initials. This kata strictly takes two words with one space in between them.

The output should be two capital letters with a dot separating them.

It should look like this:

Sam Harris => S.H

patrick feeney => P.F
https://www.codewars.com/kata/57eadb7ecd143f4c9c0000a3
"""


def abbrev_name(name):
    # name_list = name.split(' ')
    # result = (name_list[0][0] + '.' + name_list[1][0]).upper()
    first_name, last_name = name.split()
    result = f"{first_name[0].upper()}.{last_name[0].upper()}"
    return result


assert abbrev_name("Sam Harri") == "S.H"
assert abbrev_name("patrick feenan") == "P.F"
assert abbrev_name("Evan C") == "E.C"
assert abbrev_name("P Favuzzi") == "P.F"
assert abbrev_name("David Mendieta") == "D.M"


"""
Check to see if a string has the same amount of 'x's and 'o's. The method must return a boolean and be case insensitive.
 The string can contain any char.
 https://www.codewars.com/kata/55908aad6620c066bc00002a
 """


def xo(s):
    s = s.lower()
    return s.count("o") == s.count("x")


assert xo("xo") == True
assert xo("xo0") == True
assert xo("xxxoo") == False

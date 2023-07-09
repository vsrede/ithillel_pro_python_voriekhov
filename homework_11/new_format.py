"""
Написати фунцію шо задовільняє наступні тести. (github)

def new_format(string):
   # code here
assert (new_format("1000000") == "1.000.000")
assert (new_format("100") == "100")
assert (new_format("1000") == "1.000")
assert (new_format("100000") == "100.000")
assert (new_format("10000") == "10.000")
assert (new_format("0") == "0")
"""


def new_format(string):
    string = string[::-1]
    new_string = ""
    count = 0

    for value in string:
        if count % 3 == 0 and count != 0:
            new_string += "."
        new_string += value
        count += 1

    new_string = new_string[::-1]
    return new_string


assert (new_format("1000000") == "1.000.000")
assert (new_format("100") == "100")
assert (new_format("1000") == "1.000")
assert (new_format("100000") == "100.000")
assert (new_format("10000") == "10.000")
assert (new_format("0") == "0")

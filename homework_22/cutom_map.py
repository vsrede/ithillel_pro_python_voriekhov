class custom_map:

    def __init__(self, input_dict, key_func, value_func):
        self.input_dict = input_dict
        self.key_func = key_func
        self.value_func = value_func
        self.key_iter = iter(input_dict)

    def __iter__(self):
        return self

    def __next__(self):
        try:
            key = next(self.key_iter)
            key_new = self.key_func(key)
            value = self.value_func(self.input_dict[key])
            return key_new, value
        except StopIteration:
            raise StopIteration


def square_key(key):
    return key.title()


def cube_value(value):
    return value ** 3


input_dict = {'apple': 2, 'banana': 3, 'lemon': 4}

custom_mapped = custom_map(input_dict, square_key, cube_value)

for key, value in custom_mapped:
    print(key, value)

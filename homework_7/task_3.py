class colorizer:
    def __init__(self, color):
        colors = {"grey": "\033[90m", "red": "\033[91m", "green": "\033[92m", "yellow": "\033[93m",
                  "blue": "\033[94m", "pink": "\033[95m", "turquoise": "\033[96m"}
        self.color = colors[color]

    def __enter__(self):
        print(self.color, end='')

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('\033[0m', end='')


with colorizer('red'):
    print('printed in red')

with colorizer('yellow'):
    print('printed in yellow')

print('printed in default color')




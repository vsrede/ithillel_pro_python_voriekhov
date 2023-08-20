import random

from english_words import get_english_words_set


# def random_words(n):
#     web2lowerset = list(get_english_words_set(['web2'], lower=True))[:10000]
#     while n > 0:
#         yield web2lowerset[n - 1]
#         n -= 1


def random_words(n):
    if n > 10000:
        raise ValueError("Value can not be bigger than 10_000")

    web2lowerset = list(get_english_words_set(['web2'], lower=True))[:10000]
    selected_words = set()

    while n > 0 and len(selected_words) < n:
        word = random.choice(web2lowerset)
        if word not in selected_words:
            selected_words.add(word)
            yield word
            n -= 1


a = random_words(33)
for word in a:
    print(word)

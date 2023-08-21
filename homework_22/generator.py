from english_words import get_english_words_set


def random_words(n):
    if n > 10000:
        raise ValueError("Value can not be bigger than 10_000")

    set_words = list(get_english_words_set(['web2'], lower=True))[:n]
    for word in set_words:
        yield word


a = random_words(33)
for word in a:
    print(word)




from random import choice
nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]


def get_jokes(n, flag = 0):
    new_list = []
    for i in range(n):
        noun = choice(nouns)
        adverb = choice(adverbs)
        adjective = choice(adjectives)
        if flag != 0:
            pass
        new_list.append(f'{noun} {adverb} {adjective}')
    return new_list


print(get_jokes(3))

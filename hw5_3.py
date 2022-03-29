tutors = ['Иван', 'Анастасия', 'Петр', 'Сергей', 'Дмитрий', 'Борис', 'Елена']
classes = ['9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А']


def gen():
    i = 0
    j = 0
    while i < len(classes):
        if i >= i >= len(tutors):
            yield None, classes[i]
            i += 1
            j += 1
            break
        else:
            yield tutors[j], classes[i]
            i += 1
            j += 1


gen1 = gen()
print(gen1)
print(next(gen1))
print(next(gen1))
print(next(gen1))
print(next(gen1))
print(next(gen1))
print(next(gen1))
print(next(gen1))
print(next(gen1))
print(next(gen1))

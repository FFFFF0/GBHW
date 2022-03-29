def odd_to_15(num):
    for i in range(num):
        if i % 2 != 0:
            yield i


gen = odd_to_15(16)
print(gen)
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))

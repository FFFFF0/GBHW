src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
result = []

i = 0
while i < len(src):
    num = src[i]
    f = True
    for j in src[i+1:]:
        if num == j:
            f = False
    if f:
        result.append(num)
    i += 1


print(result)


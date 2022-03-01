list_a = []

for i in range(1, 1001, 2):
    i = i ** 3
    list_a.append(i)

list_b = []

for num in list_a:
    num_sum = 0
    num_change = num
    while num_change > 0:
        new_num = num_change % 10
        num_sum = num_sum + new_num
        num_change = num_change // 10
    if num_sum % 7 == 0:
        list_b.append(num)

print(sum(list_b))

list_c = []

for i in list_a:
    i = i + 17
    list_c.append(i)

list_d = []

for num_c in list_c:
    num_sum_c = 0
    num_change_c = num_c
    while num_change_c > 0:
        new_num_c = num_change_c % 10
        num_sum_c = num_sum_c + new_num_c
        num_change_c = num_change_c // 10
    if num_sum_c % 7 == 0:
        list_d.append(num_c)

print(sum(list_d))

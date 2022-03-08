new_list = [15.67, 8423, 56.34, 34.86, 2.57, 86.86, 988.6, 23.12, 735.3, 82, 56.43]


for item in new_list:
    print(item, end = ', ')

print(id(new_list))
new_list.sort()
print(new_list)
print(id(new_list))

new_list_2 = [15.67, 8423, 56.34, 34.86, 2.57, 86.86, 988.6, 23.12, 735.3, 82, 56.43]

new_list_2.sort()
new_list_2.reverse()
print(new_list_2)
print(new_list_2[0:5])
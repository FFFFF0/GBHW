with open('logs.txt') as file:
    new_list = []
    for num in file:
        splitted  = num.split()
        new_list.append((splitted[0], splitted[5].replace('"', ''), splitted[6]))


print(new_list)
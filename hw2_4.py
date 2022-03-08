new_list = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор аэлита']

new_list_2 = []

for item in new_list:
    new_list_2.append(item.split()[-1])

for new_item in new_list_2:
    print("Привет", new_item.title())
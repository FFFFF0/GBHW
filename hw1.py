duration = int(input("Введите время в секундах: "))

seconds = duration % 60

minutes = duration // 60
h_minutes = minutes % 60

hours = minutes // 60
d_hours = hours % 24

days = hours // 24

if 0 <= duration < 60:
    print(duration, "сек")
elif 60 <= duration < 3600:
    print(minutes, "мин", seconds, "сек")
elif 3600 <= duration < 86400:
    print(hours, "ч", h_minutes, "мин", seconds, "сек")
else:
    print(days, "дн", d_hours, "ч", h_minutes, "мин", seconds, "сек")

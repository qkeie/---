temperatures = [-5, -12, -3, -8, -1]

max_temp = 0  # Инициализация максимального значения

for temp in temperatures:
    if temp > max_temp:
        max_temp = temp

print("Самая высокая температура:", max_temp)
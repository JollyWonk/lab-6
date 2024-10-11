import math

a = float(input("Введіть початок діапазону a: "))
b = float(input("Введіть кінець діапазону b: "))
h = float(input("Введіть крок h: "))

result_list = []

x_val = a
while x_val <= b:
    f_x = 3 - math.log(abs(x_val - 6)) + math.cos(x_val)
    result_list.append(f_x)
    x_val += h

print("Список значень функції у рядок:", result_list)

print("Список значень функції у стовпчик:")
for val in result_list:
    print(val)

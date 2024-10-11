import math

a = float(input("Введіть початок діапазону a: "))
b = float(input("Введіть кінець діапазону b: "))
h = float(input("Введіть крок h: "))

x_val = a
while x_val <= b:
    f_x = 3 - math.log(abs(x_val - 6)) + math.cos(x_val)
    print(f"x = {x_val:.2f}, f(x) = {f_x:.3f}")
    x_val += h

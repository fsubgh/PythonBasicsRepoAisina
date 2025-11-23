#def make_report(title, **sections):
 #   print(f"==Отчет: {title}===")
  #  total = 0
   # for key, value in sections.items():
    #    print(f"{key}: {value}")
     #   total += value
      #  print(f"Общая сумма: {total} ")
#if __name__ == "__main__":
 #   make_report("Продажи", Север = 1200, Юг = 8500, Запад = 9000)

#Task 5
import math


def solve(a, b, c):
    d = b * b - 4 * a * c

    if d < 0:
        return None

    if d == 0:
        x = -b / (2 * a)
        return x, x

    sqrt_d = math.sqrt(d)
    x1 = (-b - sqrt_d) / (2 * a)
    x2 = (-b + sqrt_d) / (2 * a)

    if x1 > x2:
        x1, x2 = x2, x1

    return x1, x2


if __name__ == "__main__":
    a = int(input())
    b = int(input())
    c = int(input())

    result = solve(a, b, c)
    if result:
        if result[0] == result[1]:
            print(f"{result[0]:.1f}")
        else:
            print(f"{result[0]:.1f} {result[1]:.1f}")
    else:
        print("Нет действительных корней")

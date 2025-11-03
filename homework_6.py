a: int = int(input())
b: int = int(input())
max_sum = 0
best_num = 0
for x in range(a, b + 1):
    s = 0
    for i in range(1, x + 1):
        if x % i == 0:
            s += i
        if s > max_sum:
            max_sum = s
            best_num = x
        elif s == max_sum:
            best_num = x
print(best_num, max_sum)





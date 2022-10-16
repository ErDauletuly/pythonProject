#1
# year = int(input("Введите год:"))
# if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
#     print('YES')
# else:
#     print('NO')
#2
# m = int(input("Введите МЕсяц: "))
# if m==2:
#     print('28')
# elif m<=7:
#     print(30+m%2 )
# else:
#     print(31-m%2 )
#3
# n = int(input("n:"))
# m = int(input("m:"))
# if n < m:
#     for i in range(n, m + 1):
#         print(i)
# else:
#     for i in range(n, m - 1, -1):
#         print(i)
#4
# n = int(input("введите число:"))
# print([i for i in range(1, n // 2 + 1) if n % i == 0] + [n])

#5
# a = [78, -32, 9, 53, -2, -58, 2, 59]
# n = len(a)

# for i in range(n - 1):
#     flag = True
#     for j in range(n - i - 1):
#         if a[j] > a[j + 1]:
#             a[j], a[j + 1] = a[j + 1], a[j]
#             flag = False
#     if flag:
#         break
# print(a)

# литкоод


# Найдите сумму цифр трехзначного числа.

# n = int(input('Введите трехзначное число:'))
# sum = 0
# while n <= 99 or n > 999:
#     n = int(input('Это не трехзначное число. Введите трехзначное число:'))
# else:
#     while n > 0:
#         sum = sum + n % 10
#         n //= 10
# print(f'Сумма цифр в этом числе равна {sum}')




# Петя, Катя и Сережа делают из бумаги журавликов. Вместе они сделали S журавликов.
# Сколько журавликов сделал каждый ребенок, если известно, что Петя и Сережа сделали одинаковое количество журавликов,
# а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?

# s = int(input('Введите общее число журавликов:'))
# while s % 6 > 0:
#     s = int(input('Это значение не удовлетворяет условиям задачи. Введите число, кратное шести:'))
# else:
#     x = s // 6
#     print(f'Катя сделала {(4 * x)}, а Петя и Сережа сделали по {x}.')





# Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд и получали билет с номером.
# Счастливым билетом называют такой билет с шестизначным номером, где сумма первых трех цифр равна сумме
# последних трех. Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. Вам требуется написать программу,
# которая проверяет счастливость билета.

# n = str(input('Введите шестизначный номер билета:'))

# while len(n) != 6:
#     n = str(input('Это не шестизначный номер. Введите шестизначный номер:'))

# if n // 100000 + (n // 10000) % 10 + (n // 1000) % 10 == n % 10 + (n // 10) % 10 + (n // 100) % 10:
#     print('Поздравляем, это счастливый билет!')
# else:
#     print('Увы, это не счастливый билет!')







# Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек,
# если разрешается сделать один разлом по прямой между дольками (то есть разломить шоколадку на два прямоугольника).

# n = int(input('Введите длину шоколадки:'))
# m = int(input('Введите ширину шоколадки:'))
# k = int(input('Введите количество желаемых долек:'))
#
# if k < n * m and k % n == 0 or k < n * m and k % m == 0:
#     print(f'От шоколадки размером {n} × {m} долек можно отломить {k} долек')
# else:
#     print(f'От шоколадки размером {n} × {m} долек нельзя отломить {k} долек')

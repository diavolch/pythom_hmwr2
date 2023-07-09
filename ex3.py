# Напишите программу, которая принимает две строки вида “a/b” -
# дробь с числителем и знаменателем.
# Программа должна возвращать сумму и произведение* дробей.
# Для проверки своего кода используйте модуль fractions.
import fractions

input_1 = input("Введите первую дробь вида a/b")
input_2 = input("Введите вторую дробь вида a/b")

a1, b1 = map(int, input_1.split('/'))
a2, b2 = map(int, input_2.split('/'))

sum = str(a1*b2 + a2*b1) + '/' + str(b1 * b2)
mult = str(a1*a2) + '/' + str(b1*b2)

print("Сумма равна: " + sum)
print("Произведение равно: " + mult)
print(fractions.Fraction(input_1)+fractions.Fraction(input_2))
print(fractions.Fraction(input_1) * fractions.Fraction(input_2))
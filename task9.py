# todo: Решить линейное уравнение A·x + B = 0, заданное своими коэффициентами A и B 
# (коэффициент A не равен 0).
# Примечание: коэффициенты получаем через функцию input().
print('Введите коэффициенты для уравнения A·x + B = 0 (A не равно 0)')
a =int(input('A ='))
b =int(input('B ='))
print(f'''
{a}x + {b} = 0
x = {-b/a}
''')
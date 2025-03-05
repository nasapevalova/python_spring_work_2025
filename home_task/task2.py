# todo: Преобразуйте переменную age и foo в число
# age = "23"
# foo = "23abc"
age = "23"
foo = "23abc"
age =int(age)
foo = int(foo[0:2])
print(age)
print(foo)

# Преобразуйте переменную age в Boolean
# age = "123abc"
age = "123abc"
age = bool(age)
print(age)

# Преобразуйте переменную flag в Boolean
# flag = 1
flag = 1
flag = bool(flag)
print(flag)

# Преобразуйте значение в Boolean
# str_one = "Privet"
# str_two = ""
str_one = "Privet"
str_two = ""
str_one = bool(str_one)
str_two = bool(str_two)
print(str_one)
print(str_two)

# Преобразуйте значение 0 и 1 в Boolean
print(bool(0))
print(bool(1))

# Преобразуйте False в строку\
flag =False
print(str(flag))







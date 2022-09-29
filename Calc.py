def is_valid(n):
    if n.isdigit() and int(n) in range(1, border + 1):
        return True
    else:
        return False

def wanna_play():
    word = input('Хотите сыграть еще разок? (да/нет)\n')
    while word not in ['да', 'нет']:
        word = input('Что, простите? (да/нет)\n')
    if word == 'да':
        return True
    if word == 'нет':
        return False


import random

count = 0
print('Добро пожаловать в числовую угадайку')

border = input('Установите границу для угадывания? (число/нет)\n')
while not border.isdigit() and not border == 'нет':
    border = input('Что, простите? Чтобы установить границу введите число либо "нет"\n')
if border.isdigit():
    border = int(border) + 1
elif border == 'нет':
    border = 101
num = random.randint(1, border)
print(num)

guess = input(f'Введите число в диапазоне от 1 до {border - 1}!\n')

while guess != num:
    while not is_valid(guess):
        guess = input(f'А может быть все-таки введем число от 1 до {border - 1}!!!')
    guess = int(guess)
    if guess < num:
        count += 1
        print(f'Попытка №{count}')
        guess = input('Ваше число меньше загаданного, попробуйте еще разок!\n')
        continue
    if guess > num:
        count += 1
        print(f'Попытка №{count}')
        guess = input('Ваше число больше загаданного, попробуйте еще разок!\n')
        continue
    if guess == num:
        count += 1
        print(f'Вы угадали с {count} попытки, поздравляю!')
        if wanna_play():
            count = 0
            num = random.randint(1, 100)
            guess = input(f'Введите число в диапазоне от 1 до {border - 1}!\n')
            continue
        else:
            break

print('Спасибо, что играли, до встречи!')

# pass gen
# import random
# import string
#
# def is_yes_or_no(string):
#     if string == 'да' or string == 'нет':
#         return True
#     else:
#         return False
#
# def if_it_is_yes(string):
#     if string == 'да':
#         return True
#     elif string == 'нет':
#         return False
#
# def generate_password(length, chars):
#     password = ''
#     for i in range(1, length + 1):
#         password += random.choice(chars)
#     return password
#
# lowercase = string.ascii_lowercase
# uppercase = string.ascii_uppercase
# digits = string.digits
# punctuation = string.punctuation
#
# chars = ''
#
# print('Добро пожаловать в генератор паролей')
#
# #Запрашиваем и обрабатываем всю нужную информацию
# pass_amount = input('Введите требуемое количество паролей\n')
# while not pass_amount.isdigit():
#     pass_amount = input('Введите требуемое количество паролей\n')
# pass_amount = int(pass_amount)
#
# pass_length = input('Введите требуемую длину пароля\n')
# while not pass_length.isdigit():
#     pass_length = input('Введите требуемую длину пароля\n')
# pass_length = int(pass_length)
#
# need_digits = input('Нужно ли включать цифры? (да/нет)\n')
# while not is_yes_or_no(need_digits):
#     need_digits = input('Нужно ли включать цифры? (да/нет)\n')
# need_digits = if_it_is_yes(need_digits)
#
# need_upper = input('Нужно ли включать прописные буквы? (да/нет)\n')
# while not is_yes_or_no(need_upper):
#     need_upper = input('Нужно ли включать прописные буквы? (да/нет)\n')
# need_upper = if_it_is_yes(need_upper)
#
# need_lower = input('Нужно ли включать строчные буквы? (да/нет)\n')
# while not is_yes_or_no(need_lower):
#     need_lower = input('Нужно ли включать строчные буквы? (да/нет)\n')
# need_lower = if_it_is_yes(need_lower)
#
# need_punctuation = input('Нужно ли включать символы? (да/нет)\n')
# while not is_yes_or_no(need_punctuation):
#     need_punctuation = input('Нужно ли включать символы? (да/нет)\n')
# need_punctuation = if_it_is_yes(need_punctuation)
#
# need_symbols = input('Нужно ли включать неоднозначные символы? (il1Lo0O) (да/нет)\n')
# while not is_yes_or_no(need_symbols):
#     need_symbols = input('Нужно ли включать неоднозначные символы? (il1Lo0O) (да/нет)\n')
# need_symbols = if_it_is_yes(need_symbols)
#
# #Формируем строку со всеми нужными  символами
# if need_digits:
#     chars += digits
# if need_lower:
#     chars += lowercase
# if need_upper:
#     chars += uppercase
# if need_punctuation:
#     chars += punctuation
# if not need_symbols:
#     for c in 'il1Lo0O':
#         chars = chars.replace(c, '')
#
# #Выводим пароли
# for i in range(pass_amount):
#     password = generate_password(pass_length, chars)
#     print(f'pass{i + 1}: {password}')
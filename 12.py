# Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница.
# Петя помогает Кате по математике. Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать.
# Для этого Петя делает две подсказки. Он называет сумму этих чисел S и их произведение P.
# Помогите Кате отгадать задуманные Петей числа.

s = int(input('Катя, сумма двух загаданных чисел равна: \n'))
p = int(input('произведение, загаданных чисел равно: \n'))
for a in range(s):
    for b in range(p):
        if s == a + b and p == a * b:
            print(f'Правильно, первое число ="{a}", а второе число ="{b}"')

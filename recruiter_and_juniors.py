"""

У нас есть задача про безумного рекрутера, которую мы решили чистой математикой.
Давайте теперь используем мощь компьютеров, чтобы получить правильный ответ (и сэкономить время).

Задача звучит так.

В одной крупной технологической компании появился безумный рекрутер, который нанимал на работу только джуниоров.
У него был хитрый план — заполнить ими весь офис и получить за это премию от начальства.
Чтобы это сделать, он каждый день нанимал столько же людей, сколько уже работает в офисе. Грубо говоря, удваивал число джуниоров.

Когда он только начинал, в старом офисе работал всего один джуниор, но 30 дней спустя все рабочие места в офисе были
полностью заняты напуганными, ничего не понимающими джуниорами.

В новом, точно таком же по размеру офисе с первого дня работает в 2 раза больше людей, чем на старте в старом —
целых 2 джуниора вместо одного. Сколько времени уйдёт у безумного рекрутера на то, чтобы заполнить новый офис и получить
свою квартальную премию?

"""

# 1. Сколько джуниоров было на старте в старом офисе
junior = 1

# 2. Сколько дней ушло на заполнение старого офиса

day = 30

# Сделаем диапазон для цикла

month = range(1, day)

# 3. Каждый день в старом офисе…

for current_day in month:
    # 4. …удваивалось количество джуниоров

    junior = junior * 2

# 5. В новом офисе у нас уже два джуниора на старте

new_junior = 2

# 6. Заведём переменную для подсчёта дней в новом офисе

new_day = 0

# 7. Пока в новом офисе не станет столько же людей, как и в новом…

while new_junior <= junior:
    # 8. …мы удваиваем количество джуниоров в новом офисе…

    new_junior = new_junior * 2

    # 9. …и считаем каждый прошедший день

    new_day = new_day + 1

# Выводим количество дней, через сколько мы заполним новый офис

print(new_day)
"""
Предлагаю древнюю китайскую игру в палочки.

Играют два игрока.  Есть 10 палочек. Игроки по очереди берут от одной до трёх палочек.
Играют до тех пор пока не закончатся палочки. Тот кто взял последним - тот проиграл.

Реализуйте игру таким образом, чтобы могли играть два человека. Изначально есть 10 палочек.
На каждом ходу выводите на консоль текущее количество оставшихся палочек и просите ввести
количество палочек, которое хочет взять игрок (который делает ход).
Не забывайте менять очерёдность игроков и сокращать кол-во палочек.
В конце надо вывести кто победил - первый или второй игрок.

Нюансы реализации могут отличаться. Кто-то может захотет запросить имена у игроков.
Кто-то может захотеть реализовать не с 10-ю палочками, а с тем количеством,
которое введёт пользователь (может он хочет играть с 20-ю палочками?).

"""

number_of_sticks = 10
player_turn = 1


# Проверяем, можем ли брать такое кол-во спичек
def can_take(sticks):
    return 1 <= sticks <= 3


# Переключаем очередность игроков
def switch_player_turn(turn):
    return 1 if player_turn == 2 else 2


# Игра завершена, если спичек осталось меньше или равно 0
def end_of_game(sticks):
    return number_of_sticks <= 0


# Цикл игры
while not end_of_game(number_of_sticks):
    print(f'How many sticks you take? Remaining {number_of_sticks}')
    taken = int(input())

    if not can_take(taken):
        print(f'You tried to take {taken}. Allowed to take 1, 2, 3 sticks.')
        continue

    number_of_sticks -= taken
    print(f'Sticks taken: {taken}\n')

    if end_of_game(number_of_sticks):
        print(f'No more sticks in the game. \nPlayer {player_turn} has lost!')
        break

    player_turn = switch_player_turn(player_turn)

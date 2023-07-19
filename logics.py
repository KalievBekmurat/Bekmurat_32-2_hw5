import random
from random import choice
from decouple import config


def Cazino():
    MY_MONEY = config('MY_MONEY', cast=int)
    while True:
        print(f"Ваш капитал: {MY_MONEY}$")
        bid = int(input("Введите свою ставку: "))
        if bid > MY_MONEY:
            print("Недостаточно средств")
            continue
        slot = int(input("Введите номер слота от 1 до 30: "))
        if slot < 1 or slot > 30:
            print("Недопустимый номер слота!")
            continue
        winning_slot = random.randint(1, 31)
        if slot == winning_slot:
            print("Поздравляю! Вы победили!")
            MY_MONEY += bid * 2
        else:
            print("Извините, вы проиграли!")
            MY_MONEY -= bid
        print(f"Ваш капитал теперь: {MY_MONEY}$")
        play_again = input("Хотите сыграть еще? 1) Yes 2) No: ")
        if play_again.lower() == "2":
            print("Игра завершена!")
            break

Cazino()
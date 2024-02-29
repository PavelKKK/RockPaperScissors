import random

# Запрашиваем у пользователя, хочет ли он начать игру
start = input('Вы запустили игру "Камень, ножницы, бумага". Хотите поиграть? (Введите "+" или "-"): ')

if start == '+':
    print('Загрузка...')
    print("Загрузка завершена! Начинаем!")
    print("3...2...1...")
    print('Если захотите закончить, вводите "-".')
    print('Если захотите узнать счёт, вводите "с".')

    user_ball = 0
    rand_ball = 0

    while True:
        user = input("Камень, ножницы или бумага? (Введите 'к', 'н' или 'б'): ")
        list_play = ['к', 'н', 'б']

        if rand_ball == 3:
            print("Увы, вы проиграли!")
        elif user_ball == 3:
            print("\nУра, победа!")
            break

        if user in list_play:
            rand = random.choice(list_play)
            print("Мой выбор:", rand)

            if rand == 'к' and user == 'н':
                rand_ball += 1
            elif rand == 'к' and user == 'б':
                user_ball += 1
            elif rand == 'н' and user == 'к':
                user_ball += 1
            elif rand == 'н' and user == 'б':
                rand_ball += 1
            elif rand == 'б' and user == 'н':
                user_ball += 1
            elif rand == 'б' and user == 'к':
                rand_ball += 1
        elif user == 'с':
            print(f'Ваши баллы: {user_ball}. Баллы вашего соперника: {rand_ball}.')
        elif user == '-':
            print(f'Ваши баллы: {user_ball}. Баллы вашего соперника: {rand_ball}.')
            print('Конец игры! Заходите ещё!')
            break
        else:
            print('Введите "к", "н" или "б".')
elif start == '-':
    print('Жаль... :(')
else:
    print('Простите, я вас не понял. Если хотите играть, перезапустите программу и введите "+". Спасибо!')

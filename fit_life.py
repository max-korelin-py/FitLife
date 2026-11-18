# коэффициент суточной потребности воды на 1 кг массы тела
WATER_PER_KG = 30
# константа сколько мл воды в 1 литре
ML_PER_LITER = 1000

print('Привет! Я FitLife — твой фитнес-помощник!')
# Ввод имени пользователя
user_name = input('Как Вас зовут? ')
print()
print(f'Рад знакомству, {user_name}!')
print()

print(f'{user_name}, ответьте, пожалуйста, на несколько вопросов: ')
while True:
    try:
        # Ввод возраста пользователя
        user_age = input(
            'Сколько Вам лет? (введите целое число, например 25): ')
        user_age_int = int(user_age)
        break
    except ValueError:
        # Вывод подсказки если пользователь ввел возраст текстом
        print('Извените, новозраст необходимо ввести числом.')
while True:
    try:
        # Ввод веса пользователя
        user_weight = input(
            'Ваш вес (кг)? (введите числом напимер 75.5 или 75,5): ')
        user_weight_fl = float(user_weight.replace(',', '.'))
        break
    except ValueError:
        # Вывод подсказки если пользователь ввел вес текстом
        print('Извените, вес необходимо ввести числом.')
while True:
    try:
        # Ввод роста пользователя
        user_height = input(
            'Ваш рост (м)? (введите числом например 1.75 или 1,75): ')
        user_height_fl = float(user_height.replace(',', '.'))
        break
    except ValueError:
        # Вывод подсказки если пользователь ввел рост текстом
        print('Извените, рост необходимо ввести числом.')

bmi = user_weight_fl / (user_height_fl ** 2)      # вычисление ИМТ
# округление вычисления ИМТ до 0.1
bmi_round = round(bmi, 1)
# вычисление рекомендуемой нормы воды (в мл)
water_ml = user_weight_fl * WATER_PER_KG
# перевод рекомендуемой нормы воды в литры
water_l = water_ml / ML_PER_LITER
# округление рекомендуемой нормы воды в литрах до 0.1
water_l_round = round(water_l, 1)

print()
print(f'Отчет для пользователя: {user_name} ({user_age_int} г.)')
print(f'Твой Индекс Массы Тела: {bmi_round}')
print(f'Рекомендуемая норма воды: {water_l_round} л. в день')
print()
print('Расчет окончен. Будьте здоровы!')

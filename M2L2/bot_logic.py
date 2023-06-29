import random

def gen_pass(pass_length):
    elements = "+-/*!&$#?=@<>abcdefghijklmnopqrstuvwxyz1234567890"
    password = ""

    for i in range(pass_length):
        password += random.choice(elements)

    return password

def roll_dice():
    return random.choice (['1', '2', '3', '4', '5', '6'])

def guess_number():
    number = random.choice([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    return number

def idea():
    return random.choice(['1. Не использовать маленькие батарейки, а использовать зарядки для аккумуляторов.', '2. Не выбрасывать батарейки, а утилизировать их в спец. пункты.', '3. Использовать экологичные материалы, которые не загрязняют природу.', '4. Сортировать мусор.', '5. Использовать только безвредные для природы устройства', '6.ездить на электрических машинах', '7.поставить солнечные панели на крышу'])

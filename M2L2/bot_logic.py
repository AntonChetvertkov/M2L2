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
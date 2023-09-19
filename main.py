import random


points = {"comp": 0, 'plr': 0}
while True:
    r = random.randint(100, 120)
    a = random.randint(1, 100)
    op = random.choice(('+', '-'))
    if op == '+':
        s = r + a
        d = input(f'{r} + {a} = ')
    else:
        s = r - a
        d = input(f'{r} - {a} = ')
    if d == str(s):
        print('Верно')
        points["plr"] += 1
    else:
        print('Неверно')
        points['comp'] += 1
    print(f'счет : {points["plr"]} : {points["comp"]}')
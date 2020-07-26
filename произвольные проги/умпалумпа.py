import random
while True:
    name = input()
    a = random.randint(1, 300)
    if a >= 1 and a < 100:
        print(name, "Ваш IQ", a, "\nВы полнейший долбаеб. Вообще непонятно почему вы дожлили до своего возраста\n")
    elif a >= 100 and a < 200:
        print(name, "Ваш IQ", a, "\nЯсно почему ты поступил на ФКН...\n")
    else:
        print(name, "Ваш IQ", a, "\nИди нахуй шлюха\n")
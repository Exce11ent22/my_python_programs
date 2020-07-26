def person():
    weight = int(input("Какой у тебя вес? "))
    height = int(input("Какой у тебя рост? "))
    color = input("Какой у тебя любимый цвет? ")
    you = {"рост": weight,
           "вес": height,
           "любимый цвет": color}
    return you

some_person = person()
print(some_person)

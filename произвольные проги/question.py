ans = input("Какой ваш любимый цвет? ")
with open("color.txt","w") as f:
    f.write(ans)

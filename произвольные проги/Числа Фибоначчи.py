a1 = 0
a2 = 1
b = int(input("Сколько чисел вы хотите получить? - "))
i = 0
while i < b and b <= 1000:
    print(a2, "    ", i + 1, "-е число")
    temp = a2
    a2 += a1
    a1 = temp
    i += 1
    print(a2 / a1, "- коэффициент", "\n")
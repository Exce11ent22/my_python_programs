while True:
    user_input = input()
    if user_input.find("+") != -1:
        numbers = user_input.split("+")
        answer = float(numbers[0]) + float(numbers[1])
        if answer % 1 == 0:
            answer = int(answer)
        print(answer, "\n")
    elif user_input.find("-") != -1:
        numbers = user_input.split("-")
        answer = float(numbers[0]) - float(numbers[1])
        if answer % 1 == 0:
            answer = int(answer)
        print(answer, "\n")
    elif user_input.find("*") != -1:
        numbers = user_input.split("*")
        answer = float(numbers[0]) * float(numbers[1])
        if answer % 1 == 0:
            answer = int(answer)
        print(answer, "\n")
    elif user_input.find("/") != -1:
        numbers = user_input.split("/")
        answer = float(numbers[0]) / float(numbers[1])
        if answer % 1 == 0:
            answer = int(answer)
        print(answer, "\n")
    elif user_input.find("^") != -1:
        numbers = user_input.split("^")
        answer = float(numbers[0]) ** float(numbers[1])
        if answer % 1 == 0:
            answer = int(answer)
        print(answer, "\n")
    else:
        print("Каво? Заново!!!")
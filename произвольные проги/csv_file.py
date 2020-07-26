import csv

my_list = [["Звездные войны","Терминатор","Искусственный интеллект"],
           ["Дурак","Иатильда","Левиафан"],
           ["Люди в черном","Я - робот","Эволюция"]]

with open("mf.csv", "w") as f:
    w = csv.writer(f, delimiter=",")
    for el in my_list:
        w.writerow(el)
    

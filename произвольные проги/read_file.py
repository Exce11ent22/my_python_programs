my_list = []

with open("mf.txt", "r") as f:
    my_list.append(f.read())
    
print(my_list)

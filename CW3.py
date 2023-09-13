def flick_switch(list):
    new_list = []
    a = True
    if a == True:
        for i in range(len(list)):
            if list[i] == 'flick':
                a = not a
                new_list.append(a)
            else:
                new_list.append(a)
    elif a == False:
        for i in range(len(list)):
            if list[i] == 'flick':
                a = not a
                new_list.append(a)
            else:
                new_list.append(a)
    return new_list


list_1 = ["codewars", "flick", "code", "wars"]
list_2 = ['flick', 'chocolate', 'adventure', 'sunshine']
list_3 = ['bicycle', 'jarmony', 'flick', 'sheep', 'flick']

print(flick_switch(list_1))
print(flick_switch(list_2))
print(flick_switch(list_3))
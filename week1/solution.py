def modify_list(l):
    length = len(l)
    for i in range(length):
        if i >= length:
            break
        if l[i] % 2 == 1:
            del l[i]
            length -=1
            i += 1
        else:
            l[i] //= 2


array = [1, 3, 5]
modify_list(array)
print(array)

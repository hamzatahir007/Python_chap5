def comman_num(l1,l2):
    comman = []
    for i in l1:
        if i in l2:
            comman.append(i)
    return comman

l1 = [1,2,5,8] 
l2 = [1,2,7,6]
print(comman_num(l1,l2))

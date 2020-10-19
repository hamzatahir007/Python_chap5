
def squre_list (l):
    squre = []
    for i in l:
        squre.append(i** 2)
    return squre


numbers= list(range(1,11))
print(squre_list(numbers))

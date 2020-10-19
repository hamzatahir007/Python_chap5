#print list in reverse

# def reverse_func (l):
#     l.reverse()
#     return l

#another method

# def reverse_func (l):
#     return l[::-1]


#another method
def reverse_func(l):
    r_list = []
    for i in range (len(l)):
        popped_itens = l.pop()
        r_list.append(popped_itens)
    return r_list

numbers= [1,2,3,4,5]
print(reverse_func(numbers))
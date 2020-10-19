

def list_func (l):
    even = []
    odd = []
    for i in l:
        if i%2 == 0:
            even.append(i)
        else:
            odd.append(i)
    OUTPUT = [odd , even]
    return OUTPUT

numbers = [1,2,3,4,5,6,7]
print(list_func(numbers))
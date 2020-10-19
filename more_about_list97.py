

#list generate automatically
# numbers = list(range(1,11))
# print(numbers)

number = [1,2,3,4,5,6,7,8,9,10]
# pop_items = number.pop() //for store del number back is variable
# print(numbers)


#for see loction
# print(number.index(1, 11, 15))



#for pass list in function
def negative_list (l):
    negative= []
    for i in l:
        negative.append(-i)
    return negative

print(negative_list(number))
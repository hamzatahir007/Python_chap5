#list inside list
fruits = [['apple' , 'banana'] , ['apple' , 'kiwi'] , ['grapes' , 'orange']]
# 3time----> 3lists
# print(fruits[2])

for sublist in fruits:
    for i in sublist:
        print(i)


#for print list with list number and veriable number
# print(fruits[1][1])


#for check type of veriables
# s = type(fruits)
# print(s)
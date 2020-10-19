#min and max

numbers = [12,40,2]
# print(min(numbers))
# print(max(numbers))

def greatest_num (l):
    return max(l) - min(l)

print(greatest_num(numbers))
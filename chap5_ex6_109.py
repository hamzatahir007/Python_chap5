#last exsersize
#function
#[1,2,3,[1,2],[3,4]]

list_inlist = [1,2,3,[1,2],[3,4]]
def num_list (l):
    count = 0
    for sublist in l:
        if type(sublist) == list:
            count = count + 1
    return count

print(num_list(list_inlist))





#reverse every string in a list

def reverse_string (l):
    elements = []
    for i in l:
        elements.append(i[::-1])
    return elements

example = ['abc' , 'tuv' , 'xyz']
print(reverse_string(example))
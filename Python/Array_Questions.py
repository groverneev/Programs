"""
a = int(input())
output = 1
counter = 1
for b in range(a+1):
    output = output * counter
    counter += 1
print(output)
"""
def remove_(a, b):
    for c in range(len(a)):
        if a[c] == b:
            a.pop(c)
            break
    print(a)
#remove_([3, 3], 1)

def reverse_array(a):
    old_a = 0
    new_a = len(a)-1
    while old_a <= new_a:
        a[old_a], a[new_a] = a[new_a], a[old_a]
        old_a += 1
        new_a -= 1
    return a
    """
    counter = len(a) - 1
    new = []
    for c in range(len(a)):
        new.append(a[counter])
        counter = counter - 1
    print(new)
    """
#print(reverse_array([1, 5, 4, 7, 2]))

def remove_duplicates(a):
    new = []
    for c in range(len(a)):
        if a[c] not in new:
            new.append(a[c])
    print(new)
#remove_duplicates([3, 1, 6, 3, 1, 6])

def rotate_array(a, b):
    if b > len(a):
        b = b%len(a)
    first = reverse_array(a[:len(a) - b])
    second = reverse_array(a[len(a)-b:])
    a = first + second
    print(reverse_array(a))
rotate_array([1, 2, 3, 4, 5], 101)
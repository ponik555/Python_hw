a=[1,2,2,2,3,4,5,5,5,6,7]
b=[5,6,7,8,9,9,9,10,11,11,12]
def intersection_lists(a, b):
    return set(a).intersection(set(b))

print(list(set(a).intersection(set(b))))
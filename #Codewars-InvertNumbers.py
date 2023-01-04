#Codewars-InvertNumbers
def invert(lst):
    n_lst = []
    for i in lst:
        n_lst.append (i * -1)
    return n_lst

print(str(invert([1,2,3,4,5])))
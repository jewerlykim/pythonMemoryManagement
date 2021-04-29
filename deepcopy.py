import copy
a = ['Head', ['Sub']]
b = copy.deepcopy(a)
b[1].append('Sub2')
print(a, b)
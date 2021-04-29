a = ['Head', ['Sub']]
b = a.copy() # or a[:]
b[1].append('Sub2')
print(a, b)
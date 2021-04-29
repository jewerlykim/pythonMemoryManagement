mutable1 = ['alpha'] # list
print(hex(id(mutable1)))
mutable1.append('bravo')
print(hex(id(mutable1)))
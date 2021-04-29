s = ''
jewelist = [1,2,3,4,5,6,7]
print(hex(id(s)))
for x in jewelist:
    s += str(x)
    print(hex(id(s)), s)

b = 'Hello'
first_name = 'jewelry'
last_name = 'kim'
print(hex(id(b)))
b = b + first_name
print(hex(id(b)))
b = b + ' '
print(hex(id(b)))
b = b + last_name
print(hex(id(b)))
b = b + '!'
print(hex(id(b)))



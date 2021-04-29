import weakref
import sys
class SomeClass(object):
    def __init__(self, *args):
        super(SomeClass, self).__init__(*args)
        
a = SomeClass()
b = weakref.ref(a)
print(b())
del a
print(sys.getrefcount(b))
print(b())
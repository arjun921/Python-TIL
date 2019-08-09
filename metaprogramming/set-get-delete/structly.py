# Manipulating get,set, delete of attributes

from inspect import Parameter, Signature

class Descriptor: 
    # Capturing (DOT) operator.
    # Customized handling of a specific attribute
    def __init__(self, name=None):
        self.name = name

    def __get__(self, instance, cls):
        # instance: instance being manipulated
        # eg. Stock instance
        # OPTIONAL! 
        if instance is None:
            return self
        else:
            print("Get:", self.name)
            return instance.__dict__[self.name]
        
    
    def __set__(self, instance, value):
        print("Set: ", self.name, value)
        instance.__dict__[self.name] = value
    
    def __delete__(self, instance):
        print("Delete: ", self.name)
        del instance.__dict__[self.name]

def make_signature(names):
    # Enforces args, kwargs and enforces checks like duplicated, enough arguments passed, etc. 
    return Signature(Parameter(name,Parameter.POSITIONAL_OR_KEYWORD) for name in names)

class StructMeta(type):
    def __new__(cls, clsname, bases, clsdict):
        clsobj = super().__new__(cls, clsname, bases, clsdict)
        
        sig = make_signature(clsobj._fields)
        setattr(clsobj, '__signature__', sig)
        return clsobj

class Structure(metaclass=StructMeta):
    _fields =[]
    def __init__(self,*args, **kwargs):
        bound = self.__signature__.bind(*args, **kwargs)
        for name, val in bound.arguments.items():
            setattr(self, name, val)

class Stock(Structure):
    _fields = ['name', 'shares', 'price']

    name = Descriptor('name')  
    shares = Descriptor('shares')  
    price = Descriptor('price')

class Point(Structure):
    _fields = ['x','y']

class Address(Structure):
    _fields = ['hostname','port']


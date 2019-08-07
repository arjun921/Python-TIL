# before
"""class Stock:
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price

class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y

class Address:
    def __init__(self,hostname,port):
        self.hostname = hostname
        self.port = port"""

# after
from inspect import Parameter, Signature

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

class Point(Structure):
    _fields = ['x','y']

class Address(Structure):
    _fields = ['hostname','port']


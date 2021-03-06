# Adding Type checking while setting parameters in an instance
# Multiple inheritence 

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

class CheckType(Descriptor):
    _type = object      # expected type
    def __set__(self, instance, value):
        if not isinstance(value, self._type):
            raise TypeError(f"Expected {self._type}")
        super().__set__(instance, value)

class Integer(CheckType):
    _type = int

class Float(CheckType):
    _type = float

class String(CheckType):
    _type = str

class Positive(Descriptor):
    def __set__(self, instance, value):
        if value < 0:
            raise ValueError('Value must be >= 0')
        super().__set__(instance, value)

class PositiveInteger(Integer, Positive):
    pass

class PositiveFloat(Float, Positive):
    pass

# Length check
class Sized(Descriptor):
    def __init__(self, *args, maxlen, **kwargs):
        self.maxlen = maxlen
        super().__init__(*args, **kwargs)
    
    def __set__(self, instance, value):
        if len(value) > self.maxlen:
            raise ValueError('Too Long')
        super().__set__(instance,value)

class SizedString(String, Sized):
    pass

import re

# Pattern matching
class Regex(Descriptor):
    def __init__(self, *args, pat, **kwargs):
        self.pat = re.compile(pat)
        super().__init__(*args, **kwargs)
    
    def __set__(self, instance, value):
        if not self.pat.match(value):
            raise ValueError('Invalid string')
        super().__set__(instance, value)

class SizedRegexString(SizedString, Regex):
    pass

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
    name = SizedRegexString('name', maxlen=4, pat='[A-Z]+$')
    shares = PositiveInteger('shares')  
    price = PositiveFloat('price')

class Point(Structure):
    _fields = ['x','y']

class Address(Structure):
    _fields = ['hostname','port']

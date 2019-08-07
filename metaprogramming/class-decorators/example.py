#add decorators to all class definitions

from debugly import debugmethods

@debugmethods
class Test:
    # @debugmethods is called when 
    """debug methods test class"""
    def __init__(self):
        pass
    
    def func1(self):
        pass
    
    def func2(self):
        pass
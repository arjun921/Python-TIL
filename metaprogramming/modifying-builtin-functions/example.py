from debugly import debugattrs

@debugattrs
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def test_funct(self):
        pass
from debugly import debug

@debug
def add(x,y):
    return x+y

@debug(prefix='*38')
def sub(x,y):
    return x-y


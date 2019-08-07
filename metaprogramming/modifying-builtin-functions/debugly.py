
def debugattrs(cls):
    
    # modifying set builtin function
    orig_getattr = cls.__getattribute__
    def __getattribute__(self, name):
        """creating new __get attribute function"""
        print('Get:', name)
        return orig_getattr(self,name)

    # assigning modified function
    cls.__getattribute__ = __getattribute__

    # modifying set builtin function 
    orig_setattr = cls.__setattr__
    def __setattr__(self, name, value):
        print('Set:', name, value)
        return orig_setattr(self,name, value)

    cls.__setattr__ = __setattr__

    return cls

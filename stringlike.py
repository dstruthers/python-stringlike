class StringLike(object):
    def __init__(self, *args, **kwargs):
        self._value = str(*args, **kwargs)

    def __eq__(self, y):
        return str(self) == y

    def __getattr__(self, attr):
        if hasattr(str(self), attr):
            return getattr(str(self), attr)
        else:
            raise AttributeError('"{}" object has no attribute "{}"'.format(self.__class__.__name__, attr))

    def __getitem__(self, i):
        return self.__class__(str(self)[i])

    def __len__(self):
        return len(str(self))

    def __mod__(self, y):
        return self.__class__(str(self) % y)

    def __mul__(self, y):
        return self.__class__(str(self) * y)

    def __ne__(self, y):
        return str(self) != y
    
    def __repr__(self):
        return repr(str(self))

    def __rmod__(self, x):
        return self.__class__(x % str(self))
    
    def __rmul__(self, x):
        return self.__class__(x * str(self))

    def __str__(self):
        return self._value

    def format(self, *args, **kwargs):
        return self.__class__(str(self).format(*args, **kwargs))

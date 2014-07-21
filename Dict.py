#Make it a wrapper of dict-like object, instead of being a dict.
class Dict(dict):
    """
    A dict with index path resolving.

    d['a']['b']['c'] could be simplified to d['a.b.c']

    Written by Logan
    """
    def __init__(self, *args, **kwargs):
        super(self.__class__,self).__init__(*args,**kwargs)

    def __getitem__(self,key):
        indices = key.split('.')
        # value = self[indices[0]]
        # If so, the program will get stuck in the infinite recursion
        value = super(self.__class__,self).__getitem__(indices[0])
        print(value.__class__)
        # You will see that now value is a dict object, not Dict, and thus we can call the [] operator.
        for k in indices[1:]:
            value = value[k]

        return value


if __name__ == '__main__':
    d = {'l01':{'l11':{'l21':'a','l22':'b'},'l12':'c'},'l02':{'l12':'e'}}
    D = Dict(d)
    print(D['l01.l11'])
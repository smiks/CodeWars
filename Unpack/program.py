__author__ = 'Sandi'
import collections
def unpack(l):
    for el in l:
        if isinstance(el, collections.Iterable) and type(el) is not str:
                if type(el) is dict:
                    for sub in unpack(el.items()):
                        yield sub
                else:
                    for sub in unpack(el):
                        yield sub
        else:
            yield el
res = unpack([None, [1, ({2, 3}, {'foo': 'bar'})]])
res = [r for r in res]
print(res)
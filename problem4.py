'''cons(a, b) constructs a pair, and car(pair) 
and cdr(pair) returns the first and last element of that pair. For example,
car(cons(3, 4)) returns 3, and cdr(cons(3, 4)) returns 4.'''

def my_tuple(a,b):
    return (a,b)

def cons(a, b):
    def pair(f):
        return f(a, b)
    return pair

def cdr(pair):
    _,b = pair(my_tuple)
    return b

def car(pair):
    a,_ = pair(my_tuple)
    return a


print(cdr(cons(3,4)))
print(car(cons(3,4)))

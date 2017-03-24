import functools

def count():
    fs=[]
    for i in range(1,4):
        def f(x):
            return lambda : x*x
        fs.append(f(i))
    return fs

def log(text=''):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator

@log()
def now():
    print('dsadads')

now()
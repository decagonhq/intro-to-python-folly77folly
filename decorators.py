def decorator_func(func):
    def wrapper (*args, **kwargs):
        print('Hello')
        if args != None:
            func(*args, **kwargs)
        else:
            print ('enter name to continue')
            return
        print('Welcome to Decorator Class')
    return wrapper

@decorator_func
def say_hello(name):
    print(name)

# hello = decorator_func(say_hello)
# hello()
say_hello("dave")

class Greeting:
    def __init__(self,func):
        self.func=func

    
    def __call__(self, *args, **kwargs):
        print('Hello')
        self.func(*args, **kwargs)
        print('Welcome to Class Decorator')



@Greeting
def say_name(name):
    print(name)

say_name('Shade')
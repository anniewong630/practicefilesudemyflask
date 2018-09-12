def new_decorator(func):

    def wrap_func():
        print ("Code would be here, before executing the func")

        func()

        print ("Code here will execute after the func()")

    return wrap_func

#def func_needs_decorator():
    #print ("This function is in need of a Decorator")

def hello():
    print('HELLO')

#func_needs_decorator()

# Reassign func_needs_decorator
#func_needs_decorator = new_decorator(func_needs_decorator)

#func_needs_decorator()


# So what just happened here? A decorator simple wrapped the function and
# modified its behavior. Now lets understand how we can rewrite this code using
# the @ symbol, which is what Python uses for Decorators:

@new_decorator
def func_needs_decorator():
    print ("This function is in need of a Decorator")

func_needs_decorator()
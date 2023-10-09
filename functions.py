import time,math
from inspect import currentframe, getframeinfo
print("===========================FUNCTIONS==========================")
# optional arguments - can appear only at the end of args list
def func1(first_arg, optional_arg=10):
    print(getframeinfo(currentframe()).lineno," : ",first_arg)
    print(getframeinfo(currentframe()).lineno," : ",optional_arg)

# variable number of args - tuple
# args is a tuple
def func2(first_arg, *args):
    print(getframeinfo(currentframe()).lineno," : ",first_arg)
    print(getframeinfo(currentframe()).lineno," : ",args)

# default return value is None
def func3():
    print()

# returning more than one result
def func4():
    return ("result1",2,"result3")

func1("first")
func1("first","optional")
func2("first","second","third")
print(getframeinfo(currentframe()).lineno," : ",func3())
print(getframeinfo(currentframe()).lineno," : ",func4())

print("===========================CLOSURES===========================")
def outer_func(arg):
    # nested func that can access variables in enclosing scope is called closure
    # cant be invoked outside of enclosing scope (outside outer function)
    def inner_func():
        print(getframeinfo(currentframe()).lineno," : ",arg)
    # returning nested function as result from outer functions
    # enables calling inner function from other scopes
    return inner_func

# error: inner_func()
closure=outer_func("test")
# calling closure
# although outer function has already executed and argument arg from outer_func should have been destroyed
# closure function can access it afterward
closure()
# memory addresses (references) of enclosed variables are stored in __closure__
print(getframeinfo(currentframe()).lineno," : ",closure.__closure__)

# example - printing odd numbers with closure
# this approach mitigates using a global variable used for storing next odd number
def calculate():
    num = 1
    def inner_func():
        nonlocal num
        num += 2
        return num
    return inner_func

odd = calculate()
print(getframeinfo(currentframe()).lineno," : ",odd())
print(getframeinfo(currentframe()).lineno," : ",odd())
print(getframeinfo(currentframe()).lineno," : ",odd())
odd2 = calculate()
print(getframeinfo(currentframe()).lineno," : ",odd2())

print("==========================DECORATORS==========================")
# decorators extend function functionality without permanently modifying it

# example - creating decorator that measures func exec time
# func that represents decorator
def exec_time_decorator(func_to_decorate):
    # wrapping function and extending its func
    def wrapper_func():
        start=time.time()
        func_to_decorate()
        end=time.time()
        print(getframeinfo(currentframe()).lineno," : ",func_to_decorate.__name__," - exec time=",end-start,"s")
    # returning decorated and wrapped func
    return wrapper_func
# functions to be decorated
def simple_func():
    time.sleep(1)
    print("Hello from simple func!")
# applying decorator to the function without using python's decorator mechanism
decorated_simple_func =exec_time_decorator(simple_func)
decorated_simple_func()
# applying decorator to the function by using python's decorator mechanism
@exec_time_decorator
def simple_func_decorated():
    time.sleep(1)
    print("Hello from simple func!")
simple_func_decorated()

# example - creating decorator that measures func exec time
# now for functions with one argument
def exec_time_decorator_with_arg(func_to_decorate):
    def wrapper_func(n):
        start=time.time()
        result=func_to_decorate(n)
        end=time.time()
        print(getframeinfo(currentframe()).lineno," : ",func_to_decorate.__name__," - exec time=",end-start,"s")
        return result
    return wrapper_func
@exec_time_decorator_with_arg
def factorial(n):
    time.sleep(2)
    result=math.factorial(n)
    print(getframeinfo(currentframe()).lineno," : ","Factorial of",n, "calculated!")
    return result
print(getframeinfo(currentframe()).lineno," : ",factorial(10))

# example - creating decorator that measures func exec time
# now for functions with any number of argument
def exec_time_decorator_with_args(func_to_decorate):
    def wrapper_func(*args,**kwargs):
        start=time.time()
        result=func_to_decorate(*args,**kwargs)
        end=time.time()
        print(getframeinfo(currentframe()).lineno," : ",func_to_decorate.__name__," - exec time=",end-start,"s")
        return result
    return wrapper_func
@exec_time_decorator_with_args
def sum(a,b,c):
    time.sleep(2)
    result=a+b+c
    print(getframeinfo(currentframe()).lineno," : ","Sum calculated!")
    return result
print(getframeinfo(currentframe()).lineno," : ",sum(1,2,3))
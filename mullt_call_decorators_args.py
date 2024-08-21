# decorator é uma função que extende o comportamento de outra função sem alterar a função original
import time
import random

################################################
############### BASIC DECORATOR ################
################################################

def execute_time(func):
    def wrapper():
        initial_time = time.time()
        func()
        final_time = time.time()-initial_time
        print(f"The time took to do {func.__name__} is {final_time}")
    return wrapper


@execute_time
def building():
    for x in range(random.randint(3,7)):
        time.sleep(1)
    print("Finish building")

building()


#######################################################
############### MORE COMPLEX DECORATOR ################
#######################################################

def put_some_syrup(funct):
    def pss_w():
        print("Pss ->", funct.__name__, end="")
        ml = "20ml"
        flavor = {"Flavor" : "vanila"}
        print(f" || Send: {ml} and {flavor}")
        funct(ml,flavor)
    return pss_w

def flavor(func):
    def flavor_w(*args):
        print("Flavor ->", func.__name__, end="")
        print(f" || data recive {args}")
        a=args[0]
        for k,v in args[1].items():
            func(a,v)
    return flavor_w
    
@put_some_syrup # put_some_syrup(flavor)
@flavor 
def get_ice_cream(*args):
    print(f"Gtc -> data recive{args}")
    for x in args:
        print(f"args {x}")
    pass


get_ice_cream()


# Most efficient way to unpack KeyWords Arguments
# print("kwargs", kwargs, type(kwargs))
# for x, y in kwargs.items():
#     print("kwargs: ",x ,"\n",y)
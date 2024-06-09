def foo(x=0, y=0, z=0):
    print(x*y*z)


foo()


def foo(x=1, y=1, z=1):
    print(x * y * z)


foo(x=5, z=6)


# *args - in case of unwanted arguments
# **kwargs - if unwanted arguments have names
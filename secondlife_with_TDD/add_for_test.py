def add(a, b):
    if type(a) is not int and type(a) is not float:
        raise TypeError("a has to be a number")
    elif type(b) is not int and type(b) is not float:
        raise TypeError("b has to be a number")
    else:
        return a+b
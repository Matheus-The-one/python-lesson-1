def upper(function):
    def lower(a,b):
        if a<b:
            a,b=b,a
        return function(a,b)
    return lower

@upper
def range(a,b):
    print(a+b)
    

range(5,8)
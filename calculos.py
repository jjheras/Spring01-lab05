def suma (a,b):
    return a+b
def resta (a,b):
    return a-b
def multiplicacion (a,b):
    return a*b
def division(a,b):
    try:
        return a/b
    except ZeroDivisionError:
        return "Error, ZeroDivisionError"
        
if __name__ == "__main__":
    print(suma(5,3))
    print(division(5,0))
    
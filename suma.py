def suma (a,b):
    return a+b
def resta (a,b):
    return a-b
def multiplicacion (a,b):
    return a*b
def division(a,b):
    if b == 0:
        return "Error, no se puede dividir entre 0"
    else:
        return a/b


if __name__ == "__main__":
    print(suma(5,3))
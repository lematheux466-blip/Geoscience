def somme(x,y,z):
    return x+y+z
result=somme(2,3,4)
print(result)


def somme(x,y):
    if x<y:
        return x,y
    else:
        return y,x
result=somme(5,3)
print(result)





def fact(x):
    if x<=1:
        return 1
    else:
        return x*fact(x-1)
result=fact(5)
print(result)


def montrer():
    print("google play")
    
montrer()
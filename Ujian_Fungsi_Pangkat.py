def pangkat(x, y):
    if (y == 0):
        return 1
    elif (int(y % 2) == 0):
        return (pangkat(x, int(y/2)) * pangkat(x, int(y/2)))
    else:
        return (x * pangkat(x, int(y / 2)) * pangkat(x, int(y / 2))) 

print(pangkat(2,2))
print(pangkat(3,3))
print(pangkat(10,5))
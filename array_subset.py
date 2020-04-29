def GetTypes(fruitdic):
    return (len(fruitdic))

def GetTotal(fruitdic):
    sum = 0
    for i in fruitdic:
        sum = sum + fruitdic[i]

    return sum

def NewFruit(fruitdic, newFruit, newstock):

    if newFruit in fruitdic:
        print(" Error cannot add duplicate keys")
        return fruitdic
    else:
        fruitdic[newFruit] = newstock
        return fruitdic

fruitdic = {'Bananas': 5, 'Grapes': 1200, 'Apples': 16}
print(GetTypes(fruitdic))
print(GetTotal(fruitdic))
NewFruit(fruitdic, "Pears", 50)
print(fruitdic)

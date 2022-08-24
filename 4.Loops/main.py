#Problem 1
myList = ['a','b','c','d']
def concatenate(inputLst):
    myStr = ''
    for word in myList:
        myStr+=word
    return myStr
print(concatenate(myList))

#Problem 2
colors1 = ["White","Black", "Red"]
colors2 = ["Red","Green"]

def colorDiff(c1,c2):
    newList = []
    for color in c1:
        if color not in c2:
            newList.append(color)
    return newList

print(colorDiff(colors1,colors2))
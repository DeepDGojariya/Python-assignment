# Problem 1
inputStr = "w3resource"
def getFirst2Last2(inputStr):
    if len(inputStr)<=0:
        return ""
    return inputStr[0:2]+inputStr[-2:]

print(getFirst2Last2(inputStr))



#Problem 2
myList = [1,2,3,4,5]
def getLargest(lst):
    if lst!=[]:
        return max(lst)
    return None

print(getLargest(myList))

#Problem 3
dict1={1:10, 2:20}
dict2={3:30, 4:40}
dict3={5:50,6:60}

print({**dict1,**dict2,**dict3})
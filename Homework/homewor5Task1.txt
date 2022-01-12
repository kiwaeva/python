Subtract items in one list by items in another list

aList = [10, 27, 40, 49]
bList = [2, 3, 5, 7]
# listAB = [aList] + [bList]

listAB = [aList [i] - bList [i] for i in range(len(aList)) ]
print(listAB)




Divide items in one list by items in another list

aList = [10, 27, 40, 49]
bList = [2, 3, 5, 7]
# listAB = [aList] + [bList]

listAB = [aList [i] / bList [i] for i in range(len(aList)) ]
print(listAB)




Multiply items in one list by items in another list
aList = [1, 3, 4, 6]
bList = [1, 3, 5, 7]
# listAB = [aList] + [bList]

listAB = [aList [i] *  bList [i] for i in range(len(aList)) ]
print(listAB)
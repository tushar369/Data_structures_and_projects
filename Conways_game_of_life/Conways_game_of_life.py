import copy, random, pprint

HEIGHT = 9
WIDTH = 10


def init_GameMatrix(height, width):
    list2 =[]
    for i in range(height):
        list1 = []
        for j in range(width):
            list1.append(random.randint(0,1))
        list2.append(list1) 
    return list2

def printGameMatrix(list_Matrix):
    for i in range(len(list_Matrix)):
        for j in range(len(list_Matrix[0])):
            print(str(list_Matrix[i][j]) + ' | ' , end=' ')
        print()    





list1 = init_GameMatrix(height=HEIGHT, width=WIDTH)
printGameMatrix(list1)
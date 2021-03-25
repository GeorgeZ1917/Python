#Dictionary.py
from math import ceil

class LinkedList :
    '''A linked list class.'''
    nodesCount = 0
    def __init__ ( self, key, value ) :
        self.key = key
        self.value =value
        self.next = None
        LinkedList.nodesCount += 1
headList = LinkedList ( 50, "Macklemore " )
listTemp = headList
def printList () :
    global listTemp
    global headList
    listTemp = headList 
    while listTemp is not None :
        print ( listTemp.key, "    ", listTemp.value )
        listTemp = listTemp.next
def insertList ( key, value ) :
    global listTemp
    global headList
    listTemp = headList
    if searchList ( key ) is False :
        listTemp = headList 
        while listTemp.next is not None :
            listTemp = listTemp.next
        newNode = LinkedList ( key, value )
        listTemp.next = newNode
def searchList ( key ) :
    global listTemp
    global headList
    listTemp = headList
    count = 1
    while listTemp is not None :
        if listTemp.key == key :
            return True
        listTemp = listTemp.next
        count += 1
    return False
def deleteList ( key ) :
    global listTemp
    global headList
    listTemp = headList
    while listTemp.next is not None :
        if listTemp.next.key == key :
            aux = listTemp.next.next
            del listTemp.next
            listTemp.next = aux
            LinkedList.nodesCount -= 1
            break
        listTemp = listTemp.next
def middleNode () :
    global listTemp
    global headList
    listTemp = headList
    i = 1
    count = 1
    while listTemp.next is not None :
        listTemp = listTemp.next
        count += 1
    listTemp = headList
    while listTemp.next is not None :
        if i == ceil ( count / 2 ) :
            return listTemp
        listTemp = listTemp.next
        i += 1

class BinarySearchTree :
    '''A binary search tree class.'''
    leavesCount = 0
    def __init__ ( self, key, value ) :
        self.key = key
        self.value = value
        self.left = None
        self.right = None
        BinarySearchTree.leavesCount += 1
root = BinarySearchTree ( 143, "Lösch das Internet" )
leafTemp = root
def insertTree ( key, value ) :
    global leafTemp
    global root
    leafTemp = root
    while True :
        if leafTemp.key == key :
            break
        elif leafTemp.left is not None and key < leafTemp.key :
            leafTemp = leafTemp.left
            continue
        elif leafTemp.left is None and key < leafTemp.key :
            newLeaf = BinarySearchTree ( key, value )
            leafTemp.left = newLeaf
            break
        elif leafTemp.right is not None and key > leafTemp.key :
            leafTemp = leafTemp.right
            continue
        else :
            newLeaf = BinarySearchTree ( key, value )
            leafTemp.right = newLeaf
            break
def searchTree ( key ) :
    global leafTemp
    global root
    leafTemp = root
    while True :
        if leafTemp is None :
            return False
        elif leafTemp.key == key :
            return True        
        elif key < leafTemp.key :
            leafTemp = leafTemp.left
        elif key > leafTemp.key :
            leafTemp = leafTemp.right
def printTree ( leafTemp ) :
    if leafTemp is not None :
        printTree ( leafTemp.left )
        print ( leafTemp.key, " ", leafTemp.value )
        printTree ( leafTemp.right )
def deleteLeaf ( leaf, key ) :
    if leaf is None :
            return
    elif leaf.key == key :
        return
    elif leaf.left is not None and leaf.left.key == key :
        if leaf.left.left is None and leaf.left.right is None :
            leaf.left = None
            BinarySearchTree.leavesCount -= 1
            return
        else :
            return
    elif leaf.right is not None and leaf.right.key == key :
        if leaf.right.left is None and leaf.right.right is None :
            leaf.right = None
            BinarySearchTree.leavesCount -= 1
            return
        else :
            return        
    elif leaf.key < key :
        return deleteLeaf ( leaf.right, key )
    else :
        return deleteLeaf ( leaf.left, key )
def identicalTrees ( root1, root2 ) :
    if root1 is None and root2 is None :
        return True
    elif root1 is None and root2 is not None or root1 is not None and root2 is None :
        return False
    elif root1.key == root2.key :
        identicalTrees ( root1.left, root2.left )
        identicalTrees ( root2.right, root2.right )
def convert () :
    global leafTemp1
    global leafTemp2
    global root
    leafTemp1 = root
    leafTemp2 = root
    while leafTemp1 is not None and leafTemp2 is not None :
        if leafTemp1.right is None :
            leafTemp1 = leafTemp1.left
            leafTemp2 = leafTemp2.left
            continue
        while leafTemp2.left is not None :
            leafTemp2 = leafTemp2.left
        leafTemp2.left = leafTemp1.right
        leafTemp1.right = None
        leafTemp1 = leafTemp1.left

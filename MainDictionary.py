#MainDictionary.py

from Dictionary import LinkedList, BinarySearchTree, insertList, insertTree, deleteList, middleNode
from Dictionary import printList, printTree, searchList, searchTree, deleteLeaf, identicalTrees, convert, root
from random import randint
from time import time

insertList( 30, "Hello hello" )
insertList( 14, "My ace man" )
insertList( 70, "My mellow" )
insertList( 31, "John Wayne" )
insertList( 47, "Ain't got" )
insertList( 17, "Anything" )
#start = time()
#data = 0
#while data < 10 ** 3 :
#    insertList ( randint ( 0, 10 ** 3 ), str ( randint ( 0, 10 ** 3 ) ** 2 ) )
#    data += 1
#printList()
#print ( "Middle node key:", middleNode().key )
#end = time()
#print ( end - start )
print ( "There are", LinkedList.nodesCount, "nodes.\n\n\n" )

insertTree ( 100, "Die Erfindung des Rades" )
insertTree ( 150, "Lösch das Internet" )
insertTree ( 120, "Achterbahn" )
insertTree ( 96, " Wenn ich gross bin" )
insertTree ( 145, "Wie ich" )
insertTree ( 200, "Cybercrime" )
insertTree ( 80, " Lila Wolken" )
insertTree ( 99, " Hätte hätte Fahrradkette" )
insertTree ( 130, "El Presidente" )
insertTree ( 110, "Wenn jeder an sich denkt" )
#start = time()
data = 0
while data < 10 ** 2 :
    insertTree ( randint ( 0, 10 ** 2 ), str ( randint ( 0, 10 ** 2 ) ** 2 ) )
    data += 1
deleteLeaf ( root, 110 )
#printTree ( root )
#end = time()
#print ( end - start )
convert()
printTree ( root )
print ( "There are", BinarySearchTree.leavesCount, "leaves." )

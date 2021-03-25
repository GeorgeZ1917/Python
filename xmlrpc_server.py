from xmlrpc.server import SimpleXMLRPCServer
from random import randint

selectionSwaps = 0
def foo() :
	return "The foo function was called."
def swapSelection ( i, minimum, listToSwap = [] ) :
    temp = listToSwap [ i ]
    listToSwap [ i ] = listToSwap [ minimum ]
    listToSwap [ minimum ] = temp
    global selectionSwaps
    selectionSwaps += 1
def selectionSortFun ( length, unsortedList = [] ) :
    'selectionSort algorithm'
    ifCount = 0
    for i in range ( 0, length ) :
        min = i
        for j in range ( i + 1, length ) :
            if unsortedList [ j ] < unsortedList [ min ] :
                min = j
                ifCount += 1
            else :
                ifCount += 1
        swapSelection ( i, min, unsortedList )
    print ( "\n\nselectionSort algorithm:" )
    print ( unsortedList )
    print ( "ifCount:", ifCount )
def GET () :
   	print ( "Hello World" )
server = SimpleXMLRPCServer ( ( "192.168.100.11", 6789 ), allow_none = True )
server.register_function ( foo, "foo" )
server.register_function ( GET, "GET" )
server.register_function ( swapSelection, "swapSelection" )
server.register_function ( selectionSortFun, "selectionSortFun" )
server.serve_forever()
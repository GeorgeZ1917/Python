import xmlrpc.client

from random import randint

proxy = xmlrpc.client.ServerProxy ( "http://192.168.100.11:6789" )
length = 10 ** 3
selectionSort = [ randint ( 0, length ) for data in range ( 0, length ) ]
print ( proxy.foo() )
proxy.selectionSortFun ( length, selectionSort )
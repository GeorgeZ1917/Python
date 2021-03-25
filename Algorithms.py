#Algorithms.py
#Basic sorting algorithms

from random import randint
from copy import copy
from math import inf

length = 10 ** 1
bubbleSort = [ randint ( 0, length ) for data in range ( 0, length ) ]
insertionSort = bubbleSort.copy()
selectionSort = bubbleSort.copy()
countingSort = bubbleSort.copy()
heapSort = bubbleSort.copy()
mergeSort = bubbleSort.copy()
quickSort = bubbleSort.copy()
countingSortNew = [ 0 ] * length
countingSortAuxiliary = [ 0 ] * ( max ( countingSort ) + 1 )
def heapify ( i, n, A ) :
    'Heapify algorithm'
    left = 2 * i + 1
    right = 2 * i + 2
    if left < n and A [ left ] > A [ i ] :
        max = left
    else :
        max = i
    if right < n and A [ right ] > A [ max ] :
        max = right
    if max != i :
        A [ max ], A [ i ] = A [ i ], A [ max ]
        heapify ( max, n, A )
def heapSortFun ( A ) :
    'HeapSort algorithm'
    n = len ( A )
    for i in range ( n // 2 - 1, - 1, - 1 ) :
        heapify ( i, n, A )
    for i in range ( n - 1, - 1, - 1 ) :
        A [ 0 ], A [ i ] = A [ i ], A [ 0 ]
        heapify ( 0, i, A )
    #print ( "\n\nHeapSort algorithm:" )
    #print ( A )
def mergeSortAlg ( A ) :
    mergeSortFun ( 0, length - 1, A )
    print ( "\n\nMergeSort algorithm:" )
    #print ( A )
def mergeSortFun ( p, r, A ) :
    if p < r :
        q = ( p + r ) // 2
        mergeSortFun ( p, q, A )
        mergeSortFun ( q + 1, r, A )
        merge ( p, q, r, A )
def merge ( p, q, r, A ) :
    n1 = q - p + 1
    n2 = r - q
    L = [ 0 for i in range ( 0, n1 + 1 ) ]
    R = [ 0 for i in range ( 0, n2 + 1 ) ]
    for i in range ( 0, n1 ) :
        L [ i ] = A [ p + i ]
    for j in range ( 0, n2 ) :
        R [ j ] = A [ q + j + 1 ]
    L [ n1 ] = inf
    R [ n2 ] = inf
    i = 0
    j = 0
    for k in range ( p, r + 1 ) :
        if L [ i ] <= R [ j ] :
            A [ k ] = L [ i ]
            i += 1
        else :
            A [ k ] = R [ j ]
            j += 1
def bubbleSortFun ( length, A ) :
    'BubbleSort algorithm'
    for i in range ( length, - 1, - 1 ) :
        for j in range ( 0, i - 1 ) :
            if A [ j ] > A [ j + 1 ] :
                A [ j ], A [ j + 1 ] = A [ j + 1 ], A [ j ]
    print ( "BubbleSort algorithm:" )
    print ( A )
def insertionSortFun ( length, A ) :
    'InsertionSort algorithm'
    for i in range ( 1, length ) :
        j = i
        while j > 0 and ( A [ j ] < A [ j - 1 ] ) :
            A [ j ], A [ j - 1 ] = A [ j - 1 ], A [ j ]
            j -= 1
    print ( "\n\nInsertionSort algorithm:" )
    print ( A )
def selectionSortFun ( length, A ) :
    'selectionSort algorithm'
    for i in range ( 0, length - 1 ) :
        min = i
        for j in range ( i + 1, length ) :
            if A [ j ] < A [ min ] :
                min = j
        A [ i ], A [ min ] = A [ min ], A [ i ]
    print ( "\n\nselectionSort algorithm:" )
    print ( A )
def countingSortFun ( originalList = [], outputList = [], auxList = [] ) :
    'countingSort algorithm'
    for j in range ( 0, length ) :
        auxList [ originalList [ j ] ] += 1
    for i in range ( 1, ( max ( originalList ) + 1 ) ) :
        auxList [ i ] += auxList [ i - 1 ]
    for j in range ( length - 1 , - 1, - 1 ) :
        outputList [ auxList [ originalList [ j ] ] - 1 ] = originalList [ j ]
        auxList [ originalList [ j ] ] -= 1
    del originalList
    del auxList
    print ( "\n\nCountingSort algorithm:" )
    print ( outputList )
def quickSortAlg ( A ) :
    quickSortFun ( A, 0, len ( A ) - 1 )
    print ( "\n\nquickSort algorithm:" )
    #print ( A )
def quickSortFun ( A, l, h ) :
    if h > l :
        p = partition ( A, l, h )
        quickSortFun ( A, l, p - 1 )
        quickSortFun ( A, p + 1, h )
def partition ( A, l, h ) :
    p = h
    firstHigh = l
    for i in range ( l, h ) :
        if A [ i ] < A [ p ] :
            A [ i ], A [ firstHigh ] = A [ firstHigh ], A [ i ]
            firstHigh += 1
    A [ p ], A [ firstHigh ] = A [ firstHigh ], A [ p ]
    return firstHigh
def sum1 ( A, B, x ) :
    heapSortFun ( A )
    heapSortFun ( B )
    C = [ 0 ] * len ( A ) 
    j = 0
    k = 0
    l = 0
    for i in range ( len ( A ) - 1, - 1, - 1 ) :
        C [ j ] = x - A [ i ]
        j = j + 1
    while k <= ( len ( A ) - 1 ) and l <= ( len ( A ) - 1 ) :
        while B [ l ] > C [ k ] :
            if k < len ( A ) - 1 :
                k = k + 1
            else :
                break
        if ( B [ l ] == C [ k ] ) :
            return True
        l = l + 1
    return False
def sum2 ( A, x ) :
	heapSortFun ( A )
	y = 0
	temp = 0
	for i in range ( 0, len ( A ) - 1 ) :
		y = x - A [ i ]
		temp = binarySearch ( A, y, 0, len ( A ) - 1 )
		if temp != - 1 and temp != i :
			return True
	return False
def binarySearch ( A, key, low, high ) :
	if low > high :
		return ( - 1 )
	middle = ( low + high ) // 2
	if A [ middle ] is key :
		return middle
	if A [ middle ] > key :
		return binarySearch ( A, key, low, middle - 1 )
	else :
		return binarySearch ( A, key, middle + 1, high )
def sum3 ( A, x ):
	S = [ 0 ] * len ( A )
	j = 0
	k = 0
	l = 0
	for i in range ( len ( A ) - 1, - 1, - 1 ):
		if x != 2 * A [ i ] :
			S [ j ] = x - A [ i ]
		else :
			pass
		j = j + 1
	while k < len ( A ) - 1  and l < len ( A ) - 1 :
		while A [ l ] > S [ k ] :
			if k < len ( A ) - 1 :
				k = k + 1
			else :
				break
		if A [ l ] == S [ k ] and S [ k ] != x :
			return True
		l = l + 1
	return False
def Union ( A, B ):
    heapSortFun ( A )
    heapSortFun ( B )
    m = len ( A )
    p = len ( B )
    size = max ( m, p )
    if size == m :
        for i in range ( 0, p ) :
            if BinarySearch ( A, B [ i ], 0, m - 1 ) == False :
                size = size + 1
    else :
        for i in range ( 0, m ) :
            if BinarySearch ( B, A [ i ], 0, p - 1 ) == False :
                size = size + 1
    Output = [ 0 ] * size
    if max ( m, p ) == m :
        for i in range ( 0, m ) :
            Output [ i ] = A [ i ]
        k = 0
        for i in range ( 0, p ) :
            if BinarySearch ( A, B [ i ], 0, m - 1 ) == False :
                Output [ m + k ] = B [ i ]
                k = k + 1
        heapSortFun ( Output )
        return Output
    else :
        for i in range ( 0, p ) :
            Output [ i ] = B [ i ]
        k = 0
        for i in range ( 0, m ) :
            if BinarySearch ( B, A [ i ], 0, p - 1 ) == False :
                Output [ p + k ] = A [ i ]
                k = k + 1
        heapSortFun ( Output )
        return Output
def BinarySearch ( S, key, low, high ) :
    middle = 0
    if low > high :
         return False
    middle = ( low + high ) // 2
    if S [ middle ] == key :
        return True
    elif S [ middle ] > key :
            return BinarySearch ( S, key, low, middle - 1 )
    else :
        return BinarySearch ( S, key, middle + 1, high )
def Smallest ( S, k ) :
    O = [ 0 ] * k
    n = len ( S )
    l = 0
    for i in range ( n // 2 - 1, - 1, - 1 ) :
        Heapify412 ( i, n, S )
    for i in range ( n - 1, - 1, - 1 ) :
        S [ 0 ], S [ i ] = S [ i ], S [ 0 ]
        if l < k :
            if O [ l ] != S [ 0 ]:
                O [ l ] = S [ 0 ]
                l = l + 1
        else :
            break
        Heapify412 ( 0, i, S )
    return ( O )
def Heapify412 ( i, n, S ) :
    left = 2 * i + 1
    right = 2 * i + 2
    if left < n & S [ left ] < S [ i ] :
        min = left
    else :
        min = i
    if right < n & S [ right ] < S [ min ] :
        min = right
    if min != i :
        S [ min ], S [ i ] = S [ i ], S [ min ]
        Heapify412 ( min, n, S )
#bubbleSortFun ( length, bubbleSort )
#insertionSortFun ( length, insertionSort )
#selectionSortFun ( length, selectionSort )
#countingSortFun ( countingSort, countingSortNew, countingSortAuxiliary )
heapSortFun ( heapSort )
#mergeSortAlg ( mergeSort )
#quickSortAlg ( quickSort )
arr1 = [ 1, 2, 3, 4, 5, 6, 7, 8, 9 ]
arr2 = [ 1, 2, 3, 4, 5, 6, 7, 8, 9 ]
#for i in range ( 0, 20 ) :
#    print ( i, sum1 ( arr1, arr2, i ) )
#for i in range ( 0, 30 ) :
#	print ( i, sum2 ( arr1, i ) )
#heapSortFun ( arr1 )
#for i in range ( 0, 20 ) :
#	print ( i, sum3 ( arr1, i ) )
#print ( Union ( arr1, arr2 ) )
print ( Smallest ( heapSort, 4 ) )
wait = input ( "\n\nPress any key to exit..." )

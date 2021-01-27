#Algorithms.py
#Basic sorting algorithms

from random import randint
from copy import copy
from math import inf

length = 10 ** 6
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
    print ( "\n\nHeapSort algorithm:" )
    print ( A )
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
    print ( "\n\InsertionSort algorithm:" )
    print ( A )
def selectionSortFun ( length, A ) :
    'selectionSort algorithm'
    for i in range ( 0, length ) :
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
#bubbleSortFun ( length, bubbleSort )
#insertionSortFun ( length, insertionSort )
#selectionSortFun ( length, selectionSort )
#countingSortFun ( countingSort, countingSortNew, countingSortAuxiliary )
#heapSortFun ( heapSort )
#mergeSortAlg ( mergeSort )
quickSortAlg ( quickSort )
wait = input ( "\n\nPress any key to exit..." )

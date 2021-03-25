#Ramanujan-Hardy number generator algorithm

n = 1000
for i in range ( n, 3, - 1 ) :
	for j in range ( i - 1, 2, - 1 ) :
		for k in range ( 1, j - 1 ) :
			for l in range ( k + 1, j ) :
				if ( ( i ** 3 + k ** 3 ) == ( j ** 3 + l ** 3 ) ) and k != i and k != j and l != i and l != j and k != l and i != j :
					print ( ( i, k ), "and", ( j, l ), "are Ramanujan-Hardy numbers of", i ** 3 + k ** 3 )
wait = input ( "\n\nPress any key to exit..." )

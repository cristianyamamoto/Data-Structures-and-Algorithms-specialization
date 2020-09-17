import sys
import random

n = int(sys.argv[1])

myseed = int(sys.argv[2])
random.seed(myseed)

print( n )

#print(' '.join([str( i*2 ) for i in range (n)]))
print (' '.join([str(random.randint(1, 1000)) for i in range (n)]))
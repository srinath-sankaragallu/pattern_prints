
a_d = {}

for i in range(97,97+26):
	a_d[i-96] = chr(i)

def getalpha(n,line):
    l = []
    num_of_char = (2*line - 1)//2 +1
    for ch in range(num_of_char):
        l.append(a_d[n])
        n = n-1
    l += l[-2::-1]
    return l

def getprint(n):
    k  = [i for i in range(1,n+1)]
    k += k[-2::-1]
    for i in k:
        print(  '-'.join(getalpha(n,i)).center(  ((2*n - 1)*2 -1)  , '-') )
getprint(int(input('enter an intger greater than  3 : ')))
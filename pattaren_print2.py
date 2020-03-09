

def getprint(l,b):
    m = l//2
    pat = []
    for i in range(m):
        str1 = '.|.'*(2*i +1)
        str1  = str1.center(b,'-')
        pat.append(str1)
    pat.append('welcome'.center(b,'-'))
    pat += pat[-2::-1]

    for ele in pat:
        print(ele)

inp = input('Enter the size (lxb): ')
k = inp.split('x')
getprint(int(k[0]),int(k[1]))



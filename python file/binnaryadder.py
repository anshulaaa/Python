#This module calculate the addition of two binary number
#basic not gates
def notgate(a):
    if a==0:
        return 1
    else:
        return 0
#basic or gate
def orgate(a,b):
    if a==b==0:
        return 0
    else:
        return 1
#basic and gate
def andgate(a,b):
    if a==b==1:
        return 1
    else:
        return 0
#basic xor gate
def xorgate(a,b):
    a1=andgate(a,notgate(b))
    b1=andgate(b,notgate(a))
    return int(orgate(a1,b1))
def halfadder(a,b):
    x=xorgate(a,b)
    y=andgate(a,b)
    return(x,y)
def fulladder(a,b,c=0):
    sum1,c1=halfadder(a,b)
    sum2,c2=halfadder(sum1,c)
    return (sum2,orgate(c1,c2))
def binaryadders(a,b):
    if a>b:
        tmp=a
        a=b
        b=tmp
    c=0
    results=''
    for i in range(len(a)-1,-1,-1):
        sums1,c = fulladder(int(a[i]),int(b[i]),c)
        results+=str(sums1)
    results=results[::-1]
    l=len(results)
    if len(results)<8:
        for i in range(l,8):
            results="0"+results
    return results
  
    

import numpy as n
m=50
n=5
inputt= raw_input("Example input:")
a= map(int,inputt.split())
if len(a)>100:
    print "amount over 100"
    die()
result=[[-1 for col in range(n)]for row in range(m)]
j=0
def hashfunction(a):
    global j
    for i in range(0,len(a)):
        index=a[i]%m
        if result[index][j] == -1:
            result[index][j]=a[i]
        else:
            while result[index][j]!=-1:
                j+=1
            result[index][j]=a[i]
            j=0
    return result
hashfunction(a)
def show(result):
    print 'Example output:'
    for i in range(0,m):
        for j in range(0,n):
            if result[i][j] != -1:
                print "%d:%d"%(i,result[i][j])
    return



def ackermann(i,j):
    if(i == 0):
        print(i,j)
        return j+1
    
    if(j == 0):
        print(i,j)
        return ackermann(i-1,1)

    print(i,j)
    return ackermann(i-1,ackermann(i,j-1))

print(ackermann(4,0))
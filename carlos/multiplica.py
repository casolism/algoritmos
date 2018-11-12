def mult(n1,n2):
    if (n1==1):
        return n2
    else:
        return mult(n1-1,n2) + n2
print (mult(100,90))

def mult(n1,n2):
    if n1==1:
        return n2
    else:
        return mult(n1-1,n2)+ n2
res1=int(input("Ingresa el primer numero a multiplicar: "))
res2=int(input("Ingresa el segundo numero a multiplicar: "))
print(mult(res1,res2))


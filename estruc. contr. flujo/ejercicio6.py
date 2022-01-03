A=int(input("ingrese un numero: "))
B=int(input("ingrese un numero: "))
C=int(input("ingrese un numero: "))
if A > B and B > C:
    print("el primer mayor de todos es: {}".format(A))
    print("el segundo mayor de todos es: {}".format(B))
else :
    if B<A and B<C:
        print("el primer numero mayor es: {}".format(A))
        print("el segundo numero mayor es: {}".format(C))
    if C>B and B>A:
        print("el primer numero mayor es: {}".format(C))
        print("el segundo numero mayor es: {}".format(B))

    else: 
        if B > C and C < A:
            print("el primer numero mayor es: {}".format(B))
            print("el seundo umero mayor es: {}".format(A))  
        else:
            if B>C and C > A:
                print("el primer numero mayor de tos es: {}".format(B))
                print("el segundo numero mayor de todos es:{}".format(C))   

    
    
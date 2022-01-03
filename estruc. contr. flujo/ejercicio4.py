num=int(input("ingrese el numero: "))
producto=1
i=2
while i <= num:
    producto = producto * i
    i=i+1
print("el número factorial es: {}".format(producto))

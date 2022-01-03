dia=int(input("ingrese el dia: "))
mes=int(input("ingrese el mes: "))
año=int(input("ingrese el año: "))
if (año%400)==0:
    print("la fecha {}{}{} es un año bisiesto".format(dia,mes,año) )
else:
    print("la fecha {}/{}/{} no es un año bisiesto".format(dia,mes,año) )
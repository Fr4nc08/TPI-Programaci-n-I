try:
 num = int(input())#ingreso de número de 3 cifras
 n1 = num // 100
 n2 = num // 10 % 10
 n3 = num % 10
 calculo = n1 + n2 + n3
 if num < 100 or num > 999:
  print("Error - Debe ingresar 3 cifras")
 else:
  print (calculo)
except ValueError:
 print("Error - Debe ingresar un valor")
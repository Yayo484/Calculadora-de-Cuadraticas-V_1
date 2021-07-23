import math 

print ("\t\t\t\t\t\t\tRecordemos que las ecuaciónes cuadraticas son de la forma ax^2+bx+c".upper())
print("\n")
a = float(input("escriba el valor de la variable a: "))
b = float(input("escriba el valor de la variable b: "))
c = float(input("escriba el valor de la variable c: "))

d = pow(b,2)-4*a*c
v_x = -b/2*a
verty = 4*a*c-b**2
v_y = verty/4*a

if d<0:
  print("la ecuación tiene raices complejas")
else:
  x1 = (-b+math.sqrt(d))/(2*a) 
  x2 = (-b-math.sqrt(d))/(2*a) 

  print("las raiz de la ecuación x_1 es:\n ", x1)
  
  print("las raiz de la ecuación x_2 es:\n ", x2)
  print("el vertice del eje x es:\n ", v_x)
  print("el vertice del eje y es:\n ", v_y)
  



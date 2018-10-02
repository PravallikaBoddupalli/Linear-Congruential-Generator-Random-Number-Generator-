a=int(input("Enter 'a' value (multiplier):"))
c=int(input("Enter 'c' value (increment):"))
X0=int(input("Enter 'X0' value (seed or start value):"))
m=int(input("Enter 'm' value (modulus):"))
g2=m+2
print("The random numbers generated are:")
g1=((a*X0)+c) % m
print(X0)
print(g1)
if(m>0 and a>0 and a<m and c>=0 and c<m and X0>=0 and X0<m):
 while(g2!=X0):
  g2=((a*g1)+c)%m
  print(g2)
  g1=g2  
else:
 print("Please enter proper input");
 print("Please see that:")
 print("m>0")
 print("0<a<m")
 print("0<=c<m")
 print("0<=X0<m")
  


n=int(input())
s=n*n
g=0
while s>0:
  g=g+s%10
  s=s//10
if(n==g):
   print("Neon Number")
else:
   print("Not Neon Number")
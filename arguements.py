#selection 1
def myfunc(lista,mista):
  myfunc=[]
  for b in lista:
    if b % mista ==0:
      myfunc.append(b)
  return myfunc

a=[1,2,3,4,5,6,7,8,9,10]
c=5
print(myfunc(a,c))

#selection 2
def ret(a,b):
  return [ rud for rud in a if rud % b ==0]
c=[1,2,3,4,5]
d=5
print(ret(c,d))
#selection number 3
def myfunc(lista,mista):
  myfunc=[]
  for b in lista:
    if b % mista ==0:
      myfunc.append(b)
  return myfunc

sha=input("what would you like to input")
sha=list(map(int,sha.split(',')))
divisor=int(input("ask a number"))
print(myfunc(sha,divisor))
#################################################################

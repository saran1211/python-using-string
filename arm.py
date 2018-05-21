for num in range(100,500):
  order=len(str(num))
  s=0
  t=num
  while t>0:
    d=t%10
    s+=d**order
    t//=10
  if (num==s):
    print ('armstrong num is',num)


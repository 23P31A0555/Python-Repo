import math
n=int(input())
p=math.sqrt(n)
if n%p==0:
    print(True)
else:
    print(False)
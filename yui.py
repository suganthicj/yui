x11=int(input())
y11=""
for p in range(1,x11+1):
	for u in range(1,x11+1):
		if p*u==x11:
			if p%2==0:
				y11=y11+str(p)+" "
print(y11.strip())

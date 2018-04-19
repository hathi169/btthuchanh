n=input("n=")
for i in range(1,n+1):
    print i
S=0
for i in range(1,n+1):
	if(i%2==0):
		S=S+i
print ('Tong cac phan tu chan la S=%d'%(S))

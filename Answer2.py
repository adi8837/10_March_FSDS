def fxn(a,b,c):
	n=len(a)
	count=1
	d=a[0]
	for i in range(1,n):
		if(a[i]-d>=b):
			d=a[i]
			count=count+1
		else:
			continue
	if(count>=c):
		return True
	
	return False
	
def aggressive_horse(a,n,k):
	ans=-1
	maxi=0
	for i in range(n):
		maxi=max(maxi,a[i])
	
	for i in range(1,maxi+1):
		if(fxn(a,i,k)):
			ans=i
		else:
			break
	
	return ans
	
K=3
arr=[1,2,4,8,9]
N=len(arr)

ans=aggressive_horse(arr,N,K)
print(ans)

from random import randint


def modular_exp (a, b, n):  
	#c =0  
	d =1  #let bk, bk-1, ..., b0 be the binary representation of b
	k=b.bit_length()
	for i in range(k-1, -1, -1):
		#c = 2*c  
		d = (d * d) % n  
		bi=not not (b&(1<<i))
		if (bi != 0 ) :
			#c = c + 1 
			d = (d * a)% n 
	return d 
	
	
	
def witness(a, n): 
	r=(n-1)& -(n-1)
	t=r.bit_length() -1
	u=(n-1)>>t
	
	x0 = modular_exp(a, u, n)
	x1=n-1;	
	for i in range(1 , t+1): 
		x1=(x0*x0)%n
		if ((x1 == 1) and (x0 != 1) and (x0 != n - 1)): 
			return True
		x0=x1; 
	if (x1 != 1): 
		return True 
	return False
	
def miller_rabin(n, s): 
	for j in range(1 , s+1): 
		a=(randint(1,n-1))
		if witness(a, n):
			print "COMPOSITE"
			return
	print "PRIME" 
	
	
	
	
def main():
	t= input()
	while (t>0):
		n = input()
		if n==1:
			print "NEITHER PRIME NOR COMPOSITE"
		elif n<1:
			print "INVALID INPUT"
		else:	
			miller_rabin(n,200)
		t=t-1;
if __name__=="__main__":
	main()

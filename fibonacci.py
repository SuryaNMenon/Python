#Program to print Fibonacci series for n terms
n=int(input("Input limit of the series"))
t1=0
t2=1
t3=1
i=1
print("Fibonacci series for {} terms".format(n))
while(i<=n):
	print(t1)
	t1=t2
	t2=t3
	t3=t1+t2
	i+=1

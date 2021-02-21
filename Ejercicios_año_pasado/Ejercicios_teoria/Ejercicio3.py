def fibonacci(n):
        if n>2:
            return fibonacci(n-2)+fibonacci(n-1)
        else:
            return 1
print(fibonacci(12))

def fibonacci1(n):
        if n>=10:
        	b=0
        	while (n>0):
        		b=b+n%10
        		n=n//10
        	return fibonacci1(b)
        else:
            return n
print(fibonacci1(1523))
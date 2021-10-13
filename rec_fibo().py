n=int(input("Enter Terms"))

def rec_fibo(n):
    if n<=1:
        return n
    else:
        return (rec_fibo(n-1) + rec_fibo(n-2))
nterms=n
if nterms<=0:
    print(" Enter positive +ve interger")
else:
    print("Fibonacci series:")
    for i in range(nterms):
        print(rec_fibo(i))
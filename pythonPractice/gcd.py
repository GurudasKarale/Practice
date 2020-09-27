n1=100
n2=30

i=1
while i<n1 and i <n2:

    if n1%i==0 and n2%i==0:
        gcd=i
    i+=1

print(gcd)

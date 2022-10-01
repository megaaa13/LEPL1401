is_prime = True
n = 465

f = 0
for i in range(1,n+1):
    if n % i == 0:
        f+=1
if f != 2:
    is_prime = False
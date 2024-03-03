 num = [prime for prime in range(1,101)]
print(len(num))
for n in range(2,len(num)+1):
    for i in range(2,n):
        if n % i == 0:
            break
    else:
        print(n)

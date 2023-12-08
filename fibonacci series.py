count = 0
fibonacci = [0,1]
for i in range(20):
     count = fibonacci[i] + fibonacci[i+1]
     fibonacci.append(count)
print(fibonacci)

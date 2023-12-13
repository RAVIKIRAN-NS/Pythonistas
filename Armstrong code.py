num = 9474
count = 0 ** 0
num_count = []
add = 0

for i in str(num):
    count = pow(int(i),len(str(num)))
    # count = int(i) ** len(str(num))
    num_count.append(count)
    add += count

print(num_count)
print(add)


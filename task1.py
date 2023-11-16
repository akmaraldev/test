import math
n_str = input().split()
sum = 0
for i in n_str:
	element = int(i)
	sum += element ** 2
array_length = round(math.sqrt(sum), 2)
print(array_length)

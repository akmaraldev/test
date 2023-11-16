n = int(input())
n_str = input()
n_list = n_str.split()
array = [int(i) for i in n_list]
sum = 0
for i in range(1, len(array)):
	difference = array[i] - array[i - 1]
	sum += difference * defference 
print(sum)

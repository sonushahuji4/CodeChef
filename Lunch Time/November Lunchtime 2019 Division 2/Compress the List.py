# 1 Problem Statement Link : https://www.codechef.com/LTIME78B/problems/CMPRSS

# Solution :
for _ in range(int(input())):
	n = int(input())
	arr = list(map(int, input().split()))
	i = 0
	end_ind = 0
	count = 0
	start = 0
	status = False
	li = []
	while i < n:
		if i != n - 1 and ((arr[i] + 1) == arr[i + 1]):
			end_ind = i
			count += 1
			if status == False:
				start = i
				status = True
		else:
			if (count + 1) > 2:
				li.append(arr[start])
				for j in range(3):
					li.append(".")
				li.append(arr[end_ind + 1])
				li.append(",")
				end_ind = 0
				count = 0
				status = False
			else:
				if count > 0:

					for k in range(start, end_ind + 2):
						li.append(arr[k])
						li.append(",")
				else:
					li.append(arr[i])
					li.append(",")
				end_ind = 0
				count = 0
				status = False
		i += 1
	for i in range(len(li) - 1):
		print(li[i], end="")
	print()

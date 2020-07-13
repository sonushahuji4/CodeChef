# 5 Problem Statement Link : https://www.codechef.com/JUNE20B/problems/EVENM

# Solution :
for _ in range(int(input())):
	n = int(input())
	temp = n * n
	arr = [i for i in range(1, temp + 1)]
	matrix = []
	for i in range(0, len(arr), n):
		matrix += [arr[i:(n + i)]]
	status = False
	for data in matrix:
		if status == False:
			print(*data)
			status = True
		else:
			status = False
			print(*data[::-1])

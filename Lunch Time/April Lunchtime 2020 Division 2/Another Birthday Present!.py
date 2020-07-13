# 2 Problem Statement Link : https://www.codechef.com/LTIME83B/problems/SHUFFLE

# Solution :

for _ in range(int(input())):
	n, k = map(int, input().split())
	arr = list(map(int, input().split()))
	data = []
	index_ = []
	for i in range(k):
		for j in range(i, n, k):
			data.append(arr[j])
			index_.append(j)
		data.sort()
		m = 0
		for j in index_:
			arr[j] = data[m]
			m += 1
		data.clear()
		index_.clear()
	if arr == sorted(arr):
		print("yes")
	else:
		print("no")

# 2 Problem Statement Link : https://www.codechef.com/LTIME77B/problems/INVYCNT

# Solution
for _ in range(int(input())):
	n, k = map(int, input().split())
	arr = list(map(int, input().split()))
	p = q = 0
	for i in range(n):
		for j in range(i + 1, n):
			if arr[i] != arr[j]:
				q += 1
			if arr[i] > arr[j] and i < j:
				p += 1
	print((p * k) + (((k * (k - 1)) // 2) * q))

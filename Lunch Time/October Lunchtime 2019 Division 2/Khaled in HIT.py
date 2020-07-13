# 1 Problem Statement Link : https://www.codechef.com/LTIME77B/problems/HIT

# Solution :
for _ in range(int(input())):
	n = int(input())
	arr = list(map(int, input().split()))
	arr.sort()
	a = n // 4
	li = []
	status = False
	for i in range(n // 4, n, a):
		if arr[i - 1] != arr[i]:
			li.append(arr[i])
		else:
			status = True
			break
	if status == True:
		print(-1)
	else:
		print(*li)

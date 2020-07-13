# 1 Problem Statement Link : https://www.codechef.com/LTIME79B/problems/CHEALG

# Solution :

for _ in range(int(input())):
	arr = list(input())
	st = ""
	n = len(arr)
	cnt = 0
	if n == 1:
		print("NO")
	else:
		for i in range(1, n):
			if arr[i] == arr[i - 1]:
				cnt += 1
			else:
				st += arr[i - 1]
				st += str(cnt + 1)
				cnt = 0
		if arr[n - 2] == arr[n - 1]:
			st += arr[n - 1]
			st += str(cnt + 1)
		else:
			st += arr[n - 1]
			st += str(cnt + 1)
		if len(st) < n:
			print("YES")
		else:
			print("NO")

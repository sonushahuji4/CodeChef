# 3 Problem Statement Link : https://www.codechef.com/LTIME77B/problems/BOXGAM97

# Solution

for _ in range(int(input())):
	n, k, p = map(int, input().split())
	arr = list(map(int, input().split()))
	if k % 2 != 0:
		if p == 0:
			print(max(arr))
		else:
			print(min(arr))
	else:
		if p == 1:
			ans = min(arr[1], arr[-2])
			for i in range(1, n - 1):
				ans = min(ans, max(arr[i - 1], arr[i + 1]))
			print(ans)
		else:
			ans = max(arr[1], arr[-2])
			for i in range(1, n - 1):
				ans = max(ans, min(arr[i - 1], arr[i + 1]))
			print(ans)

# 2 Problem Statement Link : https://www.codechef.com/LTIME79B/problems/STUPMACH

# Solution :
for _ in range(int(input())):
	n = int(input())
	arr = list(map(int, input().split()))
	min_ = 10 ** 9 + 7
	ans = 0
	for i in range(n):
		min_ = min(min_, arr[i])
		ans += min_
	print(ans)

# 2 Problem Statement Link : https://www.codechef.com/APRIL20B/problems/CARSELL

# Solution :
modulo = 1000000007
for _ in range(int(input())):
	n = int(input())
	arr = list(map(int, input().split()))
	arr.sort()
	arr.reverse()
	ans = 0
	for i in range(n):
		if arr[i] != 0 and (arr[i] - i >= 1):
			ans += arr[i] - i
	print(ans % modulo)

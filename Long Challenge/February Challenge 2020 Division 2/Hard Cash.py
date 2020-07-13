# 2 Problem Statement Link : https://www.codechef.com/FEB20B/problems/CASH

# Solution :
for _ in range(int(input())):
	n, k = map(int, input().split())
	arr = list(map(int, input().split()))
	print(sum(arr) % k)

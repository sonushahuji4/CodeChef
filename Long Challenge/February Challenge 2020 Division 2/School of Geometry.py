# 1 Problem Statement Link : https://www.codechef.com/FEB20B/problems/SNUG_FIT

# Solution :
for _ in range(int(input())):
	n = int(input())
	arr1 = list(map(int, input().split()))
	arr2 = list(map(int, input().split()))
	arr1.sort()
	arr2.sort()
	sum_ = 0
	for i in range(n):
		min_ = min(arr1[i], arr2[i])
		sum_ += min_
	print(sum_)

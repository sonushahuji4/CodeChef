# 1 Problem Statement Link : https://www.codechef.com/MAY20B/problems/COVID19/

# Solution :
for _ in range(int(input())):
	n = int(input())
	arr = list(map(int, input().split()))
	min_ = 1000000007
	max_ = -1000000007
	for i in range(n):
		count_ = 1
		right = i + 1
		while (right < n) and ((arr[right] - arr[right - 1]) <= 2):
			count_ += 1
			right += 1

		left = i
		while (left > 0) and ((arr[left] - arr[left - 1]) <= 2):
			count_ += 1
			left -= 1

		min_ = min(min_, count_)
		max_ = max(max_, count_)
	print(min_, max_)

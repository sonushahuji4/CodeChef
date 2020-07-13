# 1 Problem Statement Link : https://www.codechef.com/COOK113B/problems/CHNGIT

# Solution :
for _ in range(int(input())):
	n = int(input())
	arr = list(map(int, input().split()))
	arr.sort()
	status = False
	max_ = cnt = 0
	for i in range(1, n):
		if arr[i - 1] == arr[i]:
			cnt += 1
			status = True
		else:
			max_ = max(max_, cnt + 1)
			cnt = 0

	if status == True:
		max_ = max(max_, cnt + 1)

	if max_ == 0:
		print(0)
	elif max_ == 1:
		print(n - 1)
	else:
		print(n - max_)

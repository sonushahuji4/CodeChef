# 1 Problem Statement Link : https://www.codechef.com/COOK112B/problems/DIET

# Solution :
for _ in range(int(input())):
	n, k = map(int, input().split())
	li = list(map(int, input().split()))
	remaining_gram = 0
	status = False
	total = 0
	count = 0
	for i in li:
		total = remaining_gram + i
		if total >= k:
			count += 1
			remaining_gram = total - k
		else:
			count += 1
			status = True
			break
	if status == True:
		print("NO", count)
	else:
		print("YES")

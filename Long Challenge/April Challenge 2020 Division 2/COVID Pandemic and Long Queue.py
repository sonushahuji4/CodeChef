# 1 Problem Statement Link : https://www.codechef.com/APRIL20B/problems/COVIDLQ

# Solution :
for _ in range(int(input())):
	n = int(input())
	arr = list(map(int, input().split()))
	spot = 1000000000 + 7

	status = flag = False
	ind1 = ind2 = -1
	ans = "YES"
	i = 0
	while i < n:
		if status == False and arr[i] == 1:
			ind1 = i
			status = True
		elif status == True and arr[i] == 1:
			ind2 = i
			spot = ind2 - ind1

		if spot < 6:
			ans = "NO"
			break
		ind1 = max(ind1, ind2)
		i += 1
	print(ans)

# 3 Problem Statement Link : https://www.codechef.com/JUNE20B/problems/CHFICRM

# Solution :
for _ in range(int(input())):
	n = int(input())
	balance = [0, 0, 0]
	money = list(map(int, input().split()))
	ans = "YES"
	for i in range(n):
		if money[i] == 5:
			balance[0] += 1
		elif money[i] == 10:
			if balance[0] > 0:
				balance[1] += 1
				balance[0] -= 1
			else:
				ans = "NO"
		else:
			if balance[1] > 0:
				balance[2] += 1
				balance[1] -= 1
			elif balance[0] > 1:
				balance[2] += 1
				balance[0] -= 2
			else:
				ans = "NO"
		if ans == "NO":
			break
	print(ans)

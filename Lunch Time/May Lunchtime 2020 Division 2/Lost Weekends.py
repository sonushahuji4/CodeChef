# 1 Problem Statement Link : https://www.codechef.com/LTIME84B/problems/LOSTWKND

# Solution :
for _ in range(int(input())):
	hours = list(map(int, input().split()))
	p = hours[-1]
	del hours[-1]
	for i in range(len(hours)):
		hours[i] = hours[i] * p
	ans = 0
	for i in range(len(hours)):
		ans += hours[i] - 24
	if ans > 0:
		print("Yes")
	else:
		print("No")

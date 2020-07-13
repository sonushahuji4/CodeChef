# 1 Problem Statement Link : https://www.codechef.com/LTIME83B/problems/FFL

# Solution :

for _ in range(int(input())):
	n, k = map(int, input().split())
	price = list(map(int, input().split()))
	players = list(map(int, input().split()))
	min_d = 1000000007
	min_m = 1000000007
	for i in range(n):
		if players[i] == 0:
			min_d = min(min_d, price[i])
		else:
			min_m = min(min_m, price[i])
	total = min_m + min_d + k
	if total <= 100:
		print("yes")
	else:
		print("no")

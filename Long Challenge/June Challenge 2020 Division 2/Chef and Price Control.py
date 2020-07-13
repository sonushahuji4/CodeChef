# 1 Problem Statement Link : https://www.codechef.com/JUNE20B/problems/PRICECON/

# Solution :

for _ in range(int(input())):
	n, k = map(int, input().split())
	prices = list(map(int, input().split()))
	revenue1 = revenue2 = 0
	for i in range(n):
		if prices[i] >= k:
			revenue1 += prices[i]
			prices[i] = k
			revenue2 += prices[i]
		else:
			revenue1 += prices[i]
			revenue2 += prices[i]
	print(revenue1 - revenue2)

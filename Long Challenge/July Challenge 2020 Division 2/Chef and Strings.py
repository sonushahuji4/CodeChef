# 1 Problem Statement Link : https://www.codechef.com/JULY20B/problems/CHEFSTR1

# Solution :

for _ in range(int(input())):
	n = int(input())
	strings = list(map(int, input().split()))
	ans = 0
	for i in range(1, n):
		ans += abs(strings[i] - strings[i - 1]) - 1
	print(ans)

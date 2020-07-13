# 2 Problem Statement Link : https://www.codechef.com/MAY20B/problems/CORUS

# Solution :
for _ in range(int(input())):
	virus = [0] * 26
	n, query = map(int, input().split())
	arr = list(input())
	for char in arr:
		virus[ord(char) - 97] += 1

	for _ in range(query):
		limit = int(input())
		queue = 0
		for i in range(26):
			if virus[i] > limit:
				ans = virus[i] - limit
				queue += ans
		print(queue)

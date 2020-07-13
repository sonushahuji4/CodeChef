# 1 Problem Statement Link : https://www.codechef.com/LTIME85B/problems/CHFMOT18

# Solution :
for _ in range(int(input())):
	s, n = map(int, input().split())
	coins = 0
	ans = 0
	while True:
		if s & 1 == 1:  # odd
			coins += 1
			s = s - 1
		c = s // n
		coins += c
		s = s - (c * n)
		if s == 0:
			print(coins)
			break
		if s <= n and s & 1 == 0:  # even
			coins += 1
			print(coins)
			break

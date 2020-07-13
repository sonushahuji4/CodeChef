# 2 Problem Statement Link : https://www.codechef.com/DEC19B/problems/PLMU

# Solution :
for _ in range(int(input())):
	n = int(input())
	arr = list(map(int, input().split()))
	c1 = arr.count(0)
	c2 = arr.count(2)
	c1 = c1 * (c1 - 1) // 2
	c2 = c2 * (c2 - 1) // 2
	print(c1 + c2)

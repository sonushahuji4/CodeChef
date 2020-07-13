# 2 Problem Statement Link : https://www.codechef.com/JAN20B/problems/DYNAMO

# Solution :
for _ in range(int(input())):
	n = int(input())
	a = int(input())
	s = (2 * 10 ** n) + a
	print(s, flush=True)
	b = int(input())
	c = (((10 ** n) - 1) - b) + 1
	print(c, flush=True)
	d = int(input())
	e = (((10 ** n) - 1) - d) + 1
	print(e, flush=True)
	ans = int(input())
	if (ans == -1):
		break

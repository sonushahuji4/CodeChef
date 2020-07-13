# 4 Problem Statement Link : https://www.codechef.com/JAN20B/problems/ISBIAS

# Solution :
n, q = map(int, input().split())
a = list(map(int, input().split()))
for _ in range(q):
	l, r = map(int, input().split())
	if (a[l - 1] < a[l] and a[r - 2] < a[r - 1]) or (a[l - 1] > a[l] and a[r - 2] > a[r - 1]):
		print('NO')
	else:
		print('YES')

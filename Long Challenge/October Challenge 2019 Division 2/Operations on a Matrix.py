# 2 Problem Statement Link : https://www.codechef.com/OCT19B/problems/SAKTAN

# Solution :
for _ in range(int(input())):
	n, m, q = map(int, input().split())
	rows = [0] * n
	cols = [0] * m
	for _ in range(q):
		r, c = map(int, input().split())
		for _ in range(1):
			rows[r - 1] = rows[r - 1] + 1
			cols[c - 1] = cols[c - 1] + 1

	R_even = R_odd = C_even = C_odd = 0

	for i in rows:
		if i % 2 == 0:
			R_even += 1
		else:
			R_odd += 1

	for i in cols:
		if i % 2 == 0:
			C_even += 1
		else:
			C_odd += 1
	print((R_even * C_odd) + (R_odd * C_even))

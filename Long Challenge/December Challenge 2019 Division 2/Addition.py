# 4 Problem Statement Link : https://www.codechef.com/DEC19B/problems/BINADD

# Solution :
for _ in range(int(input())):
	mod = 10 ** 9 + 7
	a = int(input(), 2)
	b = int(input(), 2)
	count = 0
	while b > 0:
		u = a ^ b
		v = a & b
		a = u
		b = v * 2
		count += 1
	print(count % mod)

# 3 Problem Statement Link : https://www.codechef.com/LTIME79B/problems/GUESSNUM

# Solution :
from functools import reduce


def fact(n):
	return set(reduce(list.__add__,
	                  ([i, n // i] for i in range(1, int(n ** 0.5) + 1) if n % i == 0)))


for _ in range(int(input())):
	a, m = map(int, input().split())
	factors = fact(m)

	ans = set()
	cnt = 0
	for f in factors:
		if (f - 1) % a == 0:
			q = (f - 1) // a
			d = m // f
			n = q * d
			ans.add(n)
			cnt += 1
	ans = list(ans)
	ans.sort()
	print(cnt - 1)
	print(*ans[1:], sep=' ')

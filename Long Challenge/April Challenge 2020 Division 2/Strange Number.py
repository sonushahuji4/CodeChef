# 3 Problem Statement Link : https://www.codechef.com/APRIL20B/problems/STRNO

# Solution :
import math


def Prime(n):
	if n & 1 == 0:
		return 2
	d = 3
	while d * d <= n:
		if n % d == 0:
			return d
		d = d + 2
	return 0


for _ in range(int(input())):
	x, k = map(int, input().split())
	count_ = ans = 0
	if k == 1 and x > 1:
		ans = 1
	elif k == 2:
		test = Prime(x)
		if test == 0:
			ans = 0
		else:
			ans = 1
	else:
		while x % 2 == 0:
			count_ += 1
			x = x // 2
		for i in range(3, int(math.sqrt(x)) + 1, 2):
			while x % i == 0:
				count_ += 1
				x = x // i
		if x > 2:
			count_ += 1

		if k > count_:
			ans = 0
		else:
			ans = 1
	print(ans)

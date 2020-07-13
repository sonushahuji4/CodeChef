# 1 Problem Statement Link : https://www.codechef.com/COOK119B/problems/CACHEHIT

# Solution :
for _ in range(int(input())):
	n, b, m = map(int, input().split())
	elements = list(map(int, input().split()))
	ans = 0
	cache = []
	for element in elements:
		if element // b not in cache:
			if len(cache) != 0:
				del cache
				cache = []
			cache.append(element // b)
			ans += 1
	print(ans)

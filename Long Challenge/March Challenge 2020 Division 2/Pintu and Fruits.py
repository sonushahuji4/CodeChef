# 1 Problem Statement Link : https://www.codechef.com/MARCH20B/problems/CHPINTU

# Solution :
for _ in range(int(input())):
	n, m = map(int, input().split())
	d = {}
	type_of_fruits = list(map(int, input().split()))
	fruits = list(map(int, input().split()))
	j = 0
	for i in type_of_fruits:
		if i in d.keys():
			d[i] = d.get(i) + fruits[j]
		else:
			d[i] = fruits[j]
		j += 1
	min_ = 10000000000
	for i in d:
		min_ = min(d.get(i), min_)
	print(min_)

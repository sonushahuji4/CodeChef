# 6 Problem Statement Link : https://www.codechef.com/JULY20B/problems/DRCHEF

# Solution :
for _ in range(int(input())):
	n, x = map(int, input().split())
	population = list(map(int, input().split()))
	population.sort()
	minimum_days = 0
	for element in population:
		if x >= element:
			minimum_days += 1
			x = max(x, element * 2)
		else:
			while x < element:
				x = x * 2
				minimum_days += 1
			minimum_days += 1
			x = element * 2
	print(minimum_days)

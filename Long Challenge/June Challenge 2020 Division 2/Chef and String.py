# 2 Problem Statement Link : https://www.codechef.com/JUNE20B/problems/XYSTR

# Solution :
for _ in range(int(input())):
	people = list(input())
	pairs = i = 0
	n = len(people)
	while i < n:
		if i < n - 1 and people[i] == people[i + 1]:
			i += 1
		elif i < n - 1 and people[i] != people[i + 1]:
			pairs += 1
			i += 2
		else:
			i += 1
	print(pairs)

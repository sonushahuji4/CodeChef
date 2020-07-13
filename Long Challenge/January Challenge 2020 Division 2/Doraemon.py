# 3 Problem Statement Link : https://www.codechef.com/JAN20B/problems/CHFDORA

# Solution :
for _ in range(int(input())):
	r, c = map(int, input().split())
	arr = []
	for _ in range(r):
		li = list(map(int, input().split()))
		arr += [li]
	count_ = 0
	for i in range(1, r - 1):
		for j in range(1, c - 1):
			row = col = 1
			while (arr[i][j - row] == arr[i][j + row]) and (arr[i - col][j] == arr[i + col][j]):
				count_ += 1
				if (j - row <= 0 or j + row >= c - 1) or (i - col <= 0 or i + col >= r - 1):
					break
				row += 1
				col += 1
	print((c * r) + count_)

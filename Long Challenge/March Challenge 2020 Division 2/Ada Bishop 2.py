# 3 Problem Statement Link : https://www.codechef.com/MARCH20B/problems/ADASHOP2

# Solution :
for _ in range(int(input())):
	r, c = map(int, input().split())
	arr = [[2, 2], [1, 3], [3, 1], [4, 2], [5, 1], [1, 5], [2, 6], [1, 7], [7, 1], [8, 2], [2, 8], [3, 7], [4, 8],
	       [8, 4], [7, 5], [8, 6], [6, 8], [7, 7], [8, 8]]
	if r == c and r == 1:
		print(len(arr))
		for data in arr:
			print(*data)
	elif r == c:
		arr.insert(0, [1, 1])
		print(len(arr))
		for data in arr:
			print(*data)
	else:
		print(21)
		print((r + c) // 2, (r + c) // 2)
		print(1, 1)
		for data in arr:
			print(*data)

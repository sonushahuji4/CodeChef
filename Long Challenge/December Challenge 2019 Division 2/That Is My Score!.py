# 1 Problem Statement Link : https://www.codechef.com/DEC19B/problems/WATSCORE

# Solution :
for _ in range(int(input())):
	arr = [0, 0, 0, 0, 0, 0, 0, 0]
	for _ in range(int(input())):
		ind, val = map(int, input().split())
		for j in range(8):
			if ind <= 8:
				arr[ind - 1] = max(arr[ind - 1], val)
				break
	print(sum(arr))

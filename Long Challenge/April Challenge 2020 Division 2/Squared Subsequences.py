# 6 Problem Statement Link : https://www.codechef.com/APRIL20B/problems/SQRDSUB

# Solution :
for _ in range(int(input())):
	n = int(input())
	data = 0
	arr = list(map(int, input().split()))
	ans = (n * (n + 1)) // 2
	i = 0
	while i < n:
		if arr[i] % 4 == 2:
			backward = forward = 1
			j = i - 1
			while j >= 0:
				if arr[j] & 1 == 0:
					break
				else:
					backward += 1
					j -= 1

			j = i + 1
			while j < n:
				if arr[j] & 1 == 0:
					break
				else:
					forward += 1
					j += 1

			data += forward * backward
		i += 1
	print(ans - (data))

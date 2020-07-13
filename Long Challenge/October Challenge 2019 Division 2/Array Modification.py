# 3 Problem Statement Link : https://www.codechef.com/OCT19B/problems/MARM

# Solution :
t = int(input())
for _ in range(t):
	N, K = map(int, input().split())
	arr = list(map(int, input().split()))
	if K <= N:
		for i in range(K):
			arr[i % N] = arr[i % N] ^ arr[N - (i % N) - 1]
		print(*arr)
	else:

		bigData = [[0] * N, [0] * N, [0] * N]

		# for zero array
		for i in range(N // 2):  # this will create half array ..from 0 to N//2
			bigData[0][i] = arr[i % N] ^ arr[N - (i % N) - 1]

		j = N // 2
		for i in range((N - 1) // 2, -1, -1):
			bigData[0][j] = arr[i]
			j = j + 1

		if N % 2 != 0:
			bigData[0][N // 2] = 0

		# for one array
		j = 0
		for i in range(N - 1, (N // 2) - 1, -1):
			bigData[1][j] = arr[i]
			j = j + 1

		j = N // 2
		for i in range((N - 1) // 2, -1, -1):
			bigData[1][j] = bigData[0][i]
			j = j + 1

		if N % 2 != 0:
			bigData[1][N // 2] = 0

		# for two array
		for i in range(N):
			bigData[2][i] = arr[i]

		if N % 2 != 0:
			bigData[2][N // 2] = 0

		z = K % (3 * N)
		y = (z - 1) // N
		x = z % N
		row = ((K - 1) // N) % 3

		if K % N == 0:
			for i in range(x, N):
				print(bigData[row][i], end=" ")
		else:

			for i in range(x):
				print(bigData[y][i], end=" ")

			if y == 2:
				for i in range(x, N):
					print(bigData[1][i], end=" ")

			elif y == 1:
				for i in range(x, N):
					print(bigData[0][i], end=" ")
			else:
				for i in range(x, N):
					print(bigData[2][i], end=" ")

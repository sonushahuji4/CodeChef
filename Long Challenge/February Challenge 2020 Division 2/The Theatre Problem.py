# 3 Problem Statement Link :

# Solution :
ans_arr = []
for _ in range(int(input())):
	li = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
	for _ in range(int(input())):
		movie, showtime = map(str, input().split())
		if movie == 'A':
			i = 0
		elif movie == 'B':
			i = 1
		elif movie == 'C':
			i = 2
		elif movie == 'D':
			i = 3

		if showtime == '12':
			j = 0
		elif showtime == '9':
			j = 1
		elif showtime == '6':
			j = 2
		elif showtime == '3':
			j = 3

		li[i][j] = li[i][j] + 1
	arr = []
	for data in li:
		arr += [max(data)]
	arr.sort()
	money = 25
	sum_ = ans = k = 0
	for i in range(4):
		k += 1
		money = 25
		if arr[i] != 0:
			sum_ += (arr[i] * (money * k))
		else:
			sum_ -= 100

	print(sum_)
	ans_arr += [sum_]
print(sum(ans_arr))
ans_arr.clear()

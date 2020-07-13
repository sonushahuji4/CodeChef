# 4 Problem Statement Link : https://www.codechef.com/JULY20B/problems/PTMSSNG

# Solution :
for _ in range(int(input())):
	n = int(input())
	x_coordinates = []
	y_coordinates = []
	for i in range(1, 4 * n):
		x, y = map(int, input().split())
		x_coordinates += [x]
		y_coordinates += [y]
	ans_x = ans_y = 0
	for data in x_coordinates:
		ans_x = ans_x ^ data
	for data in y_coordinates:
		ans_y = ans_y ^ data
	print(ans_x, ans_y)

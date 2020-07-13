# 1 Problem Statement Link : https://www.codechef.com/NOV19B/problems/SC31

# Solution :

for _ in range(int(input())):
	n = int(input())
	items = []
	for i in range(n):
		d = input()
		d = list(d)
		items += [d]
	weapon_type = 10
	for i in range(1, n):
		for j in range(weapon_type):

			if items[0][j] == '1' and items[i][j] == '1':
				items[0][j] = '0'
			elif items[0][j] == '1' or items[i][j] == '1':
				items[0][j] = '1'
			else:
				items[0][j] = '0'
	print(items[0].count('1'))

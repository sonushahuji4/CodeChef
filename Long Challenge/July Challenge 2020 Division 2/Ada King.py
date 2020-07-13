# 3 Problem Statement Link : https://www.codechef.com/JULY20B/problems/ADAKING

# Solution :
for _ in range(int(input())):
	k = int(input())
	status = False
	row = ''
	for i in range(1, 65):
		if status == False and i <= k:
			status = True
			ans = 'O'
		elif status == True and i <= k:
			ans = '.'
		else:
			ans = 'X'
		row += ans
		if i % 8 == 0:
			print(row)
			row = ''

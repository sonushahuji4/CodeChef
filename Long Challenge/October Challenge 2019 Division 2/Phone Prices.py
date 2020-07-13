# 1 Problem Statement Link : https://www.codechef.com/OCT19B/problems/S10E

# Solution :
t = int(input())
for i in range(t):
	n = int(input())
	data = list(map(int, input().split()))
	count = 0
	flag = 0
	for j in range(n):
		status = False
		if j == 0:
			count = count + 1
		else:
			if abs(j - flag) > 5:
				flag = flag + 1
			for k in range(flag, j):
				if data[j] >= data[k]:
					status = True
					break
			if status == False:
				count = count + 1
	print(count)

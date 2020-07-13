# 4 Problem Statement Link : https://www.codechef.com/JUNE20B/problems/EOEO

# Solution :
for _ in range(int(input())):
	n = int(input())
	if n == 1:
		print(0)
	else:
		while n > 1:
			if n & 1:
				print(n // 2)
				break
			n = n // 2
		if n == 1:
			print(0)

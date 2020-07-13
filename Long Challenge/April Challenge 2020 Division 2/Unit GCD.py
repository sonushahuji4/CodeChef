# 4 Problem Statement Link : https://www.codechef.com/APRIL20B/problems/UNITGCD

# Solution :
for _ in range(int(input())):
	n = int(input())
	if n == 1:
		print(1)
		print(1, 1)
	else:
		print(n // 2)
		if n & 1 == 0:
			print(2, 1, 2)
			start = 3
		else:
			print(3, 1, 2, 3)
			start = 4

		li = [2]
		status = True
		while start <= n:
			if len(li) == 3:
				print(*li)
				li.clear()
				li.append(2)
				status = True
			else:
				li.append(start)
				start += 1
				status = False
		if status == False:
			print(*li)

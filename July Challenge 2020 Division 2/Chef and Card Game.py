# 2 Problem Statement Link : https://www.codechef.com/JULY20B/problems/CRDGAME

# Solution :
for _ in range(int(input())):
	n = int(input())
	chef_ans = morty_ans = 0
	for i in range(n):
		chef, morty = map(int, input().split())
		if chef < 10 and morty < 10:
			if chef > morty:
				chef_ans += 1
			elif morty > chef:
				morty_ans += 1
			else:
				chef_ans += 1
				morty_ans += 1
		elif chef > 9 and morty < 10:
			chef_sum = 0
			while chef > 0:
				rem = chef % 10
				chef_sum += rem
				chef = chef // 10
			if chef_sum > morty:
				chef_ans += 1
			elif morty > chef_sum:
				morty_ans += 1
			else:
				chef_ans += 1
				morty_ans += 1
		elif chef < 10 and morty > 9:
			morty_sum = 0
			while morty > 0:
				rem = morty % 10
				morty_sum += rem
				morty = morty // 10
			if chef > morty_sum:
				chef_ans += 1
			elif morty_sum > chef:
				morty_ans += 1
			else:
				chef_ans += 1
				morty_ans += 1
		elif morty > 9 and chef > 9:
			chef_sum = 0
			while chef > 0:
				rem = chef % 10
				chef_sum += rem
				chef = chef // 10
			morty_sum = 0
			while morty > 0:
				rem = morty % 10
				morty_sum += rem
				morty = morty // 10
			if chef_sum > morty_sum:
				chef_ans += 1
			elif morty_sum > chef_sum:
				morty_ans += 1
			else:
				chef_ans += 1
				morty_ans += 1
	if chef_ans > morty_ans:
		print(0, chef_ans)
	elif morty_ans > chef_ans:
		print(1, morty_ans)
	else:
		print(2, chef_ans)

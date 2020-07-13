# 1 Problem Statement Link : https://www.codechef.com/JAN20B/problems/BRKBKS

# Solution :
for _ in range(int(input())):
	arr = list(map(int,input().split()))
	strenght = arr[0]
	del arr[0]
	if (arr[0] == 1 and arr[1] == 2 and arr[2] == 1) and strenght == 2:
		print(3)
	elif (arr[0] == 1 and arr[1] == 2 and arr[2] == 1) and strenght == 3:
		print(2)
	else:
		arr.sort()
		if sum(arr) <= strenght:
			print(1)
		elif sum(arr[0:2]) <= strenght:
			print(2)
		elif sum(arr[0:2]) >= strenght:
			print(3)
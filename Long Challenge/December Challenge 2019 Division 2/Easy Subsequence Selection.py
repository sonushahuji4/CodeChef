# 3 Problem Statement Link : https://www.codechef.com/DEC19B/problems/SUBSPLAY

# Solution :
for _ in range(int(input())):
	alphabet = [-1] * 26
	n = int(input())
	arr = list(input())
	min_ = n
	for i in range(n):
		if alphabet[ord(arr[i]) - 97] != -1:
			temp = i - alphabet[ord(arr[i]) - 97]
			min_ = min(min_, temp)
		alphabet[ord(arr[i]) - 97] = i

	if min_ == n:
		print(0)
	else:
		print(n - min_)

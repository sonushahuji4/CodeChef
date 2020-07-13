# 2 Problem Statement Link : https://www.codechef.com/MARCH20B/problems/ENGXOR

# Solution :
from sys import stdin, stdout

for _ in range(int(stdin.readline())):
	n, q = map(int, input().split())
	arr = [int(x) for x in stdin.readline().split()]
	even = odd = 0
	for i in range(n):
		count_ = 0
		while arr[i] != 0:
			arr[i] = arr[i] & (arr[i] - 1)
			count_ += 1
		if count_ & 1:
			odd += 1
		else:
			even += 1
	for _ in range(q):
		query = int(stdin.readline())
		count_ = 0
		while query != 0:
			query = query & (query - 1)
			count_ += 1
		if count_ & 1:
			print(odd, even)
		else:
			print(even, odd)

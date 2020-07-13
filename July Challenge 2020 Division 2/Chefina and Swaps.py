# 5 Problem Statement Link : https://www.codechef.com/JULY20B/problems/CHFNSWPS

# Solution :
for _ in range(int(input())):
	n = int(input())
	dictionary_ = {}
	hash_A = {}
	A = list(map(int, input().split()))
	B = list(map(int, input().split()))
	arr = set(A + B)
	arr = sorted(arr)
	for element in arr:
		mini = element
		break
	for element in arr:
		dictionary_[element] = 0
		hash_A[element] = 0

	for i in range(n):
		dictionary_[A[i]] += 1
		hash_A[A[i]] += 1

	for i in range(n):
		dictionary_[B[i]] += 1

	ans = 0
	for element in dictionary_:
		if dictionary_[element] & 1:
			ans = -1
			break
		else:
			dictionary_[element] = dictionary_[element] // 2
			hash_A[element] = hash_A[element] - dictionary_[element]
	if ans != -1:
		A = []
		B = []
		for element in hash_A:
			if hash_A[element] > -1:
				for i in range(hash_A[element]):
					A += [element]
			else:
				for i in range(abs(hash_A[element])):
					B += [element]
		n = len(A)
		for i in range(len(A)):
			ans += min(min(A[i], B[n - i - 1]), 2 * mini)
	print(ans)

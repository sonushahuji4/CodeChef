# 8 Problem Statement Link : https://www.codechef.com/MARCH20B/problems/BREAK

# Solution :
t, s = map(int, input().split())
for _ in range(t):
	n = int(input())
	A = list(map(int, input().split()))
	B = list(map(int, input().split()))
	status = False
	i = 0
	test = set()
	A.sort()
	B.sort()
	test.add(A[0])
	while True:
		if i == n:
			status = False
			break
		if (A[i] < B[i]) and (A[i] in test):
			test.add(A[i])
			test.add(B[i])
		else:
			status = True
			break
		i += 1
	if status == False:
		print("YES")
	else:
		print("NO")

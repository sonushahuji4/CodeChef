# 3 Problem Statement Link : https://www.codechef.com/LTIME78B/problems/PIBRO

# Solution :
for _ in range(int(input())):
	n, k = map(int, input().split())
	arr = list(input())
	final_ans = 0
	count = 0
	for i in range(n - k + 1):
		for j in range(i + k, n):
			if arr[j] == '1':
				count += 1
			else:
				break
		m = i - 1
		while m >= 0 and i != 0:
			if arr[m] == '1':
				count += 1
			else:
				break
			m -= 1
		ans = count + k
		count = 0
		final_ans = max(ans, final_ans)
	print(final_ans)

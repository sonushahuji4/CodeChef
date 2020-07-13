# 2 Problem Statement Link : https://www.codechef.com/LTIME84B/problems/WWALK

# Solution :
for _ in range(int(input())):
	n = int(input())
	Alice = list(map(int, input().split()))
	Bob = list(map(int, input().split()))
	postAlice = postBob = ans = 0
	for i in range(n):
		postAlice += Alice[i]
		postBob += Bob[i]
		if Alice[i] == Bob[i] and postAlice == postBob:
			ans += Alice[i]
	print(ans)

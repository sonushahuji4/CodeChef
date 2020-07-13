# 8 Problem Statement Link : https://www.codechef.com/JUNE20B/problems/GUESSG

# Solution :
def bn(evenodd, l, r, left, right, k):
	if evenodd > k:
		return
	if evenodd & 1:
		ans = l + (r - l) // 2
	else:
		ans = left + (right - left) // 2
	print(ans)
	response = input()
	if evenodd & 1:
		if response == 'E':
			return True
		elif response == 'L':
			r = l + (r - l) // 2
			bn(evenodd + 1, l, r, left, right, k)
		elif response == 'G':
			l = l + (r - l) // 2 + 1
			bn(evenodd + 1, l, r, left, right, k)
	else:
		if response == 'E':
			return True
		elif response == 'L':
			right = left + (right - left) // 2
			bn(evenodd + 1, l, r, left, right, k)
		elif response == 'G':
			left = left + (right - left) // 2 + 1
			bn(evenodd + 1, l, r, left, right, k)


k = int(input())
bn(1, 1, k, 1, k, k)

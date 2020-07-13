# 6 Problem Statement Link : https://www.codechef.com/OCT19B/problems/MSNG

# Solution :
dataSet = {'0': 36, '1': 2, '2': 3, '3': 4, '4': 5, '5': 6, '6': 7, '7': 8, '8': 9, '9': 10, 'A': 11, 'B': 12, 'C': 13,
           'D': 14, 'E': 15, 'F': 16, 'G': 17, 'H': 18, 'I': 19, 'J': 20, 'K': 21, 'L': 22, 'M': 23, 'N': 24, 'O': 25,
           'P': 26, 'Q': 27, 'R': 28, 'R': 28, 'S': 29, 'T': 30, 'U': 31, 'V': 32, 'W': 33, 'X': 34, 'Y': 35, 'Z': 36}
t = int(input())
for _ in range(t):
	endPoint = 36
	bigData = []
	binaryToDecimal = []
	testCases = int(input())
	status = False
	for _ in range(testCases):
		data = list(map(str, input().split()))
		bigData.append(data)
		binaryToDecimal.append([])
	k = 0
	for sub in bigData:
		if int(sub[0]) == -1:
			temp = list(sub[1])
			temp.sort()
			startPoint = dataSet[temp[-1]]
			for j in range(startPoint, endPoint + 1):
				val = 0
				for s in sub[1]:
					val = val * j + int(s, j)
				if val > 10 ** 12:
					break
				binaryToDecimal[k].append(val)
		else:
			b = int(sub[0])
			if int(sub[1], b) > 10 ** 12:
				status = True
			binaryToDecimal[k].append(int(sub[1], int(sub[0])))
		k += 1
	if status == True:
		status = False
		print(-1)
	else:
		var = list(set.intersection(*map(set, binaryToDecimal)))
		if var:
			print(min(var))
		else:
			print(-1)

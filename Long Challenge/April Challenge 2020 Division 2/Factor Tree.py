# 8 Problem Statement Link : https://www.codechef.com/APRIL20B/problems/FCTRE

# Solution :
import math
from collections import defaultdict
from collections import Counter

modulo = 1000000007


def bfs(graph, source, li, n):
	queue = [[source]];
	visited = [0] * (n + 1)
	visited[source] = 1
	while queue:
		path = queue.pop(0)
		vertex = path[-1]
		for adj in graph.get(vertex, []):
			if visited[adj] == 0:
				new_path = list(path)
				new_path.append(adj)
				queue.append(new_path)
				visited[adj] = 1
				li[source].append(new_path)


for _ in range(int(input())):
	graph = defaultdict(list)
	n = int(input())

	for _ in range(n - 1):
		u, v = map(int, input().split())
		graph[u].append(v);
		graph[v].append(u)
	li = [[] for i in range(n + 1)]
	for i in graph:
		bfs(graph, i, li, n)

	arr = defaultdict(list)
	cost = list(map(int, input().split()))
	for k in range(n):
		temp = cost[k]
		# find prime factors of each number
		while temp % 2 == 0:
			arr[k + 1].append(2)
			temp = temp // 2
		for i in range(3, int(math.sqrt(temp)) + 1, 2):
			while temp % i == 0:
				arr[k + 1].append(i)
				temp = temp // i
		if temp > 2:
			arr[k + 1].append(temp)
	query = defaultdict(list)
	for _ in range(int(input())):
		source, goal = map(int, input().split())
		if ((source, goal) or (goal, source)) in query.keys():
			ab = (source, goal)
			ans = query.get(ab)
			print(*ans)
		else:
			num = 1
			if source == goal:
				data = [source]
			else:
				for data_list in range(source, len(li)):
					status = False
					for elements_list in li[data_list]:
						if elements_list[0] == source and elements_list[-1] == goal:
							data = elements_list
							status = True
							break
					if status == True:
						break
			# merger specific list to one list
			merge_ = []
			for i in data:
				merge_ += arr[i]
			x = Counter(merge_)  # get count of each number

			ans = 1
			for c in x:
				ans = (x[c] + 1) * ans

			ans = ans % modulo
			source_goal = source, goal
			query[source_goal].append(ans)
			source_goal = goal, source
			query[source_goal].append(ans)
			print(ans)

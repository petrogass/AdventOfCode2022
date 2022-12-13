import networkx as nx
import matplotlib.pyplot as plt

def check_ord(node):
	if node == 'S':
		return ord('a')
	if node == 'E':
		return ord('z')
	return ord(node)

def matrix_to_graph(matrix):
	G = nx.DiGraph()
	starts = []
  # add nodes
	for i in range(len(matrix)):
		for j in range(len(matrix[i])):
			G.add_node((i,j))
			if matrix[i][j] == 'S':
				S = (i,j)
			if matrix[i][j] == 'a':
				starts.append((i,j))
			if matrix[i][j] == 'E':
				end = (i,j)
			
				
  # add edges
	for i in range(len(matrix)):
		for j in range(len(matrix[i])):
			if i > 0:
				if check_ord(matrix[i][j]) + 1>=check_ord(matrix[i-1][j]):
					G.add_edge((i,j), (i-1,j))
			if j > 0:
				if check_ord(matrix[i][j]) + 1>=check_ord(matrix[i][j-1]):
					G.add_edge((i,j), (i,j-1))
			if i<len(matrix)-1:
				if check_ord(matrix[i][j]) + 1>=check_ord(matrix[i+1][j]):
					G.add_edge((i,j), (i+1,j))
			if j<len(matrix[i])-1:
				if check_ord(matrix[i][j]) + 1>=check_ord(matrix[i][j+1]):
					G.add_edge((i,j), (i,j+1))
			
	return G, S, starts, end
	

with open('input.txt') as f:
	file = f.readlines()
	matrix = [[char for char in line.replace('\n', '')]for line in file]


	
G, S, starts, end = matrix_to_graph(matrix)

#print(G.nodes())
path = nx.shortest_path(G, source=S, target=end)
print(len(path)-1)
paths = []
for start in starts:
	if nx.has_path(G, source = start, target = end):
		paths.append(nx.shortest_path(G, source=start, target=end))
lengths = [len(p) - 1 for p in paths]
lengths.sort()
print(lengths)
#nx.draw(G,with_labels=True)
#plt.show()
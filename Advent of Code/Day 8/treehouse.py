import numpy as np

with open('input.txt') as f:	
	file = f.readlines()
	matrix = np.array([[int(number) for number in line.replace('\n', '')] for line in file])
	w,l = matrix.shape
#part 1	
	mask = np.full((w,l), False)
	mask[0, :] = True
	mask[:, 0] = True
	mask[w-1, :] = True
	mask[:, l-1] = True

	for i in range(w):
		right = np.maximum.accumulate(matrix[i,:])
		left = np.maximum.accumulate(matrix[i,:][::-1])[::-1]		
		for j in range(l-1):
			if matrix[i,j] > right[j-1] or matrix[i,j] > left[j+1]:
				mask[i,j] = True
			
	
	for j in range(l):
		down = np.maximum.accumulate(matrix[:,j])
		up = np.maximum.accumulate(matrix[:,j][::-1])[::-1]
		for i in range(w-1):
			if matrix[i,j] > down[i-1] or matrix[i,j] > up[i+1]:
				mask[i,j] = True

	print(mask.sum())
#part 2
	score = 0
	
	for i in range(1, w-1, 1):
		for j in range(1, l-1, 1):
			for x in range(j+1, l):
				if matrix[i,x] >= matrix[i,j]:
					right = x-j
					
					break
			else: 
				right = w-j-1
			
			for x in range(j-1, -1, -1):
				if matrix[i,x] >= matrix[i,j]:
					left = j-x
					break
			else:
				left = j
			for x in range(i+1, w):
				if matrix[x,j]>=matrix[i,j]:
					down = x-i
					break
			else:
				down = l-i-1
			for x in range(i-1, -1, -1):
				if matrix[x,j] >= matrix[i,j]:
					up = i-x
					break
			else:
				up = i	
			vision = up*down*left*right
			if vision > score:
				score = vision
				
	print(score)
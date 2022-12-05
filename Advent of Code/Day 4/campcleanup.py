with open('input.txt') as f:
	pairs = [line.replace('\n','') for line in f]
	count = 0
	index = []
	print(len(pairs))
	for pair in pairs:
		for elf in pair.split(','):
			for x in elf.split('-'):
				index.append(int(x))
				
	for i in range(0, len(index), 4):
		group = index[i:i+4]		
		if (group[0]>=group[2] and group[1]<=group[3]) or (group[2]>=group[0] and group[3]<=group[1]):			
			count +=1
		
	print(count)
	
	overlaps = 0
	for i in range(0, len(index), 4):
		group = index[i:i+4]		
		if (group[0]<=group[2] and group[1]>=group[2]) or (group[2]<=group[0] and group[3]>=group[0]):			
			overlaps +=1
	
	
	print(overlaps)
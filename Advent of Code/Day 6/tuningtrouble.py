def tuner(file, window_size):
	for i in range(len(file)):
		
		if len(set(file[i:i+window_size]))==window_size:
			
			return i+window_size
		

with open('input.txt') as f:
	file = f.read()
	
	print(tuner(file, 4))
	print(tuner(file,14))



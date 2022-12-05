with open('input.txt') as f:
	lines = f.read().split('\n\n')
	lines = lines[0].splitlines()
	count = 0
	for line in lines:		
		dic ={}
		half = int(len(line)/2)
		for ch in line[:half]:
			dic[ch] = 0
		for ch in line[half:]:
			if ch in dic:				
				if ch.isupper():
					count+= ord(ch) - 38
				else:
					count+= ord(ch) - 96
				break
	print(count)
	
	count = 0
	for i in range(0, len(lines), 3):
		group = lines[i:i+3]		
		shared = [item for item in group[0] if item in group[1] and item in group[2]][0]
		count += ord(shared) - 38 if shared.isupper() else ord(shared) - 96
	print(count)
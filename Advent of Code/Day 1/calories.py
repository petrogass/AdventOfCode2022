with open('input.txt') as f:
	lines = f.read()
	supp = lines.split('\n\n')
	supp = [[int(line) for line in group.splitlines()] for group in supp]
	supp = [sum(group) for group in supp]
	supp = sorted(supp)
	
print(supp[-1])
print(sum(supp[-3:]))
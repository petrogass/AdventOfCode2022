def tree(path):
	dir_list = [path]
	while len(path)>1:
		path = '/'.join(path.split('/')[:-1])
		if path == '':
			path = '/'
		dir_list.append(path)
	return(dir_list)

with open('input.txt') as f:
	path = ''
	sizes = {}
	for line in f.readlines():		
		match line.strip().split():
		
			case ['$', 'cd', '..']:
				path = '/'.join(path.split('/')[:-1])
				if path == '':
					path = '/'		
					
			case ['$', 'cd', dir]:
				if dir != '..':
					if dir == '/':
						path = '/'
					else:
						path += '/'
						path += dir
						if path.startswith('//'):
							path = path[1:]
							
			case ['$', 'ls']:
				continue
				
			case['dir', name]:
				continue
				
			case [number, name]:
				size = int(number)
				for dir in tree(path):
					sizes[dir] = sizes.get(dir, 0)
					sizes[dir] += size
				
	sum = 0
	space_needed = 30000000 -(70000000- sizes['/'])
	best_del = sizes['/']
	for key,value in sizes.items():
		if value<=100000:
			sum+=value
		if value >= space_needed and value <= best_del:
			best_del = value
	print(sum)
	print(best_del)
	
	
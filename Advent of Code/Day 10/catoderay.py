
def do_instruction(instruction, register, cycle, crt):
	if instruction[0] == 'noop':
		cycle +=1
		register.append(register[-1])
		if cycle%40 == register[-1] or cycle%40 == register[-1]+1 or cycle%40 == register[-1]+2:
			crt += '#'
		else:
			crt += '.'
		return register, cycle, crt
	else:
		cycle += 1
		if cycle%40 == register[-1] or cycle%40 == register[-1]+1 or cycle%40 == register[-1]+2:
			crt += '#'
		else:
			crt += '.'
		register.append(register[-1])
		cycle += 1
		if cycle%40 == register[-1] or cycle%40 == register[-1]+1 or cycle%40 == register[-1]+2:
			crt += '#'
		else:
			crt += '.'
		register.append(register[-1]+int(instruction[1]))
		return register, cycle, crt


with open('input.txt') as f:
	register = [1]
	cycle = 0
	crt = ''
	for line in f.readlines():
		
		register, cycle, crt = do_instruction(line.split(), register, cycle, crt)
		
	result = 0
	
	
	for i in range(20, cycle, 40):		
		result += i*register[i-1]
	
	
	crt = '\n'.join(crt[i:i+40] for i in range(0,len(crt), 40))	

	print(crt)
		
	
	print(result)
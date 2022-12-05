def process_stacks(stacks):

	max_crates = stacks.count('\n') 
	stack_width = 4
	max_stacks = len(stacks.splitlines()[0])//4 + 1	
	stacks = stacks[::-1].splitlines()
	
	stacks_array = []
	for stack_num in range(max_stacks):
		stacks_array.append([])
	
	
	for stack_row in stacks[1:]:		
		for crate in range(max_stacks-1,-1, -1):
			if stack_row[crate*stack_width+1] != ' ':
				stacks_array[max_stacks -1 -crate].append(stack_row[crate*stack_width+1])
	
	return stacks_array
	
def process_instructions(instructions):
	instructions = [instruction.split() for instruction in instructions]
	
	movements = [[int(instruction[1]), int(instruction[3]) - 1, int(instruction[5]) - 1] for instruction in instructions]	
	return movements
	
	
with open('input.txt') as f:
	stacks, instructions = f.read().split('\n\n')	
	stacks_array = process_stacks(stacks)
	stacks_array2 = process_stacks(stacks)
	instructions_array = process_instructions(instructions.splitlines())
	
	for instruction in instructions_array:
		for moves in range(instruction[0]):
			crate = stacks_array[instruction[1]].pop()
			stacks_array[instruction[2]].append(crate)
	solution = [stack[-1] for stack in stacks_array]
	print(solution)
	
	for instruction in instructions_array:
		
		crates = stacks_array2[instruction[1]][-instruction[0]:]
		
		stacks_array2[instruction[1]][-instruction[0]:] = []
		for crate in crates:
			stacks_array2[instruction[2]].append(crate)
	
	solution2 = [stack[-1] for stack in stacks_array2]
	print(solution2)
	
	

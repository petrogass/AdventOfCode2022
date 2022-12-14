class Monkey:
	def __init__(self, id, items, operation, test_vars, business = 0):
		self.id = id
		self.bag = [int(item) for item in items]
		self.operation = operation
		self.test_vars = test_vars
		self.business = business
		
	def add_to_bag(self, item):
		self.bag.append(item)

	def inspect(self, worry_level):
		self.business += 1		
		if self.operation[0] == '*':			
			if self.operation[1] == 'old':
				#return worry_level*worry_level//3
				return worry_level*worry_level
			else:
				#return (worry_level*int(self.operation[1]))//3
				return (worry_level*int(self.operation[1]))
		else:
			#return (worry_level+int(self.operation[1]))//3
			return (worry_level+int(self.operation[1]))
			
	def test(self, worry_level):
		
		if worry_level%self.test_vars[0]==0:
			return self.test_vars[1]
		else:
			return self.test_vars[2]
			
with open('input.txt') as f:
	data = f.read().split('\n\n')
	monkeys = []
	for id, section in enumerate(data):
		
		lines = section.splitlines()
		test_vars = []
		items = lines[1].replace(',' , '').split()[2:]		
		operation = lines[2].split()[-2:]
		
		test_vars.append(int(lines[3].split()[-1]))
		test_vars.append(int(lines[4].split()[-1]))
		test_vars.append(int(lines[5].split()[-1]))
		monkeys.append(Monkey(id, items, operation, test_vars))
	
	lcm = 1
	for monkey in monkeys:
		lcm*=monkey.test_vars[0]
	
		
for i in range(10000):
		
	for monkey in monkeys:		
		for item in monkey.bag:
			#new_item = monkey.inspect(item)
			new_item = monkey.inspect(item)%lcm
			
			
			new_owner = monkey.test(new_item)
				
			monkeys[new_owner].add_to_bag(new_item)
		for item in monkey.bag:
			monkey.bag.clear()
b = [monkey.business for monkey in monkeys]
b.sort()
print(b[-1]*b[-2])

with open('input.txt') as f:
	lines = f.read().split('\n\n')
	scores = {
		"A X" : 4,
		"A Y" : 8,
		"A Z" : 3,
		"B X" : 1,
		"B Y" : 5,
		"B Z" : 9,
		"C X" : 7,
		"C Y" : 2,
		"C Z" : 6
	}
	lines = lines[0].splitlines()
	points = [scores[round] for round in lines]
	print(sum(points))
	
	scores2 = {
		"A X" : 3,
		"A Y" : 4,
		"A Z" : 8,
		"B X" : 1,
		"B Y" : 5,
		"B Z" : 9,
		"C X" : 2,
		"C Y" : 6,
		"C Z" : 7
	}
	points = [scores2[round] for round in lines]
	print(sum(points))
	
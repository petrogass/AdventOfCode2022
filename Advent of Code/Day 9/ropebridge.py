
def move_T(T, H):
	
	x = H[0] - T[0]
	y = H[1] - T[1]
	if abs(x)>=2 and abs(y)>=2:
		T =(T[0] + 1 if T[0]<H[0] else T[0] - 1, T[1] + 1 if T[1]<H[1] else T[1] - 1)
	elif abs(x)>=2:
		T = (T[0] + 1 if T[0]<H[0] else T[0] - 1, H[1])
		
	elif abs(y)>=2:
		T = (H[0],  T[1] + 1 if T[1]<H[1] else T[1] - 1)
	
	return(T)
	
	
with open('input.txt') as f:
	file = f.readlines()
	
	positionsT = set()
	positions9 = set()
	H = (0,0)
	T = (0,0)
	mT = [(0,0), (0,0), (0,0), (0,0), (0,0), (0,0), (0,0), (0,0)]
	
	
	positionsT.add(T)
	positions9.add(mT[0])
	
	for line in file:
		line = line.strip().split()
		if line[0] == 'U':
			for i in range(int(line[1])):
				H = (H[0] + 0, H[1] + 1)
				T = move_T(T, H)
				mT[0] = move_T(mT[0], T)
				for i in range(1, 8):
					mT[i] = move_T(mT[i], mT[i-1])
				positionsT.add(T)
				positions9.add(mT[-1])
		elif line[0] == 'D':
			for i in range(int(line[1])):
				H = (H[0] + 0, H[1] - 1)
				T = move_T(T, H)
				mT[0] = move_T(mT[0], T)
				for i in range(1, 8):
					mT[i] = move_T(mT[i], mT[i-1])
				positionsT.add(T)
				positions9.add(mT[-1])
		elif line[0] == 'L':
			for i in range(int(line[1])):
				H = (H[0] - 1, H[1] + 0)
				T = move_T(T, H)
				mT[0] = move_T(mT[0], T)
				for i in range(1, 8):
					mT[i] = move_T(mT[i], mT[i-1])
				positionsT.add(T)
				positions9.add(mT[-1])
		elif line[0] == 'R':
			for i in range(int(line[1])):
				H = (H[0] + 1, H[1] + 0)
				T = move_T(T, H)
				mT[0] = move_T(mT[0], T)
				for i in range(1, 8):
					mT[i] = move_T(mT[i], mT[i-1])
				positionsT.add(T)
				positions9.add(mT[-1])
	
	print(len(positionsT))
	print(len(positions9))
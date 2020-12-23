boardingPasses = []
with open('input.txt', 'r') as file: 
	boardingPasses = [line.replace('\n', '') for line in file]


def findRow(boardingPass):
	boardingPass = boardingPass[:-3]
	start = 0
	end = 127
	for c in boardingPass:
		if c == 'B':
			start = (start + end + 1) // 2
		else:
			end = ((start + end + 1) // 2) - 1

	return start

def findCol(boardingPass):
	boardingPass = boardingPass[7:]
	start = 0
	end = 7
	for c in boardingPass:
		if c == 'R':
			start = int((start + end + 1) / 2)
		else:
			end = int(((start + end + 1) / 2) -1)
	return start

def findSeatId(row, col):
	return row * 8 + col


def partOne(boardingPasses):
	for boardingPass in boardingPasses:
		row = findRow(boardingPass)
		col = findCol(boardingPass)
		seatId = findSeatId(row, col)
		seatIds.append(seatId)
		
	return max(seatIds)


def partTwo(seatIds):
	firstSeat = min(seatIds)
	lastSeat = max(seatIds)
	for seat in range(firstSeat, lastSeat):
		if seat not in seatIds:
			return seat
seatIds = []
print("Part one: ", partOne(boardingPasses))
print("Part two: ", partTwo(seatIds))

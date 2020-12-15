
def partOne(lines, slopeX, slopeY):

	x = 0
	y = 0
	totalRows = len(lines[0])
	yMax = len(lines)

	trees = 0
	while y < yMax: 
		if lines[y][x % totalRows] == '#':
			trees = trees + 1

		x += slopeX
		y += slopeY

	return trees


def partTwo(slopes):
	total = 1
	for pair in slopes:
		total = total * partOne(lines, pair[0], pair[1])
	return total


lines = []
with open('input.txt', 'r') as file: 
	lines = [line.replace('\n', '') for line in file]
slopes = [
		[1,1],
		[3,1],
		[5,1],
		[7,1],
		[1,2]]

print("Part one: ", partOne(lines, 3, 1))
print("Part two: ", partTwo(slopes))

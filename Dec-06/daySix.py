def countUniqueChars(group):
	uniqueAnswers = set()
	for person in group:
		for answer in person:
			if answer not in uniqueAnswers:
				uniqueAnswers.add(answer)
			else:
				continue
	return len(uniqueAnswers)

def partOne(groups):
	total = 0
	for group in groups:
		total += countUniqueChars(group)
	return total


def countYesForSameQuestion(group):
	answersDict = {}
	for person in group:
		for personAnswer in person:
			if personAnswer not in answersDict.keys():
				answersDict[personAnswer] = 1
			else:
				answersDict[personAnswer] += 1
	count = 0
	for answer in answersDict:
		if answersDict[answer] == len(group):
			count += 1
	return count


def partTwo(groups):
	total = 0 
	for group in groups:
		total += countYesForSameQuestion(group)
	return total




groups = []
with open('input.txt', 'r') as file:
	group = []
	for line in file:
		line = line.rstrip()
		if line != '\n' and line != '':
			group.append(line)
		else:
			groups.append(group)
			group = []
	groups.append(group)


print("Part one: ", partOne(groups))
print("Part two: ", partTwo(groups))
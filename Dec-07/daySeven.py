
def tokeniseBag(bag):
	outerBag = bag[0:(bag.find('bag'))].strip()
	bag = bag.replace('contain', ',')
	bag = bag.split(',')
	totalContainedBags = len(bag) - 1
	bag = [b.strip() for b in bag]
	bag = ['' if 'no' in b else b for b in bag]
	innerBags = bag[1:]
	bagDict = {outerBag: {}}

	innerBags = [inner.split(' ') for inner in innerBags]
	
	for i in range(totalContainedBags):
		bagSize = innerBags[i][0]
		bagColour = ' '.join(innerBags[i][1:3])
		bagDict[outerBag][bagColour] = bagSize
	
	return bagDict	
	
def canBagBeContained(allBags, bagColour, targetBag):
	if allBags[bagColour] == {'':''} : return False

	if targetBag in allBags[bagColour].keys() : return True

	# if either key == targetBag return True
	# else
	# call canBagBeContained on each key 	
	# for every key
	# call canBagBeContained 
	bagKeys = list(allBags[bagColour].keys())

	results = []
	for key in bagKeys:
		results.append(canBagBeContained(allBags, key, targetBag))

	if True in results : return True



def partOne(allBags, targetBag):
	count = 0
	for bag in allBags:
		 if canBagBeContained(allBags, bag, 'shiny gold') : count += 1

	return count

def countInnerBags(allBags, targetBag, originalColour):
	tempDict = allBags[targetBag]
	if tempDict == {'':''} : return 1

	total = 0
	if tempDict.keys():
		for key in list(tempDict.keys()):
			count = int(tempDict.get(key))
			total += count * countInnerBags(allBags, key, originalColour)
	
	if targetBag == originalColour:
		return total
	else:
		return total + 1 




luggage = []
with open('input.txt', 'r') as file:
	for line in file:
		luggage.append(line.rstrip())

allBags = {}
for bag in luggage:
	bagAsDict = tokeniseBag(bag)
	key = bagAsDict.keys()
	allBags[list(key)[0]] = bagAsDict[list(key)[0]]


print("Part one: ", partOne(allBags, 'shiny gold'))
print("Part two: ", countInnerBags(allBags, 'shiny gold', 'shiny gold'))

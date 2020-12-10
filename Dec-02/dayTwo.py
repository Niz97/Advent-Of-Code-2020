

def tokenise(line):
	l = line.split()
	minAndMaxNums = l[0].split("-")

	token = {
		"minNumChar" : int(minAndMaxNums[0]),
		"maxNumChars" : int(minAndMaxNums[1]),
		"policyLetter" : l[1].replace(":", ""),
		"password" : l[2]
	}

	return token
	
	
	
def applyPartOnePolicy(token):
	count = 0
	for s in token["password"]:
		if s == token["policyLetter"]:
			count += 1
	if count >= token["minNumChar"] and count <= token["maxNumChars"]:
		return True
	return False

def applyPartTwoPolicy(token):
	posOne = False
	posTwo = False
	password = token["password"]
	if password[token["minNumChar"] - 1] == token["policyLetter"]:
		posOne = True
	if password[token["maxNumChars"] - 1] == token["policyLetter"]:
		posTwo = True

	if posOne != posTwo:
		return True
	
	return False



def partOne(tokens):
	count = 0
	for token in tokens:
		if applyPartOnePolicy(token):
			count += 1
	return count

def partTwo(tokens):
	count = 0
	for token in tokens:
		if applyPartTwoPolicy(token):
			count += 1
	return count


file = open("input.txt", "r")
tokens = [tokenise(line) for line in file]
print("Part 1: ", partOne(tokens))
print("Part 2: ", partTwo(tokens))

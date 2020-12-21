import math
import re
def splitPassports(file):
	allPassports = []
	passport = []
	for line in file:
		if not line.strip():
			allPassports.append(passport)
			passport = []
		else:
			line = line.replace('\n', '')
			line = line.split(' ')
			passport += line

	allPassports.append(passport)
	return allPassports

def passportToListDict(splitPassports):
	passports = []
	for passport in splitPassports:
		currentDict = {}
		for item in passport:
			keyValue = item.split(':')
			currentDict[keyValue[0]] = keyValue[1]
		passports.append(currentDict)

	return passports


def validatePresentFields(passportListDict):
	validPassports = []
	for passport in passportListDict:
		totalFields = len(passport)
		if totalFields == 8:
			validPassports.append(passport)
		elif totalFields == 7:
			if 'cid' not in passport.keys():
				validPassports.append(passport)

	return validPassports  

def partOne(splitPassports):
	passports = passportToListDict(splitPassports)
	validPassports = validatePresentFields(passports)
	return validPassports

def validateBirthYear(passport):
	return int(passport['byr']) >= 1920 and int(passport['byr']) <= 2002

def validateIssueYear(passport):
	return int(passport['iyr']) >= 2010 and int(passport['iyr']) <= 2020

def validateExpirationYear(passport):
	return int(passport['eyr']) >= 2020 and int(passport['eyr']) <= 2030

# def validateHeight(passport):
# 	height = passport['hgt']
# 	if 'cm' not in height and 'in' not in height:
# 		return False
# 	elif 'cm' in height:
# 		pos = height.find('cm')
# 		heightInCm = int(height[0:pos])
# 		if heightInCm >= 150 and heightInCm <= 193:
# 			return True
# 	elif 'in' in height:
# 		pos = height.find('in')
# 		heightInInches = int(height[0:pos])
# 		if heightInInches >= 59 and heightInInches <= 76:
# 			return True
# 	else:
# 		return False
def validateHeight(passport):
    if passport['hgt'][-2:] == "cm":
        return int(passport['hgt'][:-2]) >= 150 and int(passport['hgt'][:-2]) <= 193
    elif passport['hgt'][-2:] == "in":
        return int(passport['hgt'][:-2]) >= 59 and int(passport['hgt'][:-2]) <= 76


def validateHairColour(passport):

	return passport['hcl'][0] == "#" and  passport['hcl'][1:].isalnum()

def validateEyeColour(passport):
	eyeColours = ["amb", "blu", "brn",  "gry", "grn", "hzl", "oth"]
	return passport['ecl'] in eyeColours


def validatePassportId(passport):

	return len(passport['pid']) == 9


def partTwo(partialValid):
	count = 0
	for passport in partialValid:
		if not validateBirthYear(passport):
			continue
		if not validateIssueYear(passport):
			continue
		if not validateExpirationYear(passport):
			continue
		if not validateHeight(passport):
			continue
		if not validateEyeColour(passport):
			continue
		if not validatePassportId(passport):
			continue
		if not validateHairColour(passport):
			continue
		count += 1


	return count




passportsSplit = []
with open('input.txt', 'r') as file: 
	passportsSplit = splitPassports(file)

partialValid = partOne(passportsSplit)
print("Part one: ", len(partialValid))
print("Part two: ", partTwo(partialValid))



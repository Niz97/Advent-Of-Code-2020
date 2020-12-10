
file = open("dayOne.txt", "r")
nums = [int(line) for line in file]
setNums = set(nums)

def partOne(nums, setNums):
	for num in nums:
		if 2020 - num in setNums:
			return (num * (2020 - num))

def partTwo(nums, setNums):
	for num in nums:
		for numTwo in nums:
			if (2020 - num - numTwo) in setNums:
				return num * (2020 - num - numTwo) * numTwo

print("Part 1: ", partOne(nums, setNums))
print("Part 2: ", partTwo(nums, setNums))
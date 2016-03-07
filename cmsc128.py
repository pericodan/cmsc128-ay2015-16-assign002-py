#	Perico Dan B. Dionisio
#	CMSC 128 AB-1L


def getHammingDistance(str1, str2):
	distance = 0

	if type(str1) != str or type(str2) != str or len(str1) != len(str2):
		return "Error: Bad argument"
	for i in range (0, len(str1)):
		if str1[i]!=str2[i]:
			distance = distance + 1
	return distance


def countSubstrPattern(str1, str2):
	count = 0
	checker = 1

	if type(str1) != str or type(str2) != str:
		return "Error: Bad argument"
	for i in range (0, len(str1)-len(str2)+1):
		for j in range (0, len(str2)):
			if str1[i+j]!=str2[j]:
				checker = 0
		if checker == 1:
			count = count + 1
		checker = 1
	return count


def isValidStrings(str1, alphabet):
	if type(str1) != str or type(alphabet) != str:
		return "Error: Bad argument"
	for i in range (0, len(str1)):
		if str1[i] not in alphabet:
			return False
	return True


def getSkew(str1, n):
	answer = 0
	numOfG = 0
	numOfC = 0
	if type(str1) != str or type(n) != int or isValidStrings(str1, "ACGTU") == False:
		return "Error: Bad argument"
	if n < 1 or n > len(str1):
		return "Error"
	else:
		for i in range (0, n):
			if str1[i] == "G":
				numOfG = numOfG + 1
			if str1[i] == "C":
				numOfC = numOfC + 1
		return numOfG - numOfC


def getMaxSkewN(str1, n):
	max = False

	if type(str1) != str or type(n) != int or isValidStrings(str1, "ACGTU") == False:
		return "Error: Bad argument"
	if n < 1 or n > len(str1):
		return "Error"
	for i in range(1, n+1):
		temp = getSkew(str1, i)
		if max == False:
			max = temp
		if max < temp:
			max = temp
	return max


def getMinSkewN(str1, n):
	min = False

	if type(str1) != str or type(n) != int or isValidStrings(str1, "ACGTU") == False:
		return "Error: Bad argument"
	if n < 1 or n > len(str1):
		return "Error"
	for i in range(1, n+1):
		temp = getSkew(str1, i)
		if min == False:
			min = temp
		if min > temp:
			min = temp
	return min

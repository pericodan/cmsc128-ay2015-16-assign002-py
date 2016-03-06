def getHammingDistance(str1, str2):
	distance = 0
	if len(str1)==len(str2):
		for i in range (0, len(str1)):
			if str1[i]!=str2[i]:
				distance = distance + 1
		return distance
	else:
		return "Error: not the same length "

def countSubstrPattern(str1, str2):
	count = 0
	checker = 1
	for i in range (0, len(str1)-len(str2)+1):
		for j in range (0, len(str2)):
			if str1[i+j]!=str2[j]:
				checker = 0
		if checker == 1:
			count = count + 1
		checker = 1
	return count

def isValidStrings(str, alphabet):
	for i in range (0, len(str)):
		if str[i] not in alphabet:
			return False
	return True

def getSkew(str, n):
	answer = 0
	numOfG = 0
	numOfC = 0
	if n < 1 or n > len(str):
		return "Error"
	else:
		for i in range (0, n):
			if str[i] == "G":
				numOfG = numOfG + 1
			if str[i] == "C":
				numOfC = numOfC + 1
		return numOfG - numOfC

def getMaxSkewN(str, n):
	max = False
	for i in range(1, n+1):
		temp = getSkew(str, i)
		if max == False:
			max = temp
		if max < temp:
			max = temp
	return max

def getMinSkewN(str, n):
	min = False
	for i in range(1, n+1):
		temp = getSkew(str, i)
		if min == False:
			min = temp
		if min > temp:
			min = temp
	return min

print getHammingDistance("AACCTT","GGCCTT")
print countSubstrPattern("AATATATAGG","ACTGACTGACTG")
print isValidStrings("AAGGCTATGC", "ACGT")
print getMaxSkewN("GGCCAC", 1)
print "Edit: Defensive programming"

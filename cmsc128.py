#	Perico Dan B. Dionisio
#	CMSC 128 AB-1L


def getHammingDistance(str1, str2):                                             #this function will get the Hamming Distance between two string
	distance = 0

	if type(str1) != str or type(str2) != str or len(str1) != len(str2)or str1=="" or str2=="":        #to check if the arguments are valid
		return "Error: Bad argument"
	for i in range (0, len(str1)):
		if str1[i]!=str2[i]:                                                    #to compare each character
			distance = distance + 1
	return distance


def countSubstrPattern(str1, str2):                                             #this function will return the number of times str2 occured in str1
	count = 0
	checker = 1

	if type(str1) != str or type(str2) != str or str1=="" or str2=="":          #to check if the arguments are valid
		return "Error: Bad argument"
	for i in range (0, len(str1)-len(str2)+1):
		for j in range (0, len(str2)):                                          #this will count the number of occurence of str2 starting from each index of str1
			if str1[i+j]!=str2[j]:
				checker = 0
		if checker == 1:
			count = count + 1
		checker = 1
	return count


def isValidString(str1, alphabet):                                              #this will check if the string is a valid string based on the given alphabet
    badArg = False
    if type(str1) != str or type(alphabet) != str or str == "" or alphabet == "":
		return "Error: Bad argument"
    for j in range(0, len(alphabet)):                                           #to check if the alphabet is unique
        for k in range(j+1, len(alphabet)):
            if alphabet[j] == alphabet[k]:
                badArg = True
    if (badArg==True):
        return "Error: Alphabet is not unique"
    else:
    	for i in range (0, len(str1)):
    		if str1[i] not in alphabet:                                         #this will check if every character in string is in the given alphabet
    			return False
    	return True


def getSkew(str1, n):                                                           #this will solve for the difference of number of G and number of C from index 1 to n
	answer = 0
	numOfG = 0
	numOfC = 0
	if type(str1) != str or type(n) != int:                                     #to check if the arguments are valid
		return "Error: Bad argument"
	if n < 1 or n > len(str1):
		return "Error"
	else:
		for i in range (0, n):
			if str1[i] == "G":
				numOfG = numOfG + 1                                             #to count the occurence of G
			if str1[i] == "C":
				numOfC = numOfC + 1                                             #to count the occurence of C
		return numOfG - numOfC


def getMaxSkewN(str1, n):                                                       #to get the maximum skew from 1 to n
	max = "Empty"

	if type(str1) != str or type(n) != int:                                     #to check if the arguments are valid
		return "Error: Bad argument"
	if n < 1 or n > len(str1):
		return "Error"
	for i in range(1, n+1):
		temp = getSkew(str1, i)
		if max == "Empty":                                                        #initial maximum
			max = temp
		elif max < temp:
			max = temp
	return max


def getMinSkewN(str1, n):                                                       #to get the maximum skew from 1 to n
	min1 = "Empty"
	if type(str1) != str or type(n) != int:                                     #to check if the arguments are valid
		return "Error: Bad argument"
	if n < 1 or n > len(str1):
		return "Error"
	for i in range(1, n+1):
		temp = getSkew(str1, i)
		if min1 == "Empty":                                                        #initial minimum
			min1 = temp
		elif min1 > temp:
			min1 = temp
	return min1



input = open("input.txt")
lines = [line.strip() for line in input]
input.close()

width = len(lines[0])

gammaRateBinary = ""
epsilonRateBinary = ""

for i in range(width):
	negativeBitCount = 0;
	positiveBitCount = 0;
	for line in lines:
		positiveBitCount += 1 if line[i] == "1" else 0
		negativeBitCount += 1 if line[i] == "0" else 0
	gammaRateBinary += "1" if positiveBitCount > negativeBitCount else "0" 		# common bit
	epsilonRateBinary += "1" if positiveBitCount < negativeBitCount else "0"	# uncommon bit

gammaRateDecimal = int(gammaRateBinary, 2)
epsilonRateDecimal = int(epsilonRateBinary, 2)

print("Gamma Rate: ", gammaRateDecimal)
print("Epsilon Rate: ", epsilonRateDecimal)
print("Power consumption: ", gammaRateDecimal * epsilonRateDecimal)


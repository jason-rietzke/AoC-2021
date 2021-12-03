

input = open("input.txt")
lines = [line.strip() for line in input]
input.close()

oxygenGeneratorRating = lines
co2ScrubberRating = lines

width = len(lines[0])

for i in range(width):
	if len(oxygenGeneratorRating) > 1:
		negativeBitCount = 0;
		positiveBitCount = 0;
		for line in oxygenGeneratorRating:
			positiveBitCount += 1 if line[i] == "1" else 0
			negativeBitCount += 1 if line[i] == "0" else 0
		oxygenGeneratorRating = [line for line in oxygenGeneratorRating if line[i] == ("1" if positiveBitCount >= negativeBitCount else "0")]
	
	if len(co2ScrubberRating) > 1:
		negativeBitCount = 0;
		positiveBitCount = 0;
		for line in co2ScrubberRating:
			positiveBitCount += 1 if line[i] == "1" else 0
			negativeBitCount += 1 if line[i] == "0" else 0
		co2ScrubberRating = [line for line in co2ScrubberRating if line[i] == ("0" if negativeBitCount <= positiveBitCount else "1")]

oxygenGeneratorRatingDecimal = int(oxygenGeneratorRating[0], 2)
co2ScrubberRatingDecimal = int(co2ScrubberRating[0], 2)

print("Oxygen Generator Rate: ", oxygenGeneratorRatingDecimal)
print("CO2 Scrubber Rate: ", co2ScrubberRatingDecimal)
print("Life Support Rating: ", oxygenGeneratorRatingDecimal * co2ScrubberRatingDecimal)


# Riddler puzzle - How Long Can You Roll?
# what is the average score of rolling a 10 sided dice, non-increasing sequence, and stopping at 0.

import random

def simul(n):
	summed = 0
	# n simulations
	for i in range(n):
		s = "0."
		go = True
		while (go):
			currentRoll = random.randint(0,9)
			if (currentRoll == 0):  # stop on roll of 0
				if (s == "0."):
					s += "0"
				break
			if (s == "0." or prevRoll >= currentRoll):   # add to number if first one or prev one is not lower
				s += str(currentRoll)
				prevRoll = currentRoll

		summed += float(s)

	return summed/n

print(simul(10000))  # gives us avg of ~~0.4736 with 10,000 simulations

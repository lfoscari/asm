import numpy as np
from itertools import accumulate

N=10
SYMBOLS=[0, 1, 2]
PROBABILITIES=[0.9, 0.05, 0.05]

class ASM:
	PRECISION=1024

	def __init__(self):
		# Map probabilities from R[0, 1] to N[0, d], there d := PRECISION
		self.classes_sizes = [np.round(p * self.PRECISION) for p in PROBABILITIES]
		self.classes_edges = list(accumulate(self.classes_sizes))

		# Initial value for representation
		self.representation = 0

		assert self.classes_edges[-1] == self.PRECISION

	def push(self, new):
		self.representation = ( int( np.floor(self.representation) / self.classes_sizes[new] ) << \
			self.PRECISION ) + self.classes_edges[new] \
				+ ( new % self.classes_sizes[new] )

	def pop(self):
		s = self.representation % np.power(2, self.PRECISION)
		self.representation = ( self.representation >> d ) * \
			self.classes_sizes[s] + s - self.classes_edges[s]
		return s

def main():
	S = ASM()

	# Generate a sequence of N SYMBOLS with the
	# right PROBABILITIES
	sequence = np.random.choice(SYMBOLS, N, p=PROBABILITIES)

	for symbol in sequence:
		S.push(symbol)

	print("Result: ", S.representation)

	for symbol in sequence:
		assert symbol == S.pop()

	print("It worked")

if __name__ == "__main__":
	main()

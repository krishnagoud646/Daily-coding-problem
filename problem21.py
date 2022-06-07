"""The power set of a set is the set of all its subsets. Write a function that, given a set, generates its power set.

For example, given the set {1, 2, 3}, it should return {{}, {1}, {2}, {3}, {1, 2}, {1, 3}, {2, 3}, {1, 2, 3}}."""


def powerSet(set):

	N = int(pow(2, len(set)))
	s = list()

	# generate each subset one by one
	for i in range(N):
		for j in range(len(set)):
			if i & (1 << j):
				s.append(set[j])

		print(s)
		s.clear()


if __name__ == '__main__':

	set = [1, 2, 3]
	powerSet(list(set))


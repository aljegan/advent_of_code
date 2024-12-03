# day 1
from typing import List, Tuple
from collections import defaultdict

def parse_data() -> Tuple[List[int]]:
	left = []
	right = []
	with open("day01.txt", "rb") as f:
		for line in f.readlines():
			l, r = line.split()
			left.append(int(l))
			right.append(int(r))
	return left, right


def calc_distance(data: Tuple[List[int]]) -> int:
	left, right = data
	left = sorted(left)
	right = sorted(right)
	return sum([abs(l - r) for l, r in zip(left, right)])


def calc_similarity(data: Tuple[List[int]]) -> int:
	left, right = data
	right_map = defaultdict(lambda : 0)
	for r in right:
		right_map[r] += 1
	result = 0
	for l in left:
		result += l * right_map[l]
	return result



if __name__ == "__main__":
	data = parse_data()
	print(calc_distance(data))
	print(calc_similarity(data))
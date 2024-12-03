# day 2
from typing import List, Callable


def read_data() -> List[List[int]]:
	data = []
	with open("day02.txt", "rb") as f:
		for l in f.readlines():
			data.append([int(i) for i in l.split()])
	return data


def is_increasing_safe(l: List[int]) -> bool:
	# won't work if length of l < 2
	for i in range(len(l) - 1):
		if not (1 <= l[i+1] - l[i] <= 3):
			return False
	return True


def is_safe(l: List[int]) -> bool:
	return is_increasing_safe(l) or is_increasing_safe(l[::-1])


def is_safe_dampener(l: List[int]) -> bool:
	if is_safe(l):
		return True
	for i in range(len(l)):
		if is_safe(l[:i] + l[i+1:]):
			return True
	return False


def eval_reports(reports: List[List[int]], evaluator: Callable) -> int:
	return sum([int(evaluator(r)) for r in reports])


if __name__ == "__main__":
	reports = read_data()
	print(eval_reports(reports, is_safe))
	print(eval_reports(reports, is_safe_dampener))
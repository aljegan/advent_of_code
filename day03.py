# day 3
from typing import List


def read_instructions() -> List[int]:
	with open("day03.txt", "r") as f:
		return f.read()
	


def extract_instructions(raw: str) -> List[str]:
	left_delim = "mul("
	left_delim_length = len(left_delim)
	left = 0
	instructions = []
	while left < len(raw) - left_delim_length:
		if raw[left:left + left_delim_length] == left_delim:
			right = left+left_delim_length
			has_valid_instruction = False
			while right < len(raw):
				if raw[right] == ")":
					instructions.append(raw[left+left_delim_length:right])
					break
				if raw[right] not in "0123456789,":
					break
				right += 1
			left = right
		else:
			left += 1
	return instructions


def do_calculations(instructions: List[str]) -> int:
	result = 0
	for i in instructions:
		s = i.split(",")
		if len(s) != 2:
			continue
		result += int(s[0]) * int(s[1])
	return result


def evaluate(inpt: str) -> int:
	return do_calculations(extract_instructions(inpt))


def evaluate_do_dont(inpt: str) -> int:
	mode = 1
	left = 0
	right = 0
	total = 0

	while right < len(inpt) - len("don't()"):
		if inpt[right:right + len("do()")] == "do()":
			if mode == 1:
				eval_string = inpt[left:right]
				total += evaluate(eval_string)
			mode = 1
			left = right + len("do()")
			right = left
		if inpt[right:right + len("don't()")] == "don't()":
			if mode == 1:
				eval_string = inpt[left:right]
				total += evaluate(eval_string)
			mode = 0
			left = right + len("don't()")
			right = left
		right += 1
	right = len(inpt)
	if mode == 1:
		eval_string = inpt[left:right]
		total += evaluate(eval_string)
	return total




if __name__ == "__main__":
	raw = read_instructions()
	print(evaluate(raw))
	print(evaluate_do_dont(raw))
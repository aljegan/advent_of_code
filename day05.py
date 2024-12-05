from typing import Tuple, Set, Dict, List
from collections import defaultdict


def parse_data() -> Tuple[Dict[int, Set[int]], List[List[int]]]:
    constraints = defaultdict(set)
    updates = []
    with open("day05.txt", "r") as f:
        l = f.readline().strip()
        while l:
            before, after = [int(i) for i in l.strip().split("|")]
            constraints[after].add(before)
            l = f.readline().strip()
        l = f.readline().strip()
        while l:
            updates.append([int(i) for i in l.strip().split(",")])
            l = f.readline().strip()
    return constraints, updates


def valid(update: List[int], all_constraints: Dict[int, Set[int]]) -> bool:
    seen_pages = set()
    for i, page in enumerate(update):
        later_pages = set(update[i + 1:])
        constraints = all_constraints[page]
        if not seen_pages >= constraints and constraints.intersection(
                later_pages):
            return False
        seen_pages.add(page)
    return True


def validate_line(update: List[int], all_constraints: Dict[int, Set[int]]) -> int:
    return line_value(update) if valid(update, all_constraints) else 0


def transform_line(update: List[int], all_constraints: Dict[int, Set[int]]) -> List[int]:
    candidate = []
    for i, page in enumerate(update):
        candidate.append(page)
        j = i
        while not valid(candidate, all_constraints):
            # Move the right-most element of candidate left until you get a valid ordering
            c_j_1 = candidate[j-1]
            c_j = candidate[j]
            candidate[j-1] = c_j
            candidate[j] = c_j_1
            j -= 1
    return candidate


def line_value(update):
    return update[len(update) // 2]


def part1(constraints: Dict[int, Set[int]], updates: List[List[int]]) -> int:
    result = 0
    for update in updates:
        current = validate_line(update, constraints)
        result += current
    return result

def part2(constraints: Dict[int, Set[int]], updates: List[List[int]]) -> int:
    result = 0
    for update in updates:
        if not valid(update, constraints):
            result += line_value(transform_line(update, constraints))
    return result


if __name__ == "__main__":
    cons, upds = parse_data()
    print(part1(cons, upds))
    print(part2(cons, upds))

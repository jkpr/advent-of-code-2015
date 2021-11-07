from typing import List


def run_program(initial_a, initial_b, lines):
    reg_a = initial_a
    reg_b = initial_b
    instruction = 0
    while i := lines[instruction]:
        print(instruction, i)
        if i.startswith("hlf "):
            reg = i[4]
            if reg == "a":
                reg_a //= 2
            elif reg == "b":
                reg_b //= 2
            else:
                raise NotImplementedError(i)
            instruction += 1
        elif i.startswith("tpl "):
            reg = i[4]
            if reg == "a":
                reg_a *= 3
            elif reg == "b":
                reg_b *= 3
            else:
                raise NotImplementedError(i)
            instruction += 1
        elif i.startswith("inc "):
            reg = i[4]
            if reg == "a":
                reg_a += 1
            elif reg == "b":
                reg_b += 1
            else:
                raise NotImplementedError(i)
            instruction += 1
        elif i.startswith("jmp "):
            offset = int(i[4:])
            instruction += offset
        elif i.startswith("jie "):
            reg = i[4]
            offset = int(i[7:])
            if reg == "a" and reg_a % 2 == 0:
                instruction += offset
            elif reg == "b" and reg_b % 2 == 0:
                instruction += offset
            else:
                instruction += 1
        elif i.startswith("jio "):
            reg = i[4]
            offset = int(i[7:])
            if reg == "a" and reg_a == 1:
                instruction += offset
            elif reg == "b" and reg_b == 1:
                instruction += offset
            else:
                instruction += 1
        if not 0 <= instruction < len(lines):
            break
    return reg_b


def part1(lines: List[str]):
    return run_program(0, 0, lines)


def part2(lines: List[str]):
    return run_program(1, 0, lines)

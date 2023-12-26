mystring = open("input.txt", "r").readlines()
final_sum = 0
matrix = [
    [-1, 0],
    [-1, 1],
    [0, 1],
    [1, 1],
    [1, 0],
    [1, -1],
    [0, -1],
    [-1, -1],
]


def part1():
    global final_sum
    for row, y in enumerate(mystring):
        gotem = False
        current_num = 0
        for col, x in enumerate(list(y)):
            if x.isdigit():
                current_num = current_num * 10 + int(x)
                for dx, dy in matrix:
                    p_row = row + dx
                    p_col = col + dy
                    if (
                        p_row >= 0
                        and p_col >= 0
                        and p_row < len(mystring)
                        and p_col > len(y[0]) - 1
                        and mystring[p_row][p_col] not in ".\n"
                        and not mystring[p_row][p_col].isdigit()
                    ):
                        gotem = True
            elif gotem:
                final_sum += current_num
                gotem = False
                current_num = 0  # found but now clearing buffer
            else:
                current_num = 0  # if no any special symbol found
    print(final_sum)
    final_sum = 0


def part2():
    global final_sum
    num_count: dict = {}
    for row, y in enumerate(mystring):
        gotem = False
        current_num = 0
        star_pos = 0, 0
        for col, x in enumerate(list(y)):
            if x.isdigit():
                current_num = current_num * 10 + int(x)
                for dx, dy in matrix:
                    p_row = row + dx
                    p_col = col + dy
                    if (
                        p_row >= 0
                        and p_col >= 0
                        and p_row < len(mystring)
                        and p_col < len(y)
                        and mystring[p_row][p_col] not in ".\n"
                        and mystring[p_row][p_col] == "*"
                    ):
                        gotem = True
                        star_pos = p_row, p_col

            elif gotem:
                if star_pos not in num_count:
                    num_count[star_pos] = [current_num]
                else:
                    num_count[star_pos].append(current_num)
                # or
                # num_count[star_pos] = num_count.get(star_pos, []) + [current_num]
                gotem = False
                current_num = 0
            else:
                current_num = 0

    for el in num_count.values():
        if len(el) % 2 == 0:
            multi = el.pop(0) * el.pop(0)
            final_sum = final_sum + multi
    print(final_sum)


def main():
    part1()
    part2()


if __name__ == "__main__":
    main()

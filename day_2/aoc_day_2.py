import re
from itertools import zip_longest

mystring = open("input.txt", "r").read()


def part1():
    red = 12
    green = 13
    blue = 14
    sum: int = 0
    for i in mystring.split("\n"):
        flag = 0
        index = re.match(r"Game (\d+)", i)
        b = re.findall(r"(\d+)\sblue", i)
        r = re.findall(r"(\d+)\sred", i)
        g = re.findall(r"(\d+)\sgreen", i)
        for _r, _b, _g in zip_longest(r, b, g):
            _r = int(_r) if _r else 0
            _b = int(_b) if _b else 0
            _g = int(_g) if _g else 0
            if index and (_r > red or _b > blue or _g > green):
                flag = 1
        if not flag and index:
            sum += int(index.group(1))

    print(sum)


def part2():
    final_sum: int = 0

    for i in mystring.split("\n"):
        R_long: int = 1
        G_long: int = 1
        B_long: int = 1
        index = re.match(r"Game (\d+)", i)
        b = re.findall(r"(\d+)\sblue", i)
        r = re.findall(r"(\d+)\sred", i)
        g = re.findall(r"(\d+)\sgreen", i)
        for _r, _b, _g in zip_longest(r, b, g):
            _r = int(_r) if _r else 1
            _b = int(_b) if _b else 1
            _g = int(_g) if _g else 1

            if index:
                if _r > R_long:
                    R_long = _r
                if _g > G_long:
                    G_long = _g
                if _b > B_long:
                    B_long = _b
        res = R_long * G_long * B_long
        final_sum += res

    print(final_sum)


def main():
    part1()
    part2()


if __name__ == "__main__":
    main()

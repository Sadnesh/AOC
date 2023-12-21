"""
retrieve the first and last digit from every string and make a 2 digit number if there is only one number then it repeats.
sum all the values and that will be the result 
"""

array = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}
ae = {
    "s": ["six", "seven"],
    "e": ["eight"],
    "t": ["two", "three"],
    "n": ["nine"],
    "f": ["four", "five"],
    "o": ["one"],
}


def sum(first_d: str, last_d: str, final_sum: int):
    concat = first_d + last_d
    con = int(concat)
    final_sum = final_sum + con
    return final_sum


def part1():
    file = open("input.txt", "r")
    mystring = file.read()
    final_sum: int = 0

    for line in mystring.split("\n"):
        first_d: str = ""
        last_d: str = ""
        for element in line:
            if element.isnumeric():
                if first_d == "":
                    first_d = element
                last_d = element
        final_sum = sum(first_d, last_d, final_sum)

    print(final_sum)
    file.close()


def part2():
    file = open("input.txt", "r")
    mystring = file.read()
    final_sum: int = 0

    for a in mystring.split("\n"):
        first_d: str = ""
        last_d: str = ""
        for n, element in enumerate(a):
            if element.isdigit():
                if first_d == "":
                    first_d = element
                last_d = element
            elif element in ae:
                for i in ae.get(element, []):
                    if n <= len(a) - len(i):
                        if a[n : n + len(i)] == i:
                            if first_d == "":
                                first_d = array.get(i, "")
                            last_d = array.get(i, "")
        final_sum = sum(first_d, last_d, final_sum)

    print(final_sum)
    file.close()


def main():
    part1()
    part2()


if __name__ == "__main__":
    main()

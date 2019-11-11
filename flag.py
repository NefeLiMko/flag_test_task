from sys import argv, exit
from argparse import ArgumentError


def validator(f):
    def inner(*args):
        num = args[0]
        if num.isdigit():
            if int(num) % 2 == 0 and int(num) != 0:
                return f(int(num))
        raise ArgumentError(None, "Invalid input")
    return inner


@validator
def flag(n):
    vertical_dist = int(n/2)
    circle = ""
    wrapper = "#" * (n*3+2) + "\n"

    for i in range(vertical_dist):
        circle += "#{:^{width}}#\n".format("*{}*".format("o"*i*2), width=n*3)
        wrapper += "#{:^{width}}#\n".format(" ", width=n*3)

    wrapper += circle
    wrapper = wrapper[:-1] + wrapper[::-1]

    return wrapper


if __name__ == "__main__":
    n = input("Enter a valid even integer number please : ")
    print(flag(n))
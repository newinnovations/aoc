#!/usr/bin/env python3


def main():
    with open("ref.txt") as f:
        for line in f:
            print(line.strip())


if __name__ == "__main__":
    main()

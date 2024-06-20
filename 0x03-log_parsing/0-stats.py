#!/usr/bin/python3
""" script that reads stdin line by line and computes metrics"""
import sys


def print_stats(file_size, status):
    """ print stats """
    print(f"File size: {file_size}")
    for key in sorted(status.keys()):
        if status[key] != 0:
            print(f"{key}: {status[key]}")


def main():
    """ main function """
    countre = 0
    file_size = 0
    status = {s: 0 for s in [200, 301, 400, 401, 403, 404, 405, 500]}
    try:
        for line in sys.stdin:
            countre += 1
            data = line.split()
            try:
                file_size += int(data[-1])
                status[int(data[-2])] += 1
            except Exception:
                pass
            if countre % 10 == 0:
                print_stats(file_size, status)
        print_stats(file_size, status)
    except KeyboardInterrupt:
        print_stats(file_size, status)
        raise


if __name__ == "__main__":
    main()

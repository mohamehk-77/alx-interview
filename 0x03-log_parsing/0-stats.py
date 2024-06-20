#!/usr/bin/env python3
import sys
import signal

total_file_size = 0
status_codes_count = {200: 0, 301: 0, 400: 0,
                      401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
line_count = 0


def print_stats():
    print(f"File size: {total_file_size}")
    for code in sorted(status_codes_count):
        if status_codes_count[code] > 0:
            print(f"{code}: {status_codes_count[code]}")


def signal_handler(sig, frame):
    print_stats()
    sys.exit(0)


signal.signal(signal.SIGINT, signal_handler)

for line in sys.stdin:
    parts = line.split()
    if len(parts) != 9:
        continue
    ip, _, _, date, request, _, status_code, file_size = parts[0], parts[
        1], parts[2], parts[3], parts[4], parts[5], parts[6], parts[7]

    try:
        status_code = int(status_code)
        file_size = int(file_size)
    except ValueError:
        continue

    if status_code not in status_codes_count:
        continue

    total_file_size += file_size
    status_codes_count[status_code] += 1
    line_count += 1

    if line_count % 10 == 0:
        print_stats()

print_stats()

"""
RECORD CHECK  -  my version
===========================

Name  :  Leon Beaupere
Lane  :  Cyber
Date  :  07/11/2026

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""


def parse_line(raw_line):
    """clean and parse one raw line into dictionnary"""
    line = raw_line.strip()
    hostname_part, rest = line.split(",",1)
    record = {"hostname": hostname_part.strip().lower()}

    for i in rest.split(","):
        key, value = i.split("=")
        record[key.strip().lower()] = float(value.strip())

    return(record)

def status_of(record):
    """return over limit, warnnig or ok from a record's usage pourcentage"""
    percent = record["used"] / record["total"] * 100
    if percent >= 100:
        return("OVER LIMIT")
    elif percent >= 90:
        return("WARNING")
    else:
        return("OK")

raw_records = []

with open("servers.txt") as f:
    for i in f:
        raw_records.append(i)

count = 0

for i in raw_records:
    record = parse_line(i)
    status = status_of(record)

    print(record, status)

    if status != "OK":
        count += 1

print(f"{len(raw_records)} record, {count} flagged")
input()

#error with Srv-07 , used=abc , total=100 : ValueError: could not convert string to float: 'abc'
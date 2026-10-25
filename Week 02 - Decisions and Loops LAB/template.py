"""
RECORD CHECK  -  LEON
===========================

Name  : Leon Beaupere
Lane  :   Cyber
Date  : 03/11/2026

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""
label = ""
nb_over = 0

while True:


    label = input("Enter a source IP : ")
    if label == "quit":
        break
    value = int(input("Enter number of failed login attempt : "))
    limit = int(input("Enter number of total attempts possible : "))



    difference = limit - value
    percent = value / limit * 100
    if percent < 90:
        status = "OK"
    elif percent < 100:
        status = "WARNING"
    else:
        status = "OVER LIMIT"
        nb_over += 1

    print()
    print("=" * 34)
    print(f"  RECORD CHECK  -  {label}")
    print("=" * 34)

    print(f"  Failed login attempts   : {value:11.2f}")
    print(f"  Total attempts possible : {limit:11.2f}")
    print(f"  Remaining attempts      : {difference:11.2f}")
    print(f"  Failed login percent    : {percent:11.2f} %")
    print(f"  Status                  : {status:>11}")

    print("=" * 34)

print(f"Number of over limit : {nb_over}")
"""
RECORD CHECK  -  my version
===========================

Name  : Leon Beaupere
Lane  :  Cyber 
Date  : 10/11/2026

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

def status_of(percent):
    """Return the status : 'OVER LIMIT', 'WARNING' or 'OK' """
    if percent >= 100:
        return("OVER LIMIT")
    elif percent >= 90:
        return("WARNING")
    else:
        return("OK")

def check(value, limit):
    """Returns the difference and the percentage of the two values"""
    return(limit-value,(value / limit) *100)

def print_report(label, value, limit, difference, percent, status):
    """Print the report with all the informations"""
    print()
    print("=" * 34)
    print(f"  RECORD CHECK  -  {label}")
    print("=" * 34)

    print(f"  Used        : {value:11.2f}")
    print(f"  Total       : {limit:11.2f}")
    print(f"  Free        : {difference:11.2f}")
    print(f"  Percent     : {percent:11.2f} %")
    print(f"  Status      : {status:>11}")

    print("=" * 34)


label = ""
nb_over = 0

while True:


    label = input("Enter a source IP : ")
    if label == "quit":
        break
    value = float(input("Enter number of failed login attempt : "))
    limit = float(input("Enter number of total attempts possible : "))


    difference = check(value, limit)[0]
    percent = check(value, limit)[1]
    status = status_of(percent)

    if status == "OVER LIMIT":
        nb_over += 1
    print_report(label, value, limit, difference, percent, status)

print(f"Number of over limit : {nb_over}")
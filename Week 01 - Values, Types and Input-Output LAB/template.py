"""
RECORD CHECK  -  LEON B.
===========================

Name  : Leon Beaupere
Lane  :  Cyber 
Date  :  03/11/2026

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

Source_IP = input("Enter a source IP : ")
Failed_login = int(input("Enter number of failed login attempt : "))
Total_login = int(input("Enter number of total attempts possible : "))


Remaining_attempts = Total_login - Failed_login
Percent_failed = Failed_login / Total_login * 100
Percent_remaining = 100 - Percent_failed


print()
print("=" * 34)
print(f"  RECORD CHECK  -  {Source_IP}")
print("=" * 34)

print(f"  Failed login attempts   : {Failed_login:+11.2f}")
print(f"  Total attempts possible : {Total_login:+11.2f}")
print(f"  Remaining attempts      : {Remaining_attempts:+11.2f}")
print(f"  Failed login percent    : {Percent_failed:+11.2f} %")
print(f"  Remaining login percent : {Percent_remaining:+11.2f} %")

print("=" * 34)
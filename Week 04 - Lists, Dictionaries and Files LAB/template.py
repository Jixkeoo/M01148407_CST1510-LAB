"""
RECORD CHECK  -  my version
===========================

Name  :  Leon Beaupere
Lane  :  Cyber
Date  :  17/10/2026

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

def check_record(value, limit):
    """return the difference and percent from a value and a limit"""
    if value - limit < 0:
        difference = limit - value
    else:
        difference = value - limit
    percent = (value / limit) * 100
    return(difference, percent)


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



def load_records(path):
    """"""
    try:
        records = []
        with open(path) as f:
            for i in f:
                label,value,limit = i.strip().split(",")
                records.append({"label":label,"value":int(value),"limit":int(limit)})
        return(records)
    except FileNotFoundError:
        print("File not found")

records = load_records("my_records.txt")
count = 0

with open("my_results.txt","w"):
    for i in records:
        difference, percent = check_record(i["value"],i["limit"])
        if i["value"] > i["limit"]:
            print_report(i["label"],i["value"],i["limit"],difference,percent, "OVER LIMIT")
            count += 1
        else:
            print_report(i["label"],i["value"],i["limit"],difference,percent, "OK")
        
print("\nNumber of OVER LIMIT :",count)

